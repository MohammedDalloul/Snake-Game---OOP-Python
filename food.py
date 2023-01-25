from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.change_place()

    def change_place(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)




