from turtle import Turtle


class Brick(Turtle):
    def __init__(self, color, points, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(color)
        self.points = points
        self.pu()
        self.goto((x, y))
