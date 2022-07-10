from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape="turtle") -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_position = self.ycor() + MOVE_DISTANCE
        self.sety(new_position)
