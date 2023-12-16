from turtle import Turtle,Screen, width
from pingpong import Pong
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
pong1 = Pong(350,0)
pong2 = Pong(-350,0)
ball = Ball()

screen.listen()
screen.update()
game_is_on = True
screen.tracer(1)

screen.onkey(pong2.goUp,'w')
screen.onkey(pong2.goDown,'s')
screen.onkey(pong1.goUp,'Up')
screen.onkey(pong1.goDown,'Down')
while game_is_on:
    ball.move()
    time.sleep(0.1)


screen.exitonclick()