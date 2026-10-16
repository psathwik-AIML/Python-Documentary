# set heading changes direction of turtle object 
import time
import turtle
pen=turtle.Turtle()

x=0
for i in range(6):
    x+=60
    time.sleep(2)
    pen.forward(100)
    time.sleep(2)
    pen.setheading(x)
turtle.done()