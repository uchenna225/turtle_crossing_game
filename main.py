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
    time.sleep(0.1)
    screen.update()

    # creates cars
    car.create()
    car.move()

    # Game_over
    for cars in car.num:
        if cars.distance(tim) < 20:
            car.end()
            Game_on = False

    # turtle_movement
    screen.onkey(tim.up, "Up")

    if tim.ycor() == 280:
        tim.add()
        tim.fresh()
        car.update()


screen.exitonclick()
