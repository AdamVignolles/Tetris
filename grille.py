class Grille:
    def __init__(self):
        self.L = 20
        self.C = 10
        self.grille = [["." for _ in range(self.C)] for _ in range(self.L)]

    def __str__(self) -> str: return "\n".join([" ".join(ligne) for ligne in self.grille])
    def __repr__(self) -> str: return self.__str__()

    def get_grille(self) -> list: return self.grille

    def est_vide(self, ligne:int, colonne:int) -> bool: return self.grille[ligne][colonne] == "."
    
    def est_remplie(self, ligne:int) -> bool:
        for colonne in range(self.C):
            if self.est_vide(ligne, colonne): return False
        return True
    
    def supprimer_ligne(self, ligne:int):
        for i in range(ligne, 0, -1):
            self.grille[i] = self.grille[i-1]
        self.grille[0] = ["." for _ in range(self.C)]
        self.tomber_ligne()

    def supprimer_lignes(self) -> int:
        count_lignes = 0
        for ligne in range(self.L):
            if self.est_remplie(ligne): 
                self.supprimer_ligne(ligne)
                count_lignes += 1
        return count_lignes
    
    def ajouter_piece(self, piece, ligne, colonne):
        pass

    def tomber_ligne(self):
        for colonne in range(self.C):
            for ligne in range(self.L-1, 0, -1):
                if self.est_vide(ligne, colonne):
                    self.grille[ligne][colonne] = self.grille[ligne-1][colonne]
                    self.grille[ligne-1][colonne] = "."


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
    grille.tomber_ligne()
    print(grille)
    print(grille.supprimer_lignes())
    print(grille)