# Austin Jenchi
# 2/23/2015
# 8th Period
# Week 5

import turtle
from time import sleep
from random import randint

scr = turtle.Screen()
scr.colormode(255)
scr.title("Week 5")

t = turtle.Turtle()
t.color((0, 200, 0), (255, 0, 0))
t.width(10)
t.shape('turtle')
t.speed(1)

def drawExNum(exNum):
    t.clear()
    t.penup()
    t.goto(-150, 300)
    t.write("**********Exercise %d**********" % exNum, False, "center", ("Comic Sans MS", 24, "normal"))
    t.home()
    t.pendown()

drawExNum(1)

length = randint(50, 200)

t.begin_fill()

for i in range(6):
    t.forward(length)
    t.right(60)

t.end_fill()

t.hideturtle()
sleep(2.5)
t.showturtle()

drawExNum(2)

t.begin_fill()

width = 10

t.speed(0)

for i in range(360):
    if width <= 1:
        width += randint(0, 1)
    else:
        width += randint(-1, 1)

    t.width(width)
    t.forward(1)
    t.left(1)

t.end_fill()

t.hideturtle()
sleep(2.5)
t.showturtle()

t.speed(1)
drawExNum(3)

t.speed(1)
t.width(1)

angles = [160, -43, 270, -97, -43, 200, 940, 17, 86]
for angle in angles:
    t.left(angle)
    t.forward(100)

t.hideturtle()
sleep(2.5)
t.showturtle()

drawExNum(4)
t.width(10)

def drawW():
    t.color("indian red")

    t.penup()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.pendown()

    t.right(80)
    t.forward(100)
    t.left(160)
    t.forward(90)
    t.right(160)
    t.forward(90)
    t.left(160)
    t.forward(100)

def drawS():
    t.color("forest green")

    for i in range(4):
        t.forward(50)
        if i < 2:
            t.left(90)
        else:
            t.right(90)

    t.forward(50)

def drawP():
    t.color("dim gray")

    t.left(90)
    t.forward(100)
    for i in range(3):
        t.right(90)
        t.forward(50)

def drawSpace(numShapesDrawn):
    t.penup()
    t.home()
    t.forward(80 * numShapesDrawn)
    t.pendown()

drawW()
drawSpace(1)
drawS()
drawSpace(2)
drawP()
drawSpace(3)
drawS()

t.hideturtle()
sleep(2.5)
t.showturtle()

t.color(0, 200, 0)
drawExNum(5)

t.color("gold2", "gold2")
t.begin_fill()
for i in range(5):
    t.forward(80)
    t.left(144)
t.end_fill()

t.hideturtle()
sleep(2.5)
t.showturtle()

t.color(0, 200, 0)
drawExNum(6)
t.color("black")
t.stamp()

def drawMinute():
    t.penup()
    t.forward(80)
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(20)
    t.stamp()
    t.backward(110)

for i in range(12):
    drawMinute()
    t.right(30)

sleep(2.5)
t.color(0, 200, 0)
t.clear()
t.penup()
t.home()
t.write("THE END", True, "center", ("Comic Sans MS", 24, "normal"))
t.color("black")
sleep(2)
t.speed(1)
t.width(1)
t.pendown()
status = 0
for i in range(500):
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
sleep(5)
scr.bye()

# Homework Assignment: 