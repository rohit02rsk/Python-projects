import random
import turtle as t
from turtle import Turtle, Screen

t.colormode(255)
straw = Turtle()
straw.speed("fastest")
straw.penup()
straw.hideturtle()

# ----HOW THE COLORS WERE EXTRACTED:----
# rgb_colors = []
# colors = colorgram.extract("Turtle Graphics\image.jpg", 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))     

# print(rgb_colors)
#---------------------------------------

color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

straw.setheading(225)
straw.forward(300)
straw.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    straw.dot(20, random.choice(color_list))
    straw.forward(50)
    if dot_count % 10 == 0:
        straw.setheading(90)
        straw.forward(50)
        straw.setheading(180)
        straw.forward(500)
        straw.setheading(0)

screen = Screen()
screen.exitonclick()
