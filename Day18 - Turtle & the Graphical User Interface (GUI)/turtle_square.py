from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.color("red")
for _ in range(4):
    tom.forward(100)
    tom.right(90)

screen = Screen()
screen.exitonclick()
