import turtle





hadi = turtle.Turtle()
moh = turtle.Screen()


def forward():
    hadi.forward(20)
def backward():
    hadi.backward(20)
def left():
    hadi.left(20)
def right():
    hadi.right(20)

def clearit():
    hadi.reset()
moh.listen()

moh.onkey(key ='w',fun=forward)
moh.onkey(backward,'s')
moh.onkey(left,'a')
moh.onkey(right,'d')
moh.onkey(clearit,'c')




moh.exitonclick()