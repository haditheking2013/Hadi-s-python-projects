from secrets import choice
import turtle
import random 


colors = ['medium blue','dark red','blue violet','orange','dark cyan','pink']
turtle.colormode(255)
hadi = turtle.Turtle()


def random_color():
       return (random.randint(0,255),random.randint(0,255),random.randint(0,255))


#for shape_range in range(3,11):
   # side_draw(shape_range)



def random_walk(num_of_moves):
    for i in range(num_of_moves):
        hadi.speed(10)
        hadi.pensize(15)
        hadi.pencolor(*random_color())
        hadi.forward(50)
        hadi.left(random.choice([90,180,270,0]))



def random_circle(num_of_turns):
    hadi.speed(100)
    for i in range(num_of_turns):
        hadi.pencolor(random_color())
        hadi.circle(100)
        hadi.left(5)


random_circle(72)
