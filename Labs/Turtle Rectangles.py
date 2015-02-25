# Austin Jenchi
# 2/23/2015
# 8th Period
# Turtle Rectangles

import turtle
from random import randint

scr = turtle.Screen()
scr.colormode(255)

t = turtle.Turtle()
t.shape("turtle")
t.pensize(10)
t.color(0, 200, 0)
t.speed(1)

while True:
    try:
        width = input("What will the width of the rectangle be? => ")
        break
    except NameError: pass

for i in range(2):
    t.forward(width)
    t.right(90)
    t.forward(width * 3)
    t.right(90)

t.penup()

status = 0

while True:
        t.forward(1)

        if status == 0:
            t.left(10)
            status = 1
        elif status == 1:
            t.right(10)
            status = 2
        elif status == 2:
            t.right(10)
            status = 3
        elif status == 3:
            t.left(10)
            status = 0


        randomint = randint(1, 100)
        if randomint > 75:
            t.right(randint(10, 50))
        elif randomint > 50:
            t.left(randint(10, 50))

turtle.mainloop()