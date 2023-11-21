import pygame
from grille import Grille
from affichage import Affichage
from score import Score
from piece import Tetromino

class Game:
    def __init__(self):
        self.grille = Grille()
        self.affichage = Affichage()
        self.score = Score()

        self.screen = pygame.display.set_mode((850, 600))
        self.clock = pygame.time.Clock()

        self.in_menu = False
        self.in_pause = False


    def run(self):

        pygame.display.set_caption("Tetris")
        icon = pygame.image.load("assets/img/tetris.png")
        pygame.display.set_icon(icon)

        self.Tetro = Tetromino(self.grille, 'J')

        running = True
        while running:

            self.clock.tick(60)
            pygame.display.flip()
            self.screen.fill((0, 0, 0))

            if self.in_menu:
                pass
            else:
                self.affichage.afficher_grille(self.screen, self.grille)
                self.affichage.afficher_zone_next_piece(self.screen)
                self.affichage.afficher_score(self.screen, self.score)
                self.affichage.afficher_touche(self.screen)
                self.affichage.afficher_line_level(self.screen, self.score.get_line(), self.score.get_level())
                if self.in_pause:
                    self.affichage.afficher_pause(self.screen)
                
                for block in self.Tetro.block:
                    self.screen.blit(block.image, block.rect)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_RETURN:
                        # afficher pause
                        self.in_pause = not self.in_pause

                    if event.key == pygame.K_LEFT:
                        self.Tetro.move_tetromino('left')

                    if event.key == pygame.K_RIGHT:
                        self.Tetro.move_tetromino('right')

                    if event.key == pygame.K_SPACE:
                        pass


        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()