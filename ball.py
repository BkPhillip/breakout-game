from turtle import Turtle
BALL_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.goto(0, -165)
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_ball(self):
        self.goto(0, -165)
        self.y_move = abs(self.y_move)
        self.bounce_x()
