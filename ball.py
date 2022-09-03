from turtle import Turtle

# config constants
SHAPE = "circle"
COLOR = "yellow"


# set ball object
class Ball(Turtle):
    def __init__(self):
        # config ball variables
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.color(COLOR)
        self.y_move = 8
        self.x_move = 8
        self.ball_speed = 0.04

    # config ball movement
    def move_forward(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    # manage ball collision with wall
    def bouncing(self):
        self.y_move *= -1

    # manage collision with paddle
    def paddle_collision(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    # manage ball out situation
    def ball_out(self):
        self.goto(0, 0)
        self.ball_speed = 0.04
        self.paddle_collision()
