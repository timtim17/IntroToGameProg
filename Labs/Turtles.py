# Austin Jenchi
# 2/19/2015
# 8th Period
# Turtles

import turtle
from random import randint

r = 0
g = 0
b = 0

width = 10

my_pretty = turtle.Turtle()
screen = turtle.Screen()

my_pretty.shape('turtle')
my_pretty.speed(10)

screen.colormode(255)

# my_pretty.color(0, 200, 0)

i = 0

while True:
    my_pretty.forward(i)
    my_pretty.left(i)
    # my_pretty.width(width)
    my_pretty.width(1)

    if r <= 200:
        r += randint(0, 10)
    else:
        r = 0

    if g <= 200:
        g += randint(0, 10)
    else:
        g = 0

    if b <= 200:
        b += randint(0, 10)
    else:
        b = 0

    my_pretty.color(r, g, b)

    width += 0.01

    i += 1

turtle.mainloop()