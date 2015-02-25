# From http://commons.wikimedia.org/wiki/Koch_snowflake#Python

import turtle

scr = turtle.Screen()
scr.colormode(255)

t = turtle.Turtle()
t.color("black", "cyan3")
t.shape("turtle")
# t.width(5)
t.width(1)
t.speed(0)

koch_flake = "FRFRF"
iterations = 5

t.begin_fill()

for i in range(iterations):
    koch_flake = koch_flake.replace("F","FLFRFLF")

for move in koch_flake:
    if move == "F":
        t.forward(100.0 / (3 ** (iterations - 1)))
    elif move == "L":
        t.left(60)
    elif move == "R":
        t.right(120)

t.end_fill()

t.hideturtle()

turtle.mainloop()