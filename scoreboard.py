from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.setposition(x=0, y=260)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.refresh_board()

    def make_point(self):
        self.score += 1
        self.refresh_board()

    def refresh_board(self):
        self.write(arg=f'Score: {self.score}', move=False, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write(arg=f'  End game...\n'
                       f'Your score: {self.score}', move=False, align='center', font=('Arial', 30, 'normal'))
