import time
import turtle
t=turtle.Turtle()
time.sleep(1)
t.goto(250,0)
t.home()
t.goto(-250,0)
t.home()
t.goto(0,250)
t.home()
t.goto(0,-250)
t.circle(250)
t.home()
turtle.done()