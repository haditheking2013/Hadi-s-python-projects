from turtle import Turtle
FONT = ("Courier", 28, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.HighScore = 0
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.update()



    def update(self):
        self.write(f'Level: {self.level}',align='left', font=FONT)


    def increase(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over!!!',align='center', font=FONT)
