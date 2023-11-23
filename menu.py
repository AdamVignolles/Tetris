import pygame as pg
class Button():
    def __init__(self, image, pos, text_input, font, base_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None :
            self.image = self.text
        self.image_rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.image_rect)
        else:
            screen.blit(self.text, self.text_rect)
    
    def press_button(self, position):
        print(position, range(self.image_rect.left, self.image_rect.right), range(self.image_rect.top, self.image_rect.bottom))
        if position[0] in range(self.image_rect.left, self.image_rect.right) and \
           position[1] in range(self.image_rect.top, self.image_rect.bottom):
            return True
        return False
    
class Menu():
    def __init__(self):
        #self.background = pg.image.load("assets/Background.png")
        pg.init()

        self.mouse_pos = pg.mouse.get_pos()
        
        self.menu_text = pg.font.SysFont("Comic Sans MS", 100).render("Tetris", True, 'white')
        self.menu_rect = self.menu_text.get_rect(center=(425, 100))
        
        self.play_button = Button(image=pg.image.load('assets/play_button.png'), \
                                  pos=(425,300), text_input="PLAY",\
                                  font=pg.font.SysFont("Comic Sans MS", 20), base_color='white')
    def check_button_input(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_pos = pg.mouse.get_pos()
                return self.play_button.press_button(self.mouse_pos)
            if event.type == pg.QUIT:
                pg.quit()
                
    def get_font(self, size):
        pg.font.Font(pg.font.get_default_font(), size)
        
    def update_menu(self, screen):
        #screen.blit(self.background, (0,0))
        screen.blit(self.menu_text, self.menu_rect)
