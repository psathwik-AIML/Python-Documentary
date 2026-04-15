import time
import turtle
t=turtle.Turtle()
for i in range(6):
    time.sleep(1)
    t.forward(100)
    t.stamp()
    t.left(60)

time.sleep(2)
t.clearstamps()

time.sleep(2)
t.goto(-240,40)
stamp_list=[]
for i in range(5):
    s=t.stamp()
    time.sleep(1)
    t.forward(100)
    t.left(90)
    stamp_list.append(s)
for i in range(5):
    time.sleep(1)
    t.clearstamp(stamp_list[i])

turtle.done()