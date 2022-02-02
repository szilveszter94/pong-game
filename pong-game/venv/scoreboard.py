from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 215)
        self.write(arg=self.l_score, align="center", font=("Impact", 40, "normal"))
        self.goto(100, 215)
        self.color("red")
        self.write(arg=self.r_score, align="center", font=("Impact", 40, "normal"))


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 215)
        self.color("white")
        self.write(arg=self.l_score, align="center", font=("Impact", 40, "normal"))
        self.goto(100, 215)
        self.color("red")
        self.write(arg=self.r_score, align="center", font=("Impact", 40, "normal"))


    def left_win(self):
        self.l_score += 1
        self.update_scoreboard()
    def right_win(self):
        self.r_score += 1
        self.update_scoreboard()

    def red_wins(self):
        self.color("red")
        self.goto(0,0)
        self.write(arg="Red wins. Congratulations!", align="center", font=("Impact", 40, "normal"))

    def white_wins(self):
        self.color("white")
        self.goto(0, 0)
        self.write(arg="White wins. Congratulations!", align="center", font=("Impact", 40, "normal"))


