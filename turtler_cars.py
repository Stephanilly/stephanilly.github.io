import random
from turtle import Turtle

COLORS = ["DarkRed", "DarkOrange", "gold", "green4", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.car_reserve = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            random_y = random.randrange(-250, 250, 20)
            new_car.teleport(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
            if car.xcor() < -320:
                self.all_cars.remove(car)
                self.car_reserve.append(car)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
