from turtle import Turtle, Screen
import turtle as t
import random

tom = Turtle()
tom.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_spirograph(gap_size):
    for i in range(int(360 / gap_size)):
        tom.color(random_color())
        tom.circle(100)
        # current_heading = tom.heading()
        tom.setheading(tom.heading() + gap_size)


draw_spirograph(3)

screen = Screen()
screen.exitonclick()
