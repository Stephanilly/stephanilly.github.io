from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        # TODO 1: Create snake body
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            coords = (x, 0)
            self.add_segment(coords)
            x -= 20

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg - 1].xcor()
            new_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def add_segment(self, coords):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(coords)
        self.snake_body.append(new_turtle)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    # TODO 3: Control the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
