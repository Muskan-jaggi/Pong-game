from turtle import Turtle, Screen
from paddle import Paddle
from screen_divider import DividingLine
from ball import Ball
from scoreboard import Scoreboard
import time

scr = Screen()
scr.title("Pong Game")
scr.bgcolor("black")
scr.setup(1000, 600)
scr.tracer(0)

paddle_1 = Paddle(-480)
paddle_2 = Paddle(480)
ball = Ball()
line = DividingLine()
score = Scoreboard()

scr.listen()
# paddle_1 (left) movement controls
scr.onkey(paddle_1.up, "w")
scr.onkey(paddle_1.down, "s")

# paddle_2 (right) movement controls
scr.onkey(paddle_2.up, "Up")
scr.onkey(paddle_2.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    scr.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle_1) < 50 and ball.xcor() < -440) or (ball.distance(paddle_2) < 50 and ball.xcor() > 440):
        ball.bounce_x()

    # when right paddle misses
    if ball.xcor() > 500:
        ball.reset_position()
        score.l_point()

    # when left paddle misses
    if ball.xcor() < -500:
        ball.reset_position()
        score.r_point()

scr.exitonclick()
