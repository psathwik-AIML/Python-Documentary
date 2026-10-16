import time
import turtle

t=turtle.Turtle()
time.sleep(1)
for i in range(5):
    t.forward(100)
    t.right(90)
    print(f"x: {t.xcor()} y:{t.ycor()}")

turtle.done()