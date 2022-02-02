from turtle import Turtle
SHAPE = "circle"
COLOR = "yellow"

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.color(COLOR)
        self.pencolor("red")
        self.y_move = 8
        self.x_move = 8
        self.ball_speed = 0.04


    def move_forward(self):

        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bouncing(self):
        self.y_move *= -1
    def paddle_collision(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
    def ball_out(self):
        self.goto(0,0)
        self.ball_speed = 0.04
        self.paddle_collision()







