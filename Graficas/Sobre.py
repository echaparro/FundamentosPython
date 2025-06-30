import turtle
import time

# Dibujar el cuadrado
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# Linea 1 de la x
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(100, 100)

# Linea 2 de la x
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(100, 0)

# Triangulo
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(50, 150)
turtle.goto(100, 100)
turtle.goto(0, 100)

time.sleep(5)
