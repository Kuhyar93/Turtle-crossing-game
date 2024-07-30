import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()

cars=[]

for i in range(18):
    car = CarManager()
    cars.append(car)
screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()
    for car in cars:
        if car.xcor() < -320:
            car.goto(random.randint(300, 380), random.randint(-240, 260))

    for car in cars:
        if car.distance(player) < 18:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() == 280:
        scoreboard.update()
        player.reset()
        for car in cars:
            car.level_up()

screen.exitonclick()