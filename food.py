from turtle import Turtle
import random

class Food(Turtle):
    """
    Food class to create food for snake and it is plased randomly"""

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
