from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEDISTANCE = 20

class Snake():
    
    def __init__(self) -> None:
        self.segments = []
        self.createSegments()


    def  createSegments(self):

        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        self.head = self.segments[0]

    def moveSnake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[i - 1].xcor()
            y_new = self.segments[i - 1].ycor()
            self.segments[i].goto(x_new, y_new)
        self.head.forward(MOVEDISTANCE)
