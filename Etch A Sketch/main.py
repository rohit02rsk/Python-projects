import turtle as t
from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def move_forward():
    turt.forward(10)

def move_backward():
    turt.backward(10)

def rotate_right():
    turt.right(15)

def rotate_left():
    turt.left(15)

def clear_screen():
    turt.reset()

screen.listen()

screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "a", fun = rotate_left)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "d", fun = rotate_right)
screen.onkey(key = "c", fun = clear_screen)

screen.exitonclick()
