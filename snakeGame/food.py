from turtle import Turtle
import random




class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        
        self.color('blue')
        
        self.goto(x=random.randrange(-280,280,20),y=random.randrange(-280,280,20))



    def move_to_new_loc(self):
        self.goto(x=random.randrange(-280,280,20),y=random.randrange(-280,280,20))
        








    