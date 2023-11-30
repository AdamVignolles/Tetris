# code by : Adam V

class Grille:
    """Classe qui gère la grille de jeu"""
    def __init__(self):
        self.L = 20
        self.C = 10
        self.grille = [["." for _ in range(self.C)] for _ in range(self.L)]

    def __str__(self) -> str: return "\n".join([" ".join(ligne) for ligne in self.grille])
    def __repr__(self) -> str: return self.__str__()

    def get_grille(self) -> list: 
        '''
        get the grid
        '''
        return self.grille

    def est_vide(self, ligne:int, colonne:int) -> bool: 
        '''
        return True if the case is empty
        '''
        return self.grille[ligne][colonne] == "."
    
    def est_remplie(self, ligne:int) -> bool:
        '''
        return True if the line is full
        '''
        for colonne in range(self.C):
            if self.est_vide(ligne, colonne): return False
        return True
    
    def supprimer_ligne(self, ligne:int) -> None:
        '''
        delete a line
        args:
            ligne: int, the line to delete
        '''
        del self.grille[ligne]
        

    def supprimer_lignes(self) -> int:
        '''
        delete all the full lines
        return the number of lines deleted
        '''
        count_lignes = 0
        for ligne in range(self.L):
            if self.est_remplie(ligne): 
                self.supprimer_ligne(ligne)
                count_lignes += 1
        return count_lignes
    
    def ajouter_piece(self, piece) -> None:
        """ajouter un tetromino dans la grille"""
        x = piece.x
        y = piece.y 
        shape = piece.image()
        for i in shape:
            self.grille[i // 4 + y][i % 4 + x] = piece
            

    def ajouter_ligne(self) -> None:
        """ajouter une ligne en haut de la grille"""
        self.grille.insert(0, ["." for _ in range(self.C)])

    def check_lost(self) -> bool:
        """check if a block is above the screen"""
        for colonne in range(self.C):
            if self.grille[0][colonne] != ".":
                return True
        return False
        
                
        


        


if __name__ == "__main__":
    grille = Grille()
    grille.get_grille()[0][0] = "X"
    grille.get_grille()[0][1] = "X"
    grille.get_grille()[0][2] = "X"
    grille.get_grille()[0][3] = "X"
    grille.get_grille()[0][4] = "X"
    grille.get_grille()[0][5] = "X"
    grille.get_grille()[0][6] = "X"
    grille.get_grille()[0][7] = "X"
    grille.get_grille()[0][8] = "X"
    grille.get_grille()[0][9] = "X"
    print(grille)
    print(grille.supprimer_lignes())
    print(grille)