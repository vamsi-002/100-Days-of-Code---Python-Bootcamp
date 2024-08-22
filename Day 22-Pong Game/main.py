from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

POSITIONS = [(-350, 0), (350, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Creating paddles, ball, and scoreboard
paddle1 = Paddle(POSITIONS[0])
paddle2 = Paddle(POSITIONS[1])
ball = Ball()
scoreboard = ScoreBoard()

# Setting up key listeners for paddle movement
screen.listen()
screen.onkey(paddle1.go_up, "w")
screen.onkey(paddle1.go_down, "s")
screen.onkey(paddle2.go_up, "Up")
screen.onkey(paddle2.go_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Ball bounces off the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Ball bounces off the paddles
    if ball.distance(paddle1) < 50 and ball.xcor() < -320 or ball.distance(paddle2) < 50 and ball.xcor() > 320:
        ball.x_bounce()

    # Detect when the ball goes out of bounds
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.y_point()
    
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.x_point()

    # Optional: End the game if a player reaches a certain score
    if scoreboard.x_score == 10 or scoreboard.y_score == 10:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
