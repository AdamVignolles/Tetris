import pygame as pg
import random

COLOR = [
    (255,0,0),
    (0,255,0),
    (0,0,255),
    (255,255,0),
    (0,255,255),
    (255,0,255),
    (255,255,255)
]
class Tetromino:
    def __init__(self, x, y, grille):
        #position x, y of the tetromino
        self.x = x
        self.y = y
        # 4x4 matrix of each tetromino shape and orientation in a list of list of list
        #each number is equal to the position in the matrix beginning at 0
        self.list_shape = [
            [[1, 5, 9, 13], [4, 5, 6, 7]],
            [[4, 5, 9, 10], [2, 6, 5, 9]],
            [[6, 7, 9, 10], [1, 5, 6, 10]],
            [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
            [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
            [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
            [[1, 2, 5, 6]],
        ]
        #choose random shape and colors
        self.shape = random.randint(0, len(self.list_shape)-1)
        self.color = random.choice(COLOR)
        self.rotation = 0

        self.grille = grille
        self.height = len(self.grille.get_grille())
        self.width = len(self.grille.get_grille()[0])

        
    def image(self):
        """return the right shape and rotation of the tetromino"""
        return self.list_shape[self.shape][self.rotation]

    def rotate(self):
        """rotate by going through each matrix of the tetromino"""
        self.rotation = (self.rotation + 1) % len(self.list_shape[self.shape])
    
    def collide(self):
        """Check for collision"""
        collide = False
        for i in range(4): #going through the y coordonate of the matrix 4x4
            for j in range(4): #going through the x coordinate of the matrix 4x4
                if i * 4 + j in self.image(): #see if
                    if i + self.y > self.height - 1 or \
                            j + self.x > self.width - 1 or \
                            j + self.x < 0 or \
                            self.grille.get_grille()[i + self.y][j + self.x] != ".":
                        collide = True
        return collide
    
    def go_side(self, dx):
        """Put the tetromino to the left or right
            if it doesn't collide on the way"""
        old_x = self.x
        self.x += dx
        if self.collide():
            self.x = old_x
    
    def rotate_tetromino(self):
        """Rotate the tetromino but if it collide,
            go back to the previous orientation"""
        old_rotation = self.rotation
        self.rotate()
        if self.collide():
            self.rotation = old_rotation
            
    def go_down(self):
        """Make the tetromino go down if it doesn't collide"""
        self.y += 1
        if self.collide():
            self.y -= 1
            return True
        return False