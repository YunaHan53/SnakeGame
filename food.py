from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        ran_x = random.randrange(-280, 280)
        ran_y = random.randrange(-280, 280)
        self.goto(ran_x, ran_y)