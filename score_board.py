from turtle import Turtle
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over, your final score is {self.score}!", align="center", font=FONT)
