#Equipo 12
#Isaac Jacinto Ruiz A01658578
#Klaus Manuel Cedillo Arreondo A01653257

from turtle import *
from random import randrange
from freegames import square, vector
import random


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colores =['blue','green','pink','brown','purple']

snakeColor = random.choice([i for i in colores])
comidaColor = random.choice([j for j in colores if j != snakeColor ])

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    #head = snake[-1].copy()
    #head.move(aim)
    head = snake[-1].copy() # posición antes de moverse
    head.move(aim) # posición después de movimiento
    food.move(vector(random.choice([-10, 0, 10]), random.choice([-10, 0, 10]))) # asignación de posiciones random comida
    
    
    #señal rojo si choca
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    #Limites comida
    elif not inside(food):
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, comidaColor)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()