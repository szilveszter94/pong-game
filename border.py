from turtle import Turtle

# draw the border
class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-380, 280)
        self.pendown()
        self.pensize(10)
        self.goto(-380, -280)
        self.goto(380, -280)
        self.goto(380, 280)
        self.goto(-380, 280)
