from turtle import Turtle, Screen
import random
# from turtle import *
# import turtle as t

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

# tim.pensize(5)
# tim.forward(25)

# Dashed line
# for _ in range(10):
#     tim.forward(5)
#     tim.up()
#     tim.forward(5)
#     tim.down()

# Multiple shapes
# for i in range(3,11):
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(360/i)

#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     tim.color(r,g,b)

# Random Walk
# angles = [0,90,180,270]
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(angles))    

# Spirograph

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(random_color())
        tim.circle(radius=100)

draw_spirograph(5)

screen.exitonclick()