from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars = []

    def add_new_car(self, lvl):
        max_rand = 9 - lvl if lvl < 8 else 2
        if randint(1, 9 - lvl) == 1:
            self.cars.append(Car(lvl))

    def clear_cars(self):
        self.cars.clear()

    def move_cars(self):
        for car in self.cars:
            car.move()

    def update_cars_speed(self, lvl):
        for car in self.cars:
            car.set_speed(lvl)


class Car(Turtle):
    def __init__(self, lvl) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(choice(COLORS))
        self.setheading(180)
        self.setx(300)
        self.set_speed(lvl)
        self.set_starting_y_pos()

    def move(self):
        self.forward(self.move_distance)

    def set_starting_y_pos(self):
        self.sety(randint(-250, 250))

    def set_speed(self, lvl=1):
        self.move_distance = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (lvl - 1)
