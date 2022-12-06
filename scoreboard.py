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
        self.refresh_board()

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh_board()

    def make_point(self):
        self.score += 1
        self.refresh_board()

    def refresh_board(self):
        self.clear()
        self.write(arg=f'Score: {self.score} / High Score: {self.high_score}',
                   move=False, align='center', font=('Arial', SCORE_FONT_SIZE, 'normal'))
