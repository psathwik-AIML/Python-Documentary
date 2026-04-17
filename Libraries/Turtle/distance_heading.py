import time
import turtle
t=turtle.Turtle()

time.sleep(1)
x,y=t.position()
print(x,y)
t.goto(10,0)
time.sleep(1)
t.goto(10,10)
distance=t.distance(x,y)
print(distance)
turtle.done()