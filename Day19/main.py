from turtle import Turtle, Screen

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

screen.exitonclick()