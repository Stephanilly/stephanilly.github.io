from turtle import Screen
from sn_snake import Snake
from sn_food import Food
from sn_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("gray10")
screen.title("Snake Game")
screen.tracer(0)


# TODO 2: Move the snake
screen.update()
game_on = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # TODO 4: Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_up()
        snake.extend()

    # TODO 6: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # TODO 7: Detect collision with snake
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
