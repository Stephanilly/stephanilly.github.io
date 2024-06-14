from turtle import Turtle

STARTING_Y = -280
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > STARTING_Y:
            self.backward(MOVE_DISTANCE)

    def reset_position(self):
        self.teleport(0, STARTING_Y)
