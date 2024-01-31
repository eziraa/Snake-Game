from turtle import Turtle


class ScoreBoard(Turtle):
    """
    This class is to create keep to tack of score of the game"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 15, "normal"))
        self.hideturtle()
