from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from border import Border
from scoreboard import Scoreboard
# set the main screen
screen = Screen()
screen.bgpic("tennis.gif")
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# draw borders
border = Border()
r_paddle = Paddle(350, 0)
r_paddle.color("red")
l_paddle = Paddle(-350, 0)
l_paddle.color("white")
ball = Ball()
score = Scoreboard()
# keyboard configuration
screen.listen()
screen.onkey(fun=r_paddle.up, key="w")
screen.onkey(fun=r_paddle.down, key="s")
screen.onkey(fun=l_paddle.up, key="Up")
screen.onkey(fun=l_paddle.down, key="Down")
# start the game
game = True
while game:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_forward()
    # manage the ball movement and collision with objects
    if ball.ycor() > 261 or ball.ycor() < -261:
        ball.bouncing()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.paddle_collision()
    if ball.xcor() > 400:
        ball.ball_out()
        score.left_win()
    if ball.xcor() < -400:
        ball.ball_out()
        score.right_win()
    # manage scores and game over when either player scores e.g 11 points
    if score.r_score >= 11:
        score.red_wins()
        game = False
        break
    if score.l_score >= 11:
        score.white_wins()
        game = False
        break

screen.exitonclick()
