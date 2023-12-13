import pygame as pg
import random

class Tetromino:
    def __init__(self, x, y, grille):
        
        #position x, y of the tetromino
        self.x = x
        self.y = y

        self.COLOR =[
            (255,0,0),
            (0,255,0),
            (0,0,255),
            (255,255,0),
            (0,255,255),
            (255,0,255),
            (255,255,255)
        ]
        
        # 4x4 matrix of each tetromino shape and orientation in a list of list of list
        #each number is equal to the position in the matrix beginning at 0
        #  0  1  2  3
        #  4  5  6  7
        #  8  9  10 11
        #  12 13 14 15
        self.list_shape = [
            [[1, 5, 9, 13], [4, 5, 6, 7]], #I
            [[4, 5, 9, 10], [2, 6, 5, 9]], #Z
            [[6, 7, 9, 10], [1, 5, 6, 10]], #S
            [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]], #T
            [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]], #L
            [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], #J
            [[1, 2, 5, 6]], #O
        ]
        #choose random shape and colors
        self.shape = random.randint(0, len(self.list_shape)-1) #choose a shape
        self.color = random.choice(self.COLOR) #choose a color
        self.rotation = 0 # initial rotation

        self.grille = grille #call the an object Grille
        self.height = len(self.grille.get_grille()) #get the height from the object
        self.width = len(self.grille.get_grille()[0]) #get the width from the object

        
    def image(self) -> list:
        """return the right shape and rotation of the tetromino"""
        return self.list_shape[self.shape][self.rotation]

    def rotate(self) -> None:
        """rotate by going through each matrix of the tetromino"""
        self.rotation = (self.rotation + 1) % len(self.list_shape[self.shape])
    
    def collide(self) -> bool:
        """Check for collision"""
        collide = False #Assume it's false in the start
        for i in range(4): #going through the y coordonate of the matrix 4x4
            for j in range(4): #going through the x coordinate of the matrix 4x4
                if i * 4 + j in self.image(): #check for point in the tetromino right orientation
                    #check if the tetromino doesn't leave the height, width of the screen and if there's no other tetromino
                    if i + self.y > self.height - 1 or \
                            j + self.x > self.width - 1 or \
                            j + self.x < 0 or \
                            self.grille.get_grille()[i + self.y][j + self.x] != ".":
                        collide = True 
        return collide
    
    def go_side(self, dx:int) -> None:
        """Put the tetromino to the left or right
            if it doesn't collide on the way"""
        old_x = self.x
        self.x += dx
        if self.collide(): #go back to the old position if it collide
            self.x = old_x
    
    def rotate_tetromino(self) -> None:
        """Rotate the tetromino but if it collide,
            go back to the previous orientation"""
        old_rotation = self.rotation
        self.rotate()
        if self.collide(): #go back to the old rotation if it collide
            self.rotation = old_rotation
            
    def go_down(self) -> bool:
        """Make the tetromino go down if it doesn't collide"""
        self.y += 1
        if self.collide(): 
            self.y -= 1
            return True
        return False

    def display_tetromino(self, screen, affichage, current)-> None:
        """Display the tetromino"""
        shape = self.image()
        matrix = [[0 for _ in range(4)] for _ in range(4)]
        #Re-create the matrix of the tetromino:
        for block in shape: 
            matrix[block // 4][block % 4] = 1
        #Display each blocks:
        for i in range(len(matrix)):
            for j in range(len(matrix [i])):
                if matrix[i][j] == 1:
                    if current:
                        x = j * affichage.taille_case + affichage.pos_grille[0] + self.x * affichage.taille_case
                        y = i * affichage.taille_case + affichage.pos_grille[1] + self.y * affichage.taille_case
                    else:
                        x = affichage.pos_next_piece[0] + j * affichage.taille_case
                        y = affichage.pos_next_piece[1] + i * affichage.taille_case
                    pg.draw.rect(screen, self.color, (x, y, affichage.taille_case, affichage.taille_case))
