from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, lvl) -> None:
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.setheading(180)
        self.setx(300)
        self.set_speed(lvl)

    def move(self):
        self.forward(self.move_distance)

    def set_starting_y_pos(self):
        self.sety(randint(-250, 250))

    def set_speed(self, lvl=1):
        self.move_distance = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (lvl - 1)
