import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False

    #Detect successful crossing
    if player.ycor() > 280:
        player.reset()
        car_manager.speed_up_cars()
        scoreboard.increase_level()

scoreboard.game_over()
screen.exitonclick()