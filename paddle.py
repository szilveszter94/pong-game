from turtle import Turtle, Screen

# set the initial speed variable
SPEED = 40
# set the screen
screen = Screen()

# create the paddle
class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.speed("fastest")
        self.goto(x_cor, y_cor)
    # manage movement
    def up(self):
        y_cor = self.ycor() + SPEED
        self.goto(self.xcor(), y_cor)

    def down(self):
        y_cor = self.ycor() - SPEED
        self.goto(self.xcor(), y_cor)
