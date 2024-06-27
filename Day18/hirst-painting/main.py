# import colorgram

# # Extract colours from image
# colours = colorgram.extract("hirst-painting/image.jpeg", 25)
# rgb_colours = []

# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_colours.append((r, g, b))

# print(rgb_colours)

from turtle import Turtle, Screen
import random

colour_list = [(184, 148, 94), (152, 104, 46), (178, 150, 22), (83, 34, 27), (228, 229, 231), (12, 57, 73), (31, 100, 120), (101, 41, 48), (57, 137, 121), (108, 40, 29), (22, 65, 50), (40, 80, 7), (94, 62, 68), (110, 8, 9), (199, 91, 65), (116, 167, 77), (131, 178, 92), (139, 167, 175), (216, 202, 142), (178, 147, 150), (179, 205, 177), (225, 177, 167)]

screen = Screen()
screen.setup(800,800)
screen.colormode(255)

tim = Turtle()
tim.shape("arrow")
tim.penup()
tim.speed("fastest")

# x coordinate start
x = -315
# y coordinate start
y = -315

num_of_dots = 10
step_size = 70

for _ in range(num_of_dots):
    for _ in range(num_of_dots):
        tim.teleport(x, y)
        tim.dot(20, random.choice(colour_list))
        x += step_size
    x -= step_size * num_of_dots
    y += step_size

tim.hideturtle()

screen.exitonclick()