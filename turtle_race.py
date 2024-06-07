import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
racing = False
user_bet = screen.textinput("Make your bet", "Which turtle will win the race?\nred, orange, yellow, green, "
                                             "blue, or purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x = -230
y = -70
for shade in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(shade)
    new_turtle.goto(x, y)
    y += 30
    all_turtles.append(new_turtle)

if user_bet:
    racing = True

while racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            racing = False
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You lost. The {winner} turtle is the winner.")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


screen.exitonclick()
