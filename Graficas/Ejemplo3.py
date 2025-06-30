import turtle as t
import math
import time

x= -2*(math.pi)
A=100
b=100
c=0
d=0

period =(2*(math.pi)/b)
Y=A*(math.sin((period*x-c)+d))
t.penup()
t.goto(x,Y)
t.pendown()
x=(-23*(math.pi)/12)
while x!= 2*(math.pi):
    Y=A*(math.sin((period *x-c)+d))
    t.goto(x,Y)
    x=x+((math.pi)/12)

time.sleep(5)
