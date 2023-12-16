from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.color('white')
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(x=-150,y=260)
        self.writeit()
        

    def writeit(self):
        self.write(f'Score: {self.score}  Highscore: {self.highscore}', align = 'left', font= ('Courier',24,'normal'))



    def addScore(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt','w') as data:
                data.write(str(self.highscore))
        self.clear()
        self.writeit()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.writeit()


    


    
    












