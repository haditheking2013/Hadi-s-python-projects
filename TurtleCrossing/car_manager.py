from turtle import Turtle 
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self,spawnLocation):
        super().__init__(shape = 'square')
        self.penup()
        self.shapesize(1,2)
        self.goto(320,spawnLocation)
        self.left(180)
        self.color(random.choice(COLORS))



    def move(self):
        self.forward(MOVE_INCREMENT)


    
