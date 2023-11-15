from turtle import Turtle
import random


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.num_cars()

    def num_cars(self):
        for i in range(10):
            new_y = random.randint(-260, 260)
            self.car(new_y)

    def car(self, y):
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(280, y)
