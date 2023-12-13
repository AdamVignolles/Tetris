# code by : Adam V 
import pygame
from grille import Grille
from affichage import Affichage
from score import Score

from menu import Menu
from tetromino import Tetromino
import random


class Game:
    '''
    the class game is the main class of the game, it manage all the game 
    '''
    def __init__(self):
        self.menu = Menu("Tetris")
        self.button = self.menu.play_button

        self.grille = Grille()
        self.affichage = Affichage()
        self.score = Score()

        self.screen = pygame.display.set_mode((850, 600))
        self.clock = pygame.time.Clock()

        self.in_menu = True
        self.in_pause = False
        self.game_over = False

        self.level_speed = {
            1: 30,
            2: 20,
            3: 15,
            4: 10,
            5: 5
        }

        self.count_tour_boucle = 0
        self.max_tour_boucle = self.level_speed[self.score.get_level()]

    def is_lost(self) -> None:
        self.game_over = True
        self.Tetro = None
        self.next_Tetro = None
        self.score.quit()

    def init_run(self) -> None:
        pygame.init()

        pygame.display.set_caption("Tetris")
        icon = pygame.image.load("assets/img/tetris.png")
        pygame.display.set_icon(icon)

        random_x =  random.randint(0, 6)

        self.Tetro = Tetromino(random_x, 0, self.grille)
        self.next_Tetro = Tetromino(random_x, 0, self.grille)

    def is_collide(self) -> None:
        self.grille.ajouter_piece(self.Tetro)
        random_x =  random.randint(0, 6)
        self.Tetro = self.next_Tetro
        self.next_Tetro = Tetromino(random_x, 0, self.grille)  
  

    def run(self) -> None:
        '''
        Main loop of the game
        Manage the game state and the inputs, and call the different functions for displaying the game
        '''

        self.init_run()

        # main loop
        running = True
        
        while running:

            self.clock.tick(60)
            pygame.display.flip()
            self.screen.fill((0, 0, 0))

            # check if the game is in the menu or not for displaying the menu and get the button input
            if self.in_menu:
                self.menu.update_menu(self.screen)
                self.button.update(self.screen)
                if self.menu.check_button_input():
                    self.in_menu = False

            else:
                # afficher la grille
                self.affichage.afficher_screen(self.screen, self.grille, self.score, self.score.get_ligne(), self.score.get_level())
                
                # do the loop only if the game is not over 
                if self.game_over:
                    self.affichage.afficher_game_over(self.screen)

                else:

                    # afficher le tetromino
                    self.Tetro.display_tetromino(self.screen, self.affichage, True)
                    self.next_Tetro.display_tetromino(self.screen, self.affichage, False)

                    # check if the tetromino is colliding with the bottom of the grid , else go down, but not if the game is paused
                    
                    if self.in_pause:
                        self.affichage.afficher_pause(self.screen)

                    else:
                        colide_down = False
                        if self.count_tour_boucle < self.max_tour_boucle:
                            self.count_tour_boucle += 1
                        else:
                            colide_down = self.Tetro.go_down() 
                            self.count_tour_boucle = 0
                            self.max_tour_boucle = self.level_speed[self.score.get_level()]

                            # check the collision of the tetromino with the bottom of the grid or another tetromino
                            if (self.Tetro is not None and self.Tetro.collide()) or (self.Tetro is not None and colide_down == True):
                                self.is_collide()

                    # check completed lines and delete them 
                    count_lignes = 0
                    for ligne in range(self.grille.L - 1, 0, -1):
                        if self.grille.est_remplie(ligne):
                            count_lignes += 1
                            self.grille.supprimer_ligne(ligne)
                    
                    # add new lines to the grid caused by the completed lines
                    for i in range(count_lignes):
                        self.grille.ajouter_ligne()

                    # update the score 
                    self.score.add_ligne(count_lignes)
                    self.score.add_score(self.score.score_by_nb_ligne[count_lignes])

                    #check if the game is lost 
                    if self.grille.check_lost():
                        self.is_lost()

            # pygame event loop for detecting inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.score.quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        if self.game_over:
                            self.in_menu = True
                        running = False

                    if event.key == pygame.K_RETURN:
                        # afficher pause
                        self.in_pause = not self.in_pause

                    if event.key == pygame.K_LEFT:
                        if self.Tetro is not None and not self.in_pause:
                           self.Tetro.go_side(-1)

                    if event.key == pygame.K_RIGHT:
                        if self.Tetro is not None and not self.in_pause:
                            self.Tetro.go_side(1)

                    if event.key == pygame.K_DOWN:
                        if self.Tetro is not None and not self.in_pause:
                            self.Tetro.go_down()

                    if event.key == pygame.K_SPACE:
                        if self.Tetro is not None and not self.in_pause:
                            self.Tetro.rotate_tetromino()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
