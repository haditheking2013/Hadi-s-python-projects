import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
sleep_time = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

hadi = Player()
car = CarManager(30)
screen.onkey(hadi.move,'w')
score = Scoreboard()
game_is_on = True
list_of_cars = []
while game_is_on:
    time.sleep(sleep_time)

    for x in range(-250,250,20):
        if random.randrange(100) ==6:
            list_of_cars.append(CarManager(x))
    for lst in list_of_cars:
        if lst.xcor()>-320:
             lst.move()
             if hadi.distance(lst) < 20:
                game_is_on= False
                score.game_over()
        if hadi.ycor() > 250:
                hadi.reset()
                score.clear()
                score.increase()
                score.update()
                sleep_time *= 0.8
                screen.update()
        screen.update()

            
   



screen.exitonclick()
