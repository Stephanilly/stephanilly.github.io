from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-270, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT, align="left")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")

    def scored(self):
        self.score += 1
        self.update_scoreboard()
