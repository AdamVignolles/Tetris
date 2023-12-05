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
        self.menu = Menu()
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

    def run(self) -> None:
        '''
        Main loop of the game
        Manage the game state and the inputs, and call the different functions for displaying the game
        '''

        pygame.init()

        pygame.display.set_caption("Tetris")
        icon = pygame.image.load("assets/img/tetris.png")
        pygame.display.set_icon(icon)

        random_x =  random.randint(0, 6)

        self.Tetro = Tetromino(random_x, 0, self.grille)
        self.next_Tetro = Tetromino(random_x, 0, self.grille)

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
                self.affichage.afficher_grille(self.screen, self.grille)
                self.affichage.afficher_zone_next_piece(self.screen)
                self.affichage.afficher_score(self.screen, self.score)
                self.affichage.afficher_touche(self.screen)
                self.affichage.afficher_ligne_level(self.screen, self.score.get_ligne(), self.score.get_level())
                
                # do the loop only if the game is not over 
                if not self.game_over:

                    # afficher le tetromino
                    shape = self.Tetro.image()
                    matrice = [[0 for _ in range(4)] for _ in range(4)]
                    for i in shape:
                        matrice[i // 4][i % 4] = 1
                    for i in range(len(matrice)):
                        for j in range(len(matrice[i])):
                            if matrice[i][j] == 1:
                                x = j * self.affichage.taille_case + self.affichage.pos_grille[0] + self.Tetro.x * self.affichage.taille_case
                                y = i * self.affichage.taille_case + self.affichage.pos_grille[1] + self.Tetro.y * self.affichage.taille_case
                                pygame.draw.rect(self.screen, self.Tetro.color, (x, y, self.affichage.taille_case, self.affichage.taille_case))

                    # afficher la prochaine piece
                    shape = self.next_Tetro.image()
                    matrice = [[0 for _ in range(4)] for _ in range(4)]
                    for i in shape:
                        matrice[i // 4][i % 4] = 1
                    for i in range(len(matrice)):
                        for j in range(len(matrice[i])):
                            if matrice[i][j] == 1:
                                x = self.affichage.pos_next_piece[0] + j * self.affichage.taille_case
                                y = self.affichage.pos_next_piece[1] + i * self.affichage.taille_case
                                pygame.draw.rect(self.screen, self.next_Tetro.color, (x, y, self.affichage.taille_case, self.affichage.taille_case))

                    # check if the tetromino is colliding with the bottom of the grid , else go down, but not if the game is paused
                    colide_down = False
                    if self.in_pause:
                        self.affichage.afficher_pause(self.screen)
                    else:
                        if self.count_tour_boucle < self.max_tour_boucle:
                            self.count_tour_boucle += 1
                        else:
                            colide_down = self.Tetro.go_down() 
                            self.count_tour_boucle = 0
                            self.max_tour_boucle = self.level_speed[self.score.get_level()]

                    # check the collision of the tetromino with the bottom of the grid or another tetromino
                    if (self.Tetro is not None and self.Tetro.collide()) or (self.Tetro is not None and colide_down == True):
                        self.grille.ajouter_piece(self.Tetro)
                        random_x =  random.randint(0, 6)
                        del self.Tetro
                        self.Tetro = self.next_Tetro
                        self.next_Tetro = Tetromino(random_x, 0, self.grille)  

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
                        self.game_over = True
                        self.Tetro = None
                        self.next_Tetro = None
                        self.affichage.afficher_game_over(self.screen)
                else:
                    self.affichage.afficher_game_over(self.screen)

            # pygame event loop for detecting inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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