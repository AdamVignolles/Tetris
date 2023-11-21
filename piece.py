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
COLOR = {'T':'insert color here'}
class Block():
    def __init__(self,tetromino, color, pos):
        self.tetromino = tetromino #call an object Tetromino
        self.pos = pos #pos in the main list
        
        self.image = pg.Surface([TILE_SIZE, pos[1] * TILE_SIZE])
        self.image = pg.fill(color) #Display of the block
        
        self.rect = self.image.get_rect()
    
    def set_pos(self):
        """Calculating the new position of the image of the block"""
        self.rect.topleft = self.pos[0] * TILE_SIZE, self.pos[1] * TILE_SIZE
        
        
    def update(self):
        """Update the position of the display of the block"""
        return self.set_pos()
    
    def rotate(self):
        """Rotate the block according to the whole tetromino"""
        pass #Work in Progress, it's  a pain, help
    
class Tetromino():
    def __init__(self, grille, shape):
        self.grille = grille #call an object Tetris
        self.shape = shape #the shape from the TETROMINOES dict
        self.color = COLOR[shape] #get the color of the tetrominoes
        self.block = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        #list of all the blocks coords of the tetromino
        
    def put_middle(self):
        """Put the tetromino in the middle of the screen"""
        for block in self.block:
            if block.pos[0] < 0 :
                for block in self.block:
                    block.pos[0] += 1
            if block.pos[1] < 0 :
                block.pos[1] += 1
        for block in self.block:
            block.pos[0] += MIDDLE
            
    def move_tetromino(self,direction):
        """Move the tetrominoes in one given direction"""
        move_piece = MOVES[direction] #Move in one given direction from MOVES
        if direction == 'left':
            if self.collide_left() == True :
                for block in self.block: #Apply the movement to all tetrimino blocks
                    block.pos[0] = move_piece #go left
        if direction == 'right':
            if self.collide_down() == True :
                for block in self.block: #Apply the movement to all tetrimino blocks
                    block.pos[0] = move_piece #go right
                
    def check_lost(self):
        """check if a block is above the screen"""
        for pos in self.block:
            x, y = pos.pos
            return y < 0
        
    def valid_spaces(self, grille):
        """check spaces without blocks"""
        accepted_pos = [[[x, y] for x in range(len(grille.grille[0])-1) if grille.grille[y][x] == 0] for y in range(len(grille.grille)-1)]
        accepted_pos = [j for sub in test for j in sub]
        return accepted_pos
         
    def update(self):
        """Update the tetromino going down"""
        if game_on == True :
            if self.collide_down() == False :
                self.move_tetromino(direction = 'down') #the tetromino always goes down
                pg.time.wait(200) #Regulate the speed of the movement
