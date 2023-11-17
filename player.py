from turtle import Turtle

coordinate = (0, -280)


class TIm(Turtle):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.level()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(coordinate)

    def up(self):
        self.fd(20)

    def fresh(self):
        self.goto(coordinate)

    def level(self):
        self.color("white")
        self.penup()
        self.goto(-260, 270)
        self.write(f"level {self.stage}", align="center", font=("Arial", 16, "normal"))

    def add(self):
        self.stage += 1
        self.clear()
        self.level()
