import turtle
import time

posponer = 0.1

wn = turtle.Screen()
wn.title("Juego Serpiente")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.color("white")
cabeza.goto(0,0)
cabeza.direction = "stop"

comida = turtle.Turtle()
comida.speed(0)
comida.shape("square")
comida.penup()
comida.color("white")
comida.goto(0,0)
comida.direction = "stop"

# Funciones
def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"
def right():
	cabeza.direction = "right"
def left():
	cabeza.direction = "left"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

while True:
    wn.update()

    mov()
    time.sleep(posponer)