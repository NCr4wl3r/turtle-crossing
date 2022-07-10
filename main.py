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

turtle_player = Player()
cars = CarManager()
loop_counter = 0
lvl = 1

game_is_on = True
while game_is_on:
    loop_counter += 1
    time.sleep(0.1)
    screen.update()

    # Create cars every 6 loops:
    if loop_counter % 6 == 0:
        cars.add_new_car(lvl)

    # move the cars
    cars.move_cars()

    # Player movement event
    screen.onkeypress(turtle_player.move_up, key="Up")

    # check cars colision:
    for car in cars.cars:
        if turtle_player.distance(car) < 20:
            game_is_on = False

    # Check Player arrive finish line:
    if turtle_player.is_on_finish_line():
        # reset player position
        turtle_player.reset_position()
        # rise lvl
        lvl += 1
        cars.update_cars_speed(lvl)

screen.exitonclick()
