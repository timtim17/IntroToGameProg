# Austin Jenchi
# 2/20/2015
# 8th Period
# Circle

import turtle
from random import randint

r = 0
g = 0
b = 0

my_pretty = turtle.Turtle()
screen = turtle.Screen()

my_pretty.shape('turtle')
my_pretty.speed(10)
my_pretty.width(10)

screen.colormode(255)

while True:
    my_pretty.forward(1)
    my_pretty.left(1)

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

turtle.mainloop()