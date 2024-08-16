from turtle import Turtle, Screen
import random
import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
START_X = -230
FINISH_LINE_X = 230
TURTLE_SHAPE = 'turtle'

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter the color: ")

colors = ['red', 'blue', 'orange', 'yellow', 'green', 'violet', 'indigo']
y_positions = [-80, -50, -20, 10, 40, 70, 100]

turtles = []
for index in range(len(colors)):
    new_turtle = Turtle(shape=TURTLE_SHAPE)
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=START_X, y=y_positions[index])
    turtles.append(new_turtle)

def start_race():
    if user_bet:
        game_on = True
        screen.title("Race has Started...")

        while game_on:
            for turtle in turtles:
                turtle.forward(random.randint(0, 10))
                if turtle.xcor() > FINISH_LINE_X:
                    game_on = False
                    winning_color = turtle.pencolor()

                    if winning_color == user_bet:
                        screen.title(f"You Won! The {winning_color} turtle is the Winner!")
                        print(f"You Won!! The {winning_color} turtle is the Winner")
                    else:
                        screen.title(f"You Lost! The {winning_color} turtle is the Winner!")
                        print(f"You Lost!! The {winning_color} turtle is the Winner")
                    
                    return

start_race()

screen.exitonclick()
