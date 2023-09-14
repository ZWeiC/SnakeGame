import turtle
from turtle import Turtle,Screen
STARTINT_SEGMENTS = 5
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DISTANCE = 25
cpc = "cpc.gif"
turtle.register_shape(cpc)
class Snake:
    def __init__(self):
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]

    def create_segments(self):
        for i in range(STARTINT_SEGMENTS):
            position = 0 + i * -20, 0
            self.add_segment(position)


    def add_segment(self,position):
        snake_segment = Turtle(shape=cpc)
        snake_segment.shapesize(stretch_len=0.1, stretch_wid=0.1)
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)
    def increase_snake(self):
        self.add_segment(self.segments[-1].position())


    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_move(self):

        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            new_heading = self.segments[seg_num - 1].heading()
            self.segments[seg_num].goto(new_x,new_y)
            self.segments[seg_num].setheading(new_heading)
        self.segments[0].forward(DISTANCE)

