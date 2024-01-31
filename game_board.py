# Impoerting necessary module
from snake import Snake
from food import Food
from score_board import ScoreBoard
from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Snake Game")
screen.bgcolor("black")

# to listen events

screen.listen()

snake = Snake()

score_board = ScoreBoard()

food = Food()
is_game_on = True
screen.onkey(fun=snake.turn_up, key='Up')
screen.onkey(fun=snake.turn_right, key='Right')
screen.onkey(fun=snake.turn_down, key='Down')
screen.onkey(fun=snake.turn_left, key='Left')
while is_game_on:
    snake.moveSnake()
    screen.update()
    time.sleep(0.14)

    # Detect food eating
    if snake.head.distance(food) <= 15:
        snake.extend()
        food.refresh()
        score_board.increase_score()

    # Detect snake reach to the wall

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        is_game_on = False
        score_board.game_over()

# Detect collision between snake body

    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 15:
            is_game_on = False
            score_board.game_over()


screen.exitonclick()
