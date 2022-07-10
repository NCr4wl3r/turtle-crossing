from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()

    def print_score(self, score):
        self.clear()
        self.goto(-280, 270)
        str_template = f"Score : {score}"
        self.pendown()
        self.write(str_template, align="left", font=FONT)
        self.penup()

    def print_game_over(self):
        self.goto(-20, 0)
        str_template = "GAME OVER"
        self.pendown()
        self.write(str_template, align="center", font=FONT)
        self.penup()
