from turtle import Turtle
FONT = ("Courier", 64, "normal")
ALIGNMENT = "CENTER"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.score = 0
        self.lives = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(350, 170)
        self.write(self.score, align=ALIGNMENT, font=FONT)
        self.goto(-350, 170)
        self.write(f"x{self.lives}", align=ALIGNMENT, font=FONT)

    def score_points(self, points):
        self.score += points
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()


# Display points

# Display lives
