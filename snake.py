from turtle import Turtle


from constants import *


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.star_game()
        self.head = self.segments[0]

    def star_game(self):
        for c in range(SNAKE_INITIAL_SIZE):
            self.create_snake((0, 0))

    def reset(self) -> None:
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.star_game()
        self.head = self.segments[0]

    def create_snake(self, position):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.speed(1)
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.create_snake(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
