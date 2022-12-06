from turtle import Screen
from time import sleep


from scoreboard import ScoreBoard
from constants import *
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = 0
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.move_down, key='s')
screen.onkey(fun=snake.move_up, key='w')
screen.onkey(fun=snake.move_left, key='a')
screen.onkey(fun=snake.move_right, key='d')

game_is_on = True

while game_is_on:
    screen.update()
    sleep(GAME_SPEED)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.make_point()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        screen.update()

    # Detect collision with the tail.
    for seg in snake.segments[1:]:
        if seg.distance(snake.head) < 10:
            scoreboard.reset()
            snake.reset()
            screen.update()

screen.exitonclick()
