from turtle import Turtle

coordinate = (0, -280)

class TIm(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(coordinate)

    def up(self):
        self.fd(20)

    def fresh(self):
        self.goto(coordinate)

