# code by : Adam V
import pygame

class Affichage:
    '''
    the class Affichage manage all the display of the game
    '''
    def __init__(self):
        # grille info
        self.pos_grille = (325, 75)
        self.taille_case = 25
        #color
        self.blanc = (255, 255, 255)
        self.red = (255, 0, 0)
        # next piece info
        self.pos_next_piece = (675, 75)
        self.taille_case_next_piece = 100
        # score info
        self.pos_score = (625, 450)
        pygame.font.init()
        self.font_score = pygame.font.SysFont("Comic Sans MS", 20)
        # ligne level info
        self.pos_line_level = (625, 300)
        self.font_line_level = pygame.font.SysFont("Comic Sans MS", 15)
        # touche info
        self.pos_touche = (25, 250)
        self.init_touche_img()
        # pause info
        self.pos_pause = (325, 250)
        self.font_pause = pygame.font.SysFont("Comic Sans MS", 50)


    def afficher_screen(self, screen, grille, score, ligne, level) -> None:
        self.afficher_grille(screen, grille)
        self.afficher_zone_next_piece(screen)
        self.afficher_score(screen, score)
        self.afficher_touche(screen)
        self.afficher_ligne_level(screen, score.get_ligne(), score.get_level())
        


    def afficher_grille(self, screen, grille) -> None:
        '''
        Display the grid, the case and the tetromino on the screen
        args:
            screen: pygame screen
            grille: Grille
        '''

        # lignes colonnes
        for ligne in range(grille.L + 1):
            pygame.draw.line(screen, self.blanc, (self.pos_grille[0], self.pos_grille[1]+ligne*self.taille_case), (self.pos_grille[0]+grille.C*self.taille_case, self.pos_grille[1]+ligne*self.taille_case))
        for colonne in range(grille.C + 1):
            pygame.draw.line(screen, self.blanc, (self.pos_grille[0]+colonne*self.taille_case, self.pos_grille[1]), (self.pos_grille[0]+colonne*self.taille_case, self.pos_grille[1]+grille.L*self.taille_case))

        # afficher les cases
        for ligne in range(grille.L):
            for colonne in range(grille.C):
                if grille.get_grille()[ligne][colonne] != ".":
                    pygame.draw.rect(screen, grille.get_grille()[ligne][colonne].color , (self.pos_grille[0]+colonne*self.taille_case+1, self.pos_grille[1]+ligne*self.taille_case+1, self.taille_case-1, self.taille_case-1))

    def afficher_zone_next_piece(self, screen) -> None:
        '''
        Display the next piece zone
        args:
            screen: pygame screen
        '''
        pygame.draw.rect(screen, self.blanc, (self.pos_next_piece[0], self.pos_next_piece[1], self.taille_case_next_piece, self.taille_case_next_piece), 1)

    def afficher_score(self, screen, score) -> None:
        '''
        Display the score and the high score
        args:
            screen: pygame screen
            score: Score
        '''
        text_score = self.font_score.render(f"Score : {score.get_score()}", True, self.blanc)
        text_high_score = self.font_score.render(f"High Score : {score.get_hight_score()}", True, self.blanc)
        screen.blit(text_score, (self.pos_score[0]+25, self.pos_score[1]+15))
        screen.blit(text_high_score, (self.pos_score[0]+5, self.pos_score[1]+65))

    def init_touche_img(self) -> None:
        # load image
        self.key_enter = pygame.image.load("assets/img/key_enter.png")
        self.key_left = pygame.image.load("assets/img/key_left.png")
        self.key_right = pygame.image.load("assets/img/key_right.png")
        self.key_space = pygame.image.load("assets/img/key_space.png")

        # resize image
        self.key_enter = pygame.transform.scale(self.key_enter, (50, 50))
        self.key_left = pygame.transform.scale(self.key_left, (50, 50))
        self.key_right = pygame.transform.scale(self.key_right, (50, 50))
        self.key_space = pygame.transform.scale(self.key_space, (50, 50))

        # add text expicative
        self.text_enter = self.font_score.render(f"Start/Pause", True, self.blanc)
        self.text_left = self.font_score.render(f"Left", True, self.blanc)
        self.text_right = self.font_score.render(f"Right", True, self.blanc)
        self.text_space = self.font_score.render(f"Rotate", True, self.blanc)
        
        

    def afficher_touche(self, screen) -> None:
        '''
        Display the key to play
        args:
            screen: pygame screen
        '''

        # blit image
        screen.blit(self.key_enter, (self.pos_touche[0], self.pos_touche[1]))
        screen.blit(self.key_left, (self.pos_touche[0], self.pos_touche[1]+75))
        screen.blit(self.key_right, (self.pos_touche[0], self.pos_touche[1]+150))
        screen.blit(self.key_space, (self.pos_touche[0], self.pos_touche[1]+225))

        # blit text
        screen.blit(self.text_enter, (self.pos_touche[0]+75, self.pos_touche[1]))
        screen.blit(self.text_left, (self.pos_touche[0]+75, self.pos_touche[1]+85))
        screen.blit(self.text_right, (self.pos_touche[0]+75, self.pos_touche[1]+160))
        screen.blit(self.text_space, (self.pos_touche[0]+75, self.pos_touche[1]+235))


    def afficher_ligne_level(self, screen, ligne, level) -> None:
        '''
        Display the number of line and the level
        args:
            screen: pygame screen
            ligne: int
            level: int
        '''

        # draw tableaux
        pygame.draw.rect(screen, self.blanc, (self.pos_line_level[0], self.pos_line_level[1], 200, 100), 1)
        pygame.draw.line(screen, self.blanc, (self.pos_line_level[0]+100, self.pos_line_level[1]), (self.pos_line_level[0]+100, self.pos_line_level[1]+100))
        pygame.draw.line(screen, self.blanc, (self.pos_line_level[0], self.pos_line_level[1]+50), (self.pos_line_level[0]+200, self.pos_line_level[1]+50))
        
        # draw the text
        text_line = self.font_line_level.render(f"Lines", True, self.blanc)
        screen.blit(text_line, (self.pos_line_level[0]+25, self.pos_line_level[1] + 10))
        text_level = self.font_line_level.render(f"Level", True, self.blanc)
        screen.blit(text_level, (self.pos_line_level[0]+125, self.pos_line_level[1] + 10))

        # draw the number
        text_line_number = self.font_line_level.render(f"{ligne}", True, self.blanc)
        screen.blit(text_line_number, (self.pos_line_level[0]+35, self.pos_line_level[1] + 60))
        text_level_number = self.font_line_level.render(f"{level}", True, self.blanc)
        screen.blit(text_level_number, (self.pos_line_level[0]+135, self.pos_line_level[1] + 60))

    def afficher_pause(self, screen) -> None:
        '''
        Display the pause
        args:
            screen: pygame screen
        '''

        text_pause = self.font_pause.render(f"Pause", True, self.blanc)
        screen.blit(text_pause, (self.pos_pause[0]+75, self.pos_pause[1]+25))

    def afficher_game_over(self, screen) -> None:
        '''
        Display the game over
        args:
            screen: pygame screen
        '''
        
        text_game_over = self.font_pause.render(f"Game Over", True, self.red)
        screen.blit(text_game_over, (self.pos_pause[0]+25, self.pos_pause[1]+25))

        