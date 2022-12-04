from turtle import Screen
from time import sleep


from scoreboard import ScoreBoard
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
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
    sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.clear()
        scoreboard.make_point()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.clear()
        scoreboard.game_over()
        screen.update()
        game_is_on = False

    # Detect collision with the tail.
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif seg.distance(snake.head) < 10:
            scoreboard.clear()
            scoreboard.game_over()
            screen.update()
            game_is_on = False

screen.exitonclick()
