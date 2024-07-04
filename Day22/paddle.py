from turtle import Turtle

WIDTH = 20
HEIGHT = 100
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position_tuple) -> None:
        super().__init__()
        self.shape("square")
        # self.resizemode("user")
        self.color("white")
        self.shapesize(stretch_wid=HEIGHT/20, stretch_len=WIDTH/20)
        self.penup()
        self.teleport(position_tuple[0], position_tuple[1])

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        
