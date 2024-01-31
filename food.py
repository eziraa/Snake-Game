from turtle import Turtle


class Food(Turtle):
    """
    Food class to create food for snake and it is plased randomly"""

    def __init__(self) -> None:
        self.__init__("circle")
        self.color('red')
