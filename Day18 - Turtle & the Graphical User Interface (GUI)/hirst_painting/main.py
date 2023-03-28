# import colorgram
#
# colors = colorgram.extract("painting.jpg", 360)
# print(type(colors[0]))
# # print(colors[0])
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(type(rgb_colors[0]))
# print(rgb_colors)

color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40),
              (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159),
              (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102),
              (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39),
              (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30),
              (16, 77, 106)]
# print(len(color_list))


import turtle as t
import random

tom = t.Turtle()
# because we're using the RGB color that has the r, g and b values between 0 and 255,
# we first have to get the turtle module to change its color mode to 255
t.colormode(255)
tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(250)
tom.setheading(0)
tom.speed("fastest")
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)

    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        # 50 * 10 dots
        tom.forward(500)
        tom.setheading(0)



screen = t.Screen()
screen.exitonclick()
