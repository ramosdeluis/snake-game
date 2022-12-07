from turtle import Turtle


from constants import *


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.setposition(x=0, y=260)
        self.high_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.get_high_score()
        self.make_high_score()
        self.refresh_board()

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            self.make_high_score()
        self.score = 0
        self.refresh_board()

    def make_point(self):
        self.score += 1
        self.refresh_board()

    def refresh_board(self):
        self.clear()
        self.write(arg=f'Score: {self.score} / High Score: {self.high_score}',
                   move=False, align='center', font=('Arial', SCORE_FONT_SIZE, 'normal'))

    def get_high_score(self):
        with open('high_score.txt', mode='r') as file:
            self.high_score = int(file.read()[-1])
            print(self.high_score)

    def make_high_score(self):
        with open('high_score.txt', mode='w') as file:
            file.write(f'high_score={self.high_score}')