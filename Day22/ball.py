from turtle import Turtle

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movement = 10
        self.y_movement = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_movement, self.ycor() + self.y_movement)
    
    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1