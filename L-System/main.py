# Title:    Basic L-System Generater With Python & Turtle
# By:       Mehmet Yilmaz
# Date:     7-5-2020

# *Sources:
# 1) https://en.wikipedia.org/wiki/L-system
# 2) https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end
# 3) http://paulbourke.net/fractals/lsys/

from tkinter import *
from turtle import *
import turtle
import re

######################################
############# Parameters #############
######################################
title = "Classic_Sierpinski_Curve-Paul_Bourke-&-Chris_Wallace"
######################################
variables = ["X"]
######################################
moveForward = ["F"]
turnLeft = ["-"]
turnRight = ["+"]
######################################
start = ["F--XF--F--XF"]
rules = ["XF+F+XF--F--XF+F+X"]
angle = 45
n = 5
######################################
dis = 8
spd = 100000
seeDrawing = False
saveImage = True
hideArrow = True
startAngle = 45 # only turning left
######################################

def makeString(list):
    ans = ""
    for i in range(len(list)):
        ans = ans + list[i]
    return ans

def makeList(s):
    ans = []
    for i in range(len(s)):
        ans.append(str(s[i]))
    return ans

def getState(turtle):
    return turtle.heading(), turtle.position()

def restoreState(turtle, state):
    turtle.setheading(state[0])
    turtle.setposition(state[1][0], state[1][1])

for i in range(n):
    for p in range(len(variables)):
        v = variables[p]
        for z in range(len(start)):
            if(start[z] == v):
                start[z] = rules[p]
    temp = makeString(start)
    start = makeList(temp)

if(hideArrow):
    hideturtle()

if(seeDrawing == False):
    speed(spd)
    turtle.tracer(0, 0)

savedState = []
stack = []
left(startAngle)

for i in range(len(start)):
    key = start[i]
    if(moveForward.count(key)):
        forward(dis)
    elif(turnLeft.count(key)):
        left(angle)
    elif(turnRight.count(key)):
        right(angle)
    elif(key == "["):
        savedState = getState(turtle)
        stack.append(savedState)
    elif(key == "]"):
        turtle.penup()
        restoreState(turtle, stack[-1])
        stack.pop()
        turtle.pendown()

if(saveImage):
    title = re.sub("\s+", "_", title.strip()) + ".eps"
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file=str(title))

if(seeDrawing == False):
    turtle.update()

done()


