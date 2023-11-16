import pygame as pg
#Joshua LERAS IRIARTE, v1
#vectors can be changed to manual if needed 
vec = pg.math.Vector2 #math are cool. Especially vectors, very useful
FPS = 60 #frame per second
TILE_SIZE = 50  #Size of a tile in pixels
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20 # tuple of the Weigth and Height of the screen
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE #The grid
pos_vec =  vec(FIELD_SIZE) // 2 #SHOULD BE FIXED
                                # -> Put the tetromino in the middle

#COORDS of each tetrominoes
TETROMINOES = {
    'T' : [(0,0), (-1,0), (1,0), (0,-1)],
    'O' : [(0,0), (0,-1), (1,0), (1,-1)],
    'J' : [(0,0), (-1,0), (0,-1), (0,-2)],
    'L' : [(0,0), (1,0), (0,-1), (0,-2)],
    'I' : [(0,0), (0,1), (0,-1), (0,-2)],
    'S' : [(0,0), (-1,0), (0,-1), (1,-1)],
    'Z' : [(0,0), (1,0), (0,-1), (-1,-1)]
    }
#Possible moves of the tetrominoes
MOVES = {'left' : vec(-1,0),
         'right' : vec(1,0),
         'down' : vec(0,1),
         'up' : vec(0,-1)}

class Block():
    def __init__(self,tetromino, pos):
        self.tetromino = tetromino #call an object Tetromino
        self.pos = vec(pos) + pos_vec #calculating the pos
        
        self.image = pg.Surface([TILE_SIZE, pos[1] * TILE_SIZE])
        self.image = fill('green') #Display of the block
        
        self.rect = self.image.get_rect()
        
    def set_rect_pos(self):
        """Display the block at the position given"""
        self.rect.topleft = self.pos * TILE_SIZE
        
    def update(self):
        """Update the position of the block"""
        self.set_rect_pos()
        
    def rotate(self):
        """Rotate the block according to the whole tetromino"""
        pass #Work in Progress
    
    def collide(self):
        pass #Work in Progress
    
    def forward(self):
        """Move the block bellow"""
        self.pos[1] += 1 #might be useless
        
    def left(self):
        """Move the blok on the left"""
        self.pos[0] -= 1 #Also might be useless
        
    def right(self):
        """Move the block on the right"""
        self.pos[1] += 1 #useless ?
    
class Tetromino():
    def __init__(self, tetris, shape):
        self.tetris = Tetris #call an object Tetris
        self.shape = shape #the shape from the TETROMINOES dict
        self.block = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        #list of all the blocks coords of the tetromino
        
    def move_tetromino(self,direction):
        """Move the tetrominoes in one given direction"""
        move_piece = MOVES[direction] #Move in one given direction from MOVES
        for block in self.block: #Apply the movement to all tetrimino blocks
            block.pos = move_piece 
            
    def update(self):
        """Update the tetromino going down"""
        if game_on == True : #Might be changed if wrong variabl
            self.move(direction = 'down')
            pg.time.wait(200) #Regulate the speed of the movement
