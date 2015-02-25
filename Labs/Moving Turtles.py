# Austin Jenchi
# 2/20/2015
# 8th Period
# Moving Turtles

# Austin Jenchi
# 2/19/2015
# 8th Period
# Turtles

import turtle

width = 10

screen = turtle.Screen()

screen.colormode(255)

my_pretty = turtle.Turtle()

my_pretty.shape('turtle')
my_pretty.speed(10)
my_pretty.color(0, 200, 0)

def forwards():
    my_pretty.fd(10)

def backwards():
    my_pretty.back(10)

def left():
    my_pretty.left(10)

def right():
    my_pretty.right(10)

screen.getcanvas().bind("<Up>", forwards())
screen.getcanvas().bind("<Down>", backwards)
screen.getcanvas().bind("<Left>", left)
screen.getcanvas().bind("<Right>", right)

screen.listen()

turtle.mainloop()