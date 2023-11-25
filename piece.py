import pygame as pg
#Joshua LERAS IRIARTE, v1
#vectors can be changed to manual if needed 
TILE_SIZE = 20  #Size of a tile in pixels
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20 # tuple of the Weigth and Height of the screen
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE #The grid
MIDDLE = FIELD_SIZE[0] // 2
#COORDS of each tetrominoes
TETROMINOES = {
    'T' : [[0,0], [-1,0], [1,0], [0,-1]],
    'O' : [[0,0], [0,-1], [1,0], [1,-1]],
    'J' : [[2,2], [3,2], [2,1], [2,0]],
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
COLOR = {'T': (255,0,0),
         'O': (0,255,0),
         'J': (0,0,255),
         'L': (255,255,0),
         'I': (0,255,255),
         'S': (255,0,255),
         'Z': (255,255,255)}
class Block():
    def __init__(self,tetromino, color, pos, pos_grille):
        self.tetromino = tetromino #call an object Tetromino
        self.pos = pos #pos in the main list
        self.color = color #color of the block
        self.pos_grille = pos_grille #pos of the grid
        
    def aficher_block(self, screen):
        """Display the block in the screen"""
        self.image = pg.draw.rect(screen, self.color, (self.pos_grille[0] + (self.pos[0] * TILE_SIZE), self.pos_grille[1] + (self.pos[1] * TILE_SIZE), TILE_SIZE, TILE_SIZE))
    
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
    def __init__(self, grille, shape, pos_grille):
        self.grille = grille #call an object Tetris
        self.shape = shape #the shape from the TETROMINOES dict
        self.color = COLOR[shape] #get the color of the tetrominoes
        self.block = [Block(self, self.color, pos, pos_grille) for pos in TETROMINOES[self.shape]]
        self.rotation = 0 #the rotation of the tetrominoes
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

    def rotate(self):
        """Rotate the tetromino"""
        # write the function to rotate the tetromino here
        

        
            
    def move_tetromino(self,direction):
        """Move the tetrominoes in one given direction"""
        move_piece = MOVES[direction] #Move in one given direction from MOVES
        if direction == 'down':
            if self.collide_down() == True :
                for block in self.block: #Apply the movement to all tetrimino blocks
                    block.pos[1] = move_piece #modify the index of the block
        if direction == 'left':
            if self.collide_left() == True :
                for block in self.block: #Apply the movement to all tetrimino blocks
                    block.pos[0] = move_piece #go left
        if direction == 'right':
            if self.collide_right() == True :
                for block in self.block: #Apply the movement to all tetrimino blocks
                    block.pos[0] = move_piece #go right

                
    def collide_down(self):
        """Verifie les collisions avec l'index en dessous de la liste grille de Grille"""
        pos_block = []
        for block in self.block:
            pos_block.append(block.pos)
            
        for i in range(len(pos_block)):
            if pos_block[i][1] + 1 >= len(self.grille.grille) \
                or self.grille.grille[pos_block[i][1]+1] != None:
                return True
        return False
            
    def collide_right(self):
        """Verify the collision on the right"""
        pos_block = []
        for block in self.block:
            pos_block.append(block.pos)
            
        for i in range(len(pos_block)):
            if pos_block[i][0] + 1 > len(self.grille.grille[0]) \
                or self.grille.grille[pos_block[i][0]+1] != None:
                return True
        return False
    
    def collide_left(self):
        """Verify the collision on the left"""
        pos_block = []
        for block in self.block:
            pos_block.append(block.pos)
            
        for i in range(len(pos_block)):
            if pos_block[i][0] - 1 < 0 \
                or self.grille.grille[pos_block[i][0]-1] != None:
                return True
        return False
    
    def check_lost(self):
        """check if a block is above the screen"""
        for pos in self.block:
            x, y = pos.pos
            return y < 0
        
    def valid_spaces(self, grille):
        """check spaces without blocks"""
        #return a list of list of list of the coordinate x, y of each valid spaces
        accepted_pos = [[[x, y] for x in range(len(grille[0])-1) if grille[y][x] == 0] for y in range(len(grille)-1)]
        accepted_pos = [j for sub in test for j in sub] #simplify to list of list
        return accepted_pos
    
    def update(self):
        """Update the tetromino going down"""
        if game_on == True :
            if self.collide_down() == False :
                self.move_tetromino(direction = 'down') #the tetromino always goes down
                for pos in self.block :
                    x, y = pos.pos
                    self.grille[y][x] = 1
                pg.time.wait(200) #Regulate the speed of the movement
