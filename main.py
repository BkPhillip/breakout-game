from turtle import Turtle, Screen, getcanvas
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

brick_colors = ["blue", "green", "yellow", "orange", "red"]

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("BREAKOUT GAME")
screen.tracer(0)

user_paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

bricks = []
color_index = 0
for y in range(20, 170, 30):
    for x in range(-350, 420, 70):
        brick = Brick(brick_colors[color_index], x, y)
        bricks.append(brick)
    color_index += 1

screen.listen()
screen.onkeypress(fun=user_paddle.move_left, key="Left")
screen.onkeypress(fun=user_paddle.move_right, key="Right")

canvas = getcanvas()
canvas.bind('<Motion>', user_paddle.move_paddle)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall top/left/right
    if ball.ycor() > 230:
        ball.bounce_y()

    if ball.xcor() > 370 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with brick
    for brick in bricks:
        if ball.distance(brick) < 40:
            ball.bounce_y()
            scoreboard.score_points(1)
            bricks.remove(brick)
            brick.hideturtle()

    # Detect collision with paddle
    if ball.distance(user_paddle) < 50 and ball.ycor() < -170 and ball.y_move < 0:
        # Detect which half of paddle is struck to determine x direction
        if ball.xcor() < user_paddle.xcor():
            ball.x_move = -1 * abs(ball.x_move)
        else:
            ball.x_move = abs(ball.x_move)
        ball.bounce_y()

    # Detect ball goes out of bounds
    if ball.ycor() < -210:
        ball.reset_ball()

screen.exitonclick()
