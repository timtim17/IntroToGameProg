# Austin Jenchi
# 2/20/2015
# 8th Period
# Turtle AI

import turtle
from random import randint

screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor("sandy brown")
# screen.bgpic("sand.gif")

t = turtle.Turtle()
t.shape('turtle')
t.speed(1)
t.color(0, 200, 0)
t.left(90)
t.status = 0

while True:
    for t in screen.turtles():
        t.forward(1)

        if t.status == 0:
            t.left(10)
            t.status = 1
        elif t.status == 1:
            t.right(10)
            t.status = 2
        elif t.status == 2:
            t.right(10)
            t.status = 3
        elif t.status == 3:
            t.left(10)
            t.status = 0


        randomint = randint(1, 100)
        if randomint > 75:
            t.right(randint(10, 50))
        elif randomint > 50:
            t.left(randint(10, 50))

turtle.mainloop()