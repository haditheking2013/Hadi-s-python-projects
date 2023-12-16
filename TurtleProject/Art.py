from calendar import c
import colorgram
import turtle
import random


color_list = []
def grab_color():
    colors = colorgram.extract('spots.jpg', 20)
    for color in colors:
        r,g,b = color.rgb.r,color.rgb.g,color.rgb.b
        color_list.append((r,g,b))


print(color_list)


colors = [(218, 231, 237), (149, 22, 65), (118, 140, 215), (195, 76, 114),
(188, 186, 4), (237, 73, 9), (236, 152, 66), (223, 126, 180), (4, 152, 96), (246, 215, 59), (4, 128, 206), (156, 37, 127), (1, 65, 151), 
(1, 123, 56),(229, 78, 32), (228, 169, 190), (117, 187, 156)]


turtle.colormode(255)
hadi = turtle.Turtle()
hadi.hideturtle()
hadi.speed(10)
hadi.penup()

current_y = -320
def draw_it():

    global current_y
    
    for i in range(20):
        hadi.setposition(-320,current_y)
        for i in range(16):
            hadi.dot(20,random.choice(colors))
            hadi.forward(50)

        
       
        current_y += 50







draw_it()