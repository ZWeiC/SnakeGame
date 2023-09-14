from turtle import Turtle
import random
import turtle
can = "can.gif"
turtle.register_shape(can)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(can)
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)