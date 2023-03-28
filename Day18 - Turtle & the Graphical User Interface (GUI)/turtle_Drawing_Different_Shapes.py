from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")

deg = 360
for i in range(3, 11):
    angle = deg/i
    for j in range(i):
        t.right(angle)
        t.forward(100)

screen = Screen()
screen.exitonclick()