from turtle import Screen
from pong_paddle import Paddle
from pong_ball import Ball
from pong_score import Scoreboard
import time

# TODO : create screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("gray10")
screen.title("Pong")
screen.tracer(0)

# TODO : create a controllable paddle
r_paddle = Paddle(350)
# TODO : create a second paddle
l_paddle = Paddle(-350)

# TODO : create the ball and make it move
ball = Ball()

# TODO : build a scoreboard with two scores
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    # TODO : detect collision with wall to bounce
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    # TODO : detect collision with paddle to bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        time.sleep()
    # TODO : detect a miss
    elif ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.r_score > 2 or scoreboard.l_score > 2:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
