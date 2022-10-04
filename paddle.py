from turtle import Turtle, window_width


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto((0, -200))

    def move_left(self):
        if self.xcor() < -330:
            pass
        else:
            new_x = self.xcor() - 20
            self.goto(x=new_x, y=self.ycor())

    def move_right(self):
        if self.xcor() > 330:
            pass
        else:
            new_x = self.xcor() + 20
            self.goto(x=new_x, y=self.ycor())

    def move_paddle(self, event):
        mouse_x = event.x - (window_width()) / 2
        # if mouse_x < -350 or mouse_x > 350:
        #     pass
        # else:
        # The above if else is useful for keeping paddle from going out of bounds partially, but I fount it
        # useful to be able to hit ball with other side of paddle to get it out of bounce pattern
        self.goto(x=mouse_x, y=self.ycor())
