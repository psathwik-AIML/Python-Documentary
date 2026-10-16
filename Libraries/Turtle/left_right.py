import turtle 
import time

t=turtle.Turtle()

# square

for i in range(4):
    time.sleep(1)
    t.forward(200)
    time.sleep(1)
    t.left(90)

time.sleep(3)
t.right(90)
t.forward(100)
turtle.done()
