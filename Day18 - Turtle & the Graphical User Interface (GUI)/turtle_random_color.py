import turtle as tu
from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
t.pensize(15)
t.speed("fast")
tu.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


direction = [0, 90, 180, 270]

for _ in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(direction))

screen = Screen()
screen.screensize(400, 300)
screen.colormode(150)
screen.exitonclick()
