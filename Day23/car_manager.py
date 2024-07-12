from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            self.cars.append(self.Car())

    def move_cars(self):
        for car in self.cars:
            car.move(self.car_speed)

    def speed_up_cars(self):
        self.car_speed += MOVE_INCREMENT
    
    class Car(Turtle):
        def __init__(self) -> None:
            super().__init__()
            self.shape("square")
            self.color(random.choice(COLORS))
            self.penup()
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.goto(300,random.randint(-250, 250))
            self.setheading(180)

        def move(self, distance):
            self.forward(distance)
