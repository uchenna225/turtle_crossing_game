from turtle import Turtle
import random

COLORS = ["green", "blue", "red", "purple", "orange", "brown", "pink"]


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.num = []
        self.update_speed = 10

    def create(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_y = random.randint(-240, 250)
            new_car.goto(280, new_y)
            self.num.append(new_car)

    def move(self):
        for car in self.num:
            car.setheading(180)
            car.fd(self.update_speed)

    def end(self):
        self.color("white")
        self.penup()
        self.write(f"GAME OVER", align="center", font=("Arial", 16, "normal"))

    def update(self):
        self.update_speed += 10
