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

scoreboard = Scoreboard()
turtle_player = Player()
cars = CarManager()

# init values:
lvl = 1
scoreboard.print_score(lvl)
game_is_on = True

# Player movement event
screen.onkeypress(turtle_player.move_up, key="Up")

while game_is_on:

    # Create cars:
    cars.add_new_car(lvl)

    # move the cars
    cars.move_cars()

    # check cars colision:
    for car in cars.cars:
        if turtle_player.distance(car) < 20:
            scoreboard.print_game_over()
            game_is_on = False

    # Check Player arrive finish line:
    if turtle_player.is_on_finish_line():
        # reset player position
        turtle_player.reset_position()
        # rise lvl
        lvl += 1
        cars.update_cars_speed(lvl)
        scoreboard.print_score(lvl)

    time.sleep(0.1)
    screen.update()


screen.exitonclick()
