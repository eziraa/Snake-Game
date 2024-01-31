from turtle import Turtle


class ScoreBoard(Turtle):
    """
    This class is to create keep to tack of score of the game"""

    def __init__(self):
        super().__init__()
        self.score = 0
