from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(random.randint(300, 520), random.randint(-250, 240))
        self.backward(self.car_speed)

    def move(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT





