from turtle import Turtle

X_POS = 0
Y_POS = 270
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(X_POS, Y_POS)
        self.show_score()

    def show_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()