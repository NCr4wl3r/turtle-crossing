from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("turtle")
        self.setheading(90)
        self.reset_position()

    def move_up(self):
        new_position = self.ycor() + MOVE_DISTANCE
        self.sety(new_position)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_on_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y
