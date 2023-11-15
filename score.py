import json

class Score:
    def __init__(self):
        self.score = 0
        self.hight_score = 0
        self.level = 1
        self.line = 0
        self.load_score()

    def load_score(self):
        with open("assets/score.json", "r") as f:
            data = json.load(f)
            self.hight_score = data["hight_score"]

    def save_score(self):
        with open("assets/score.json", "w") as f:
            data = {}
            data["hight_score"] = self.hight_score
            json.dump(data, f)

    def add_score(self, score):
        self.score += score
        if self.score > self.hight_score:
            self.hight_score = self.score

    def add_line(self, line):
        self.line += line
        if self.line % 10 == 0:
            self.level += 1

    def reset(self):
        self.score = 0
        self.level = 1
        self.line = 0

    def get_score(self):
        return self.score

    def get_hight_score(self):
        return self.hight_score

    def get_level(self):
        return self.level

    def get_line(self):
        return self.line
