import time
import turtle

t=turtle.Turtle()
# speed is b.w 1 and 10 
time.sleep(2)
t.speed(1)
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()