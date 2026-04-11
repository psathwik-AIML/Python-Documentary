import turtle
import time

time.sleep(2)
t=turtle.Turtle()
# changing position of turtle object 
t.goto(110,33)
time.sleep(2)
t.setpos(130,33)
time.sleep(2)
t.setposition(50,24)
print(t.pos())
turtle.done()