import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANGE = range(-250, 250)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.move_dist = STARTING_MOVE_DISTANCE
        

    def create_car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_len = 2, stretch_wid=1)
        car.color(random.choice(COLORS))
        car.goto(x=320, y=random.choice(RANGE))
        car.setheading(180)
        self.all_cars.append(car)

    def move_left(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
    
    def level_up(self):
        self.move_dist += MOVE_INCREMENT
            