import pygame

class Affichage:
    def __init__(self):
        self.pos_grille = (350, 75)
        self.taille_case = 25
        self.blanc = (255, 255, 255)

        self.pos_next_piece = (675, 75)
        self.taille_case_next_piece = 100

        self.pos_score = (625, 450)
        pygame.font.init()
        self.font_score = pygame.font.SysFont("Comic Sans MS", 20)

        self.pos_line_level = (625, 300)
        self.font_line_level = pygame.font.SysFont("Comic Sans MS", 15)

    def afficher_grille(self, screen, grille):
        
        # lignes colonnes
        for ligne in range(grille.L + 1):
            pygame.draw.line(screen, self.blanc, (self.pos_grille[0], self.pos_grille[1]+ligne*self.taille_case), (self.pos_grille[0]+grille.C*self.taille_case, self.pos_grille[1]+ligne*self.taille_case))
        for colonne in range(grille.C + 1):
            pygame.draw.line(screen, self.blanc, (self.pos_grille[0]+colonne*self.taille_case, self.pos_grille[1]), (self.pos_grille[0]+colonne*self.taille_case, self.pos_grille[1]+grille.L*self.taille_case))

        # afficher les cases
        pass

    def afficher_zone_next_piece(self, screen):
        pygame.draw.rect(screen, self.blanc, (self.pos_next_piece[0], self.pos_next_piece[1], self.taille_case_next_piece, self.taille_case_next_piece), 1)

    def afficher_score(self, screen, score):
        text_score = self.font_score.render(f"Score : {0}", True, self.blanc)
        text_high_score = self.font_score.render(f"High Score : {0}", True, self.blanc)
        screen.blit(text_score, (self.pos_score[0]+25, self.pos_score[1]+15))
        screen.blit(text_high_score, (self.pos_score[0]+5, self.pos_score[1]+65))

    def afficher_touche(self, screen):
        pass

    def afficher_line_level(self, screen, line, level):
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
        text_line_number = self.font_line_level.render(f"{line}", True, self.blanc)
        screen.blit(text_line_number, (self.pos_line_level[0]+35, self.pos_line_level[1] + 60))
        text_level_number = self.font_line_level.render(f"{level}", True, self.blanc)
        screen.blit(text_level_number, (self.pos_line_level[0]+135, self.pos_line_level[1] + 60))



        