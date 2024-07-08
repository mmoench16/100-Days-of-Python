from turtle import Turtle

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movement = 10
        self.y_movement = 10

    def move(self):
        self.goto(self.xcor() + self.x_movement, self.ycor() + self.y_movement)
        print(f"xpos: {self.xcor()}")
        print(f"xmov: {self.x_movement}")
        print(f"ypos: {self.ycor()}")
        print(f"ymov: {self.y_movement}")
    
    def bounce(self):
        self.y_movement *= -1