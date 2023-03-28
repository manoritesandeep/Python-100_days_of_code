from turtle import Turtle, Screen
import random as r

t = Turtle()
t.shape("turtle")
t.pensize(15)
t.speed("fast")

colour = ["red", "green", "blue", "black", "brown", "yellow", "medium blue", "indigo"]
direction = [0, 90, 180, 270]

for _ in range(200):
    t.color(r.choice(colour))
    t.forward(30)
    t.setheading(r.choice(direction))

screen = Screen()
screen.screensize(400, 300)
screen.exitonclick()
