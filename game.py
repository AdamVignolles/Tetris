import pygame
from grille import Grille
from affichage import Affichage

class Game:
    def __init__(self):
        self.grille = Grille()
        self.affichage = Affichage()

        self.screen = pygame.display.set_mode((850, 600))
        self.clock = pygame.time.Clock()

        self.in_menu = False

        self.cont_ligne = 0
        self.level = 1

    def run(self):

        pygame.display.set_caption("Tetris")
        icon = pygame.image.load("assets/img/tetris.png")
        pygame.display.set_icon(icon)

        

        running = True
        while running:

            self.clock.tick(60)
            pygame.display.flip()

            if self.in_menu:
                pass
            else:
                self.affichage.afficher_grille(self.screen, self.grille)
                self.affichage.afficher_zone_next_piece(self.screen)
                self.affichage.afficher_score(self.screen, 0)
                self.affichage.afficher_touche(self.screen)
                self.affichage.afficher_line_level(self.screen, self.cont_ligne, self.level)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()