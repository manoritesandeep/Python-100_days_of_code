from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(25)


screen.listen()
screen.onkey(fun=move_forwards, key="space")
screen.exitonclick()
