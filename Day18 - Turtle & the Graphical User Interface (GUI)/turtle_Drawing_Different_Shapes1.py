from turtle import Turtle, Screen
import random as r

t = Turtle()
t.shape("turtle")

colour = ["red", "green", "blue", "black", "brown", "yellow", "medium blue", "indigo"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.right(angle)
        t.forward(100)


for shape_side_n in range(3, 11):
    t.color(r.choice(colour))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
