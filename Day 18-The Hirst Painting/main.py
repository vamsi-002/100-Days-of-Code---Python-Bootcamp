import turtle as turtle_module
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw():
    for i in range(10):
        timmy.dot(15, random_color())
        timmy.penup()
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

timmy = turtle_module.Turtle()
turtle_module.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(220)
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()

for _ in range(10):
    draw()

screen = turtle_module.Screen()
screen.exitonclick()