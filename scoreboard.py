from turtle import Turtle


# draw the scoreboard
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

    # manage scoreboard
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 215)
        self.color("white")
        self.write(arg=self.l_score, align="center", font=("Impact", 40, "normal"))
        self.goto(100, 215)
        self.color("red")
        self.write(arg=self.r_score, align="center", font=("Impact", 40, "normal"))

    # manage if the left player scores a point
    def left_win(self):
        self.l_score += 1
        self.update_scoreboard()

    # manage if the right player scores a point
    def right_win(self):
        self.r_score += 1
        self.update_scoreboard()

    # manage if red player wins the game
    def red_wins(self):
        self.color("red")
        self.goto(0, 0)
        self.write(arg="Red wins. Congratulations!", align="center", font=("Impact", 40, "normal"))

    # manage if white player wins the game
    def white_wins(self):
        self.color("white")
        self.goto(0, 0)
        self.write(arg="White wins. Congratulations!", align="center", font=("Impact", 40, "normal"))
