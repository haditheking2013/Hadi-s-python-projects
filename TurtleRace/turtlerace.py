from turtle import Turtle,Screen, color, position
import random
class_color = ['red','blue','purple','orange','yellow','green']
colors= ['red','blue','purple','orange','yellow','green']
moh = Screen()
moh.setup(600,600)
y = -100
race_is_on = False
the_chosen_one = moh.textinput(title='Choose your turtle',prompt='Choose which color will win NOWWW!!!')
if the_chosen_one:
    race_is_on = True
winner = None
if race_is_on:    
    for i in range(len(class_color)):
        n = i
        i = Turtle(shape='turtle')
        class_color[n] = i
        i.penup()
        i.color(colors[n])
        i.goto(x=-270,y=y)
        y+=50
while race_is_on:
    for i in class_color:
        i.forward(random.randint(0,10))
        if i.xcor() > 270:
            race_is_on = False
            
            if i.color()[0] == the_chosen_one:
                print('Congratsss you wonnnn')
            else:
                print(f'hard luck maybe next time {i.color()[0]} won')
            


moh.exitonclick()
    