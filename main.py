import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

turtle = Player()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Player movement event
    screen.onkeypress(turtle.move_up, key="Up")

    # Check Player arrive finish line:
    if turtle.is_on_finish_line():
        # TODO: reset position
        turtle.reset_position()
        # TODO: rise lvl
