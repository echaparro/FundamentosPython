import turtle
import time


#Linea punteada 1
espacio =10
for i in range(10):
    turtle.forward(espacio)
    turtle.penup()
    turtle.forward(espacio)
    turtle.pendown()

#Se baja el cursor y se crea una nueva instancia de Turtle
t = turtle.Turtle()
t.penup()
t.goto(0, -100)
t.pendown()

#Linea punteada creciendo
espacio =8
for i in range(10):
    espacio= espacio+2
    t.forward(espacio)
    t.penup()
    t.forward(espacio)
    t.pendown()


time.sleep(5)
