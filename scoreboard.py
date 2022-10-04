from turtle import Turtle
from os.path import exists
FONT = ("Calibri", 72, "normal")
FONT_LARGE = ("Calibri", 112, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        if exists("high-score.txt"):
            with open("high-score.txt", "r") as file:
                self.high_score = int(file.read())
        else:
            self.high_score = 0
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(380, 170)
        self.write(self.score, align="RIGHT", font=FONT)
        self.goto(-380, 170)
        self.write(f"x{self.lives}", align="LEFT", font=FONT)

    def score_points(self, points):
        self.score += points
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="CENTER", font=FONT_LARGE)
        self.goto(0, -90)
        if self.score > self.high_score:
            self.write(f"New High Score: {self.score}", align="CENTER", font=FONT)
            with open("high-score.txt", "w") as file:
                file.write(f"{self.score}")
        else:
            self.write(f"Score: {self.score}", align="CENTER", font=FONT)
            self.goto(0, -180)
            self.write(f"High Score: {self.high_score}", align="CENTER", font=FONT)
