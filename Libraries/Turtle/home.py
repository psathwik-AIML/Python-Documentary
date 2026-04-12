# home function makes turtle object to move to start position 
import time
import turtle

pen=turtle.Turtle()
time.sleep(1)
pen.goto(-50,100)
time.sleep(1)
pen.goto(-100,0)
time.sleep(1)
pen.home()
turtle.done()