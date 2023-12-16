from turtle import Turtle


class Pong(Turtle):
    def __init__(self,x,y):
        super().__init__(shape='square')
        self.color('white')
        self.shapesize(5,1)
        self.penup()
        self.goto(x,y)
         





    def goUp(self):
        
        self.goto(self.xcor(),self.ycor()+20)

    def goDown(self):
        self.goto(self.xcor(),self.ycor()-20)




