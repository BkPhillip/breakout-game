from turtle import Screen, getcanvas
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
bricks = []


def generate_bricks():
    color_index = 0
    for y in range(20, 170, 30):
        for x in range(-350, 420, 70):
            point_value = color_index + 1
            brick = Brick(brick_colors[color_index], point_value,  x, y)
            bricks.append(brick)
        color_index += 1


user_paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()
generate_bricks()
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
            scoreboard.score_points(brick.points)
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
        if scoreboard.lives == 1:
            game_on = False
            user_paddle.hideturtle()
            ball.hideturtle()
            scoreboard.clear()
            for brick in bricks:
                brick.hideturtle()
            screen.update()
            scoreboard.game_over()
        else:
            scoreboard.lose_life()
            ball.reset_ball()

    # Check if all bricks destroyed
    if len(bricks) == 0:
        time.sleep(0.5)
        generate_bricks()
        ball.reset_ball()
        ball.move_speed /= 1.5



screen.exitonclick()
