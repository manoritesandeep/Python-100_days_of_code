"""
W = Forwards
S = Backwards
A = Counter-Clockwise
D = Clockwise
C = Clear drawing and return cursor to center
"""

from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(25)


def move_backwards():
    tom.backward(25)


def move_left():
    tom.left(10)


def move_right():
    tom.right(10)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


# def move_counter_clockwise():
#     tom.setheading(to_angle=)

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
