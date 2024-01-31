from turtle import Turtle


class Food(Turtle):
    """
    Food class to create food for snake and it is plased randomly"""

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
