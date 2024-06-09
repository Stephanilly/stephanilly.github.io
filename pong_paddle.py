from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.teleport(x, 0)
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

