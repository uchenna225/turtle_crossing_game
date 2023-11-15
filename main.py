from turtle import Screen
import time
from player import TIm
from cars import Cars

screen = Screen()
screen.tracer(0)

screen.setup(600, 600)
screen.bgcolor("black")

tim = TIm()
car = Cars()

Game_on = True
screen.listen()
while Game_on:
    # screen_update_and_refresh
    screen.update()
    time.sleep(0.1)

    # turtle_movement
    screen.onkey(tim.up, "Up")

    if tim.ycor() == 280:
        print("win")
        tim.fresh()

screen.exitonclick()
