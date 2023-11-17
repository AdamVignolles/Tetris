import pygame as pg
#Joshua LERAS IRIARTE, v1
#vectors can be changed to manual if needed 
TILE_SIZE = 50  #Size of a tile in pixels
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20 # tuple of the Weigth and Height of the screen
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE #The grid
MIDDLE = FIELD_SIZE[0] // 2
#COORDS of each tetrominoes
TETROMINOES = {
    'T' : [[0,0], [-1,0], [1,0], [0,-1]],
    'O' : [[0,0], [0,-1], [1,0], [1,-1]],
    'J' : [[0,0], [1,0], [0,-1], [0,-2]],
    'L' : [[0,0], [1,0], [0,-1], [0,-2]],
    'I' : [[0,0], [0,1], [0,-1], [0,-2]],
    'S' : [[0,0], [-1,0], [0,-1], [1,-1]],
    'Z' : [[0,0], [1,0], [0,-1], [-1,-1]]
    }
#Possible moves of the tetrominoes
MOVES = {'left' : -1,
         'right' : 1,
         'down' : 1,
         'up' : -1} #up might be useless

class Block():
    def __init__(self,tetromino, pos):
        self.tetromino = tetromino #call an object Tetromino
        self.pos = pos #pos in the main list
        
        self.image = pg.Surface([TILE_SIZE, pos[1] * TILE_SIZE])
        self.image = fill('green') #Display of the block
        
        self.rect = self.image.get_rect()
    
    def set_pos(self):
        """Calculating the new position of the image of the block"""
        self.rect.topleft = pos * TILE_SIZE
        
    def update(self):
        """Update the position of the display of the block"""
        return self.set_pos()
    
    def rotate(self):
        """Rotate the block according to the whole tetromino"""
        pass #Work in Progress, it's  a pain
    
    def forward(self):
        """Move the block bellow"""
        self.pos[1] += 1 
        
    def left(self):
        """Move the blok on the left"""
        self.pos[0] -= 1 
        
    def right(self):
        """Move the block on the right"""
        self.pos[1] += 1 
    
class Tetromino():
    def __init__(self, grille, shape):
        self.grille = Grille #call an object Tetris
        self.shape = shape #the shape from the TETROMINOES dict
        self.block = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        #list of all the blocks coords of the tetromino
        
    def put_middle(self):
        for block in self.block:
            if block[0] < 0 :
                for block in self.block:
                    block[0] += 1
            if block[1] < 0 :
                block[1] += 1
        for block in self.block:
            block[0] += MIDDLE
            
    def move_tetromino(self,direction):
        """Move the tetrominoes in one given direction"""
        move_piece = MOVES[direction] #Move in one given direction from MOVES
        if direction == 'down':
            if collision_down == True :
                for block in self.block: #Apply the movement to all tetrimino blocks
                    block.pos = move_piece #modify the index of the block
        if direction == 'left':
            if collision_left == True :
                for block in self.block: #Apply the movement to all tetrimino blocks
                    block.pos = move_piece
        if direction == 'right':
            if collision_down == True :
                for block in self.block: #Apply the movement to all tetrimino blocks
                    block.pos = move_piece
                
    def collide_down(self):
        """Verifie les collisions avec l'index en dessous de la liste grille de Grille"""
        for block in self.block:
            if block[1] + 1 >= len(Grille.grille) \
                or Grille.grille[block[1]] != None:
                return False
            
    def collide_right(self):
        """Verify the collision on the right"""
        for block in self.block:
            if block[0] + 1 >= len(Grille.grille[0]) \
               or Grille.grille[block[0]+1] != None:
                return False
            
    def collide_left(self):
        """Verify the collision on the left"""
        for block in self.block:
            if block[0] - 1 < len(Grille.grille[0]) \
               or Grille.grille[block[0]-1] != None:
                return False
            
    def update(self):
        """Update the tetromino going down"""
        if game_on == True : #Might be changed if wrong variabl
            self.move(direction = 'down')
            pg.time.wait(200) #Regulate the speed of the movement
            pg.time.wait(200) #Regulate the speed of the movement
