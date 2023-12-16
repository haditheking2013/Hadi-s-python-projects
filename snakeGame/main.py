from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

moh = Screen()
moh.setup(height=600,width=585)
moh.bgcolor('black')
moh.title('Snake Game')
moh.tracer(0)
hadi = Snake()
score = Score()
moh.update()



game_is_on = True
apple = Food()
while game_is_on:
    
    moh.listen()
    if  moh.onkey(hadi.press_w,'w'):
        hadi.move()
    elif moh.onkey(hadi.press_a,'a'):
        hadi.move()
    elif moh.onkey(hadi.press_s,'s'):
        hadi.move()
    elif moh.onkey(hadi.press_d,'d'):
        hadi.move()
    else:
        hadi.move()
    if 5> (hadi.headx() - apple.xcor()) > -5 and 5> (hadi.heady() - apple.ycor()) > -5 :
        apple.move_to_new_loc()
        score.addScore()
        hadi.add_snake()
        
    time.sleep(0.1)
    if  hadi.headx()> 280 or hadi.headx() < -280 or hadi.heady() > 300 or hadi.heady()< -280:
    
        score.reset_score()
        hadi.reset_snake()
    for snk in hadi.snake[1:]:
        if hadi.snake[0].distance(snk) < 5:
            hadi.reset_snake()
            score.reset_score
            
    moh.update()

    
    
    

    
       
    

    
    


    
















moh.exitonclick()
