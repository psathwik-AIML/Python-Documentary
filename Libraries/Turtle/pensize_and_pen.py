import time 
import turtle

t=turtle.Turtle()
screen=turtle.Screen()
# screen.bgcolor("black")
time.sleep(2)
t.pensize(3)
t.turtlesize(10)
# pen function 
t.pen(pendown=True,fillcolor="red",pensize=10)
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()