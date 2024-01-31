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

score_b = ScoreBoard()

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
    if snake.head.distance(food) <= 10:
        food.refresh()
        score_b.update_score()


snake.screen.exitonclick()
