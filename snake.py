from turtle import Screen , Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEDISTANCE = 20

class Snake():
    
    def __init__(self) -> None:
        self.segments = []
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.createSegments()



    def  createSegments(self):

        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def moveSnake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[i - 1].xcor()
            y_new = self.segments[i - 1].ycor()
            self.segments[i].goto(x_new, y_new)
        self.segments[0].forward(MOVEDISTANCE)
