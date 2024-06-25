from turtle import Turtle, Screen
import random
# from turtle import *
# import turtle as t

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color("red")


# Dashed line
# for _ in range(10):
#     tim.forward(5)
#     tim.up()
#     tim.forward(5)
#     tim.down()

# Multiple shapes
for i in range(3,11):
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.color(r,g,b)

screen.exitonclick()