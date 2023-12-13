# code by : Adam V
import json

class Score:
    '''
    the class Score manage the score, the level and the number of lines
    '''
    def __init__(self):
        self.score = 0
        self.hight_score = 0
        self.level = 1
        self.ligne = 0
        self.load_score() # load the hight score

        self.score_by_nb_ligne = {
            0: 0,
            1: 40,
            2: 100,
            3: 300,
            4: 1200
        }

    def load_score(self) -> None:
        '''
        load the hight score from the json file
        '''
        with open("assets/score.json", "r") as f:
            data = json.load(f)
            self.hight_score = data["hight_score"]

    def save_score(self):
        '''
        save the hight score in the json file
        '''
        with open("assets/score.json", "w") as f:
            data = {}
            data["hight_score"] = self.hight_score
            json.dump(data, f)

    def quit(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            self.save_score()

    def add_score(self, score) -> None:
        '''
        add score to the score
        args:
            score: int
        '''
        self.score += score

    def add_ligne(self, ligne) -> None:
        '''
        add the number of lines to the score
        args:
            ligne: int
        '''
        if ligne != 0:
            self.ligne += ligne
            if self.ligne % 5 == 0:
                self.level += 1

    def reset(self):
        self.score = 0
        self.level = 1
        self.ligne = 0

    def get_score(self):
        return self.score

    def get_hight_score(self):
        return self.hight_score

    def get_level(self):
        return self.level

    def get_ligne(self):
        return self.ligne
