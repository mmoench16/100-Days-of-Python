from turtle import Turtle, Screen
import random

is_race_on = False
tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

i = 0
for colour in colours:
    t = Turtle(shape="turtle")
    t.color(colour)
    t.penup()
    t.goto(x=-230,y=-75 + i)
    turtles.append(t)
    i += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()