from turtle import Screen , Turtle

POSITIONS = [(0,0),(0,-20),(0,-40)]


class Snake():
    
    def __init__(self) -> None:
        self.segments = []

    def  createSegments(self):

        for position in POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
