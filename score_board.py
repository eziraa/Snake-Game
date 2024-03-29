from turtle import Turtle

# declare constant variable

ALIGNMENT = 'center'
FONT = ("Arial", 15, "normal")

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
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        """
        This method is display game over message"""
        self.goto(0, 0)
        self.write("GAME OVER!!!", align=ALIGNMENT, font=FONT)
