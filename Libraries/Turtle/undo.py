import time
import turtle
t=turtle.Turtle()
time.sleep(2)
for i in range(5):
    time.sleep(1)
    t.forward(100)
    t.left(90)
time.sleep(1)
for i in range(15):
    time.sleep(1)
    t.undo()
turtle.done()