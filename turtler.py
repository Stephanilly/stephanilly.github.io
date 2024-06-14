import time
from turtle import Screen
from turtler_player import Player
from turtler_cars import CarManager
from turtler_score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player.ycor() >= 280:
        score.scored()
        player.reset_position()
        car_manager.speed_up()
        screen.update()
    for car in car_manager.all_cars:
        if player.distance(car) < 30 and player.xcor() < car.xcor() - 20 or player.distance(car) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
