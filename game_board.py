# Impoerting necessary module
from snake import Snake
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Snake Game")
screen.bgcolor("black")


snake = Snake()
is_game_on = True

while is_game_on:
    snake.moveSnake()
    screen.update()
    time.sleep(0.4)

snake.screen.exitonclick()
