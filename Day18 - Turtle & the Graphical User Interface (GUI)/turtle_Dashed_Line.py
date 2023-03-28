from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
for i in range(15):
    tom.forward(10)
    tom.pensize(width=2)
    tom.penup()
    tom.forward(10)
    tom.pendown()


screen = Screen()
screen.exitonclick()

