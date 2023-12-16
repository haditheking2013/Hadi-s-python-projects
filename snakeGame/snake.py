from re import I
from turtle import Turtle
import time


class Snake:
        
        def __init__(self):
            self.x = 0
            self.snake = []
            self.create_snake()
            

        def create_snake(self):
             for i in range(3):
                 i = Turtle('square')
                 i.penup()
                 i.color('white')
                 i.goto(x=self.x,y=0)
                 self.snake.append(i)
                 self.x -= 20


        def move(self):
            self.xi,self.yi = self.snake[0].position()
            self.snake[0].forward(20)
            
            
            for i in self.snake[1:]:
                self.local_x,self.local_y = i.position()
                i.goto(self.xi,self.yi)
                self.xi,self.yi = self.local_x,self.local_y

        def press_w(self):
            if self.snake[0].heading() != 270:
                 self.snake[0].setheading(90)
                 
        def press_a(self):
            if self.snake[0].heading() != 0:
                  self.snake[0].setheading(180)
                  
        def press_s(self):
                 if self.snake[0].heading() != 90:
                        self.snake[0].setheading(270)
                        
        def press_d(self):
                    if self.snake[0].heading() != 180:
                            self.snake[0].setheading(0)
        def headx(self):
            return  self.snake[0].xcor()
        def heady(self):
            return self.snake[0].ycor()




        def add_snake(self):
                 i = Turtle('square')
                 i.hideturtle()
                 i.penup()
                 i.color('white')
                 i.goto(self.snake[-1].position())
                 self.snake.append(i)
                 i.showturtle()
                 


        def reset_snake(self):
            for s in self.snake:
                s.goto(-1000,-1000)
            self.snake =[]
            self.create_snake()
            

                 
              

                            







                 



    

                 



