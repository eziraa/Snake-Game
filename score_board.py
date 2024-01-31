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
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        """
        This mathod is to update score"""
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 15, "normal"))
