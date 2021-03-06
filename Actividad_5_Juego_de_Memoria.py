# 29/10/2021
# 09:42 am

# Juego memorama, cuenta cuantos intentos realizaste y detecta cuando completas el juego, dandote un mensaje de felicitaciones

# Modificado por:
# Gabriel Sebastián Garibay Dávila
# Daniel Evaristo Escalera Bonilla
# Francisco Cruz Vázquez
# Juan Carlos Martínez Zacarías
# Carmina López Palacios

# Se incluyo la librería string para crear el arreglo de los símbolos de las tarjetas
import string
from random import *
from turtle import *
from freegames import path


ima = 'bha.gif'
tiles = list(range(32)) * 2

# Se crea un nuevo arreglo con símbolos y letras que permiten una mayor diferenciación entre sí
tiles2 = ['#', '$', '%', '&', '?', '~']
tiles2.extend(list(string.ascii_uppercase))
tiles2 = tiles2 * 2

state = {'mark': None}
hide = [True] * 64
tapCount = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    # Se crea una variable global para guardar el número de veces que se inenta descubrir una parte de la imagen
    global tapCount
    # Aumento de variable e impresión
    tapCount = tapCount + 1
    print(tapCount)
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles2[mark] != tiles2[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    # Cuando todas las tarjetas hayan sido descubiertas se da un mensaje de "bien hecho"
    if(hide == [False]*64):
        print("all done")
        return
    
def draw():
    # Contador para los cuadros que se han revelado
    revealed = 0;
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(ima)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    
    # Cuenta cuantos cuadros se han revelado
    for count in range(64):
        if not hide[count]:
            revealed += 1
            # Si se revelaron todos escribe un mensaje de felicitaciones
            if revealed >= 63:
                goto(-125, -20)
                color('white')
                write('Felicidades', font=('Arial', 30, 'normal'))

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Se va a las coordenadas donde se dió clic y se imprime el símbolo de la tarjeta
        goto(x + 26, y + 7)
        color('black')
        write(tiles2[mark], font=('Arial', 30, 'normal'), align="center")

    update()
    ontimer(draw, 100)

shuffle(tiles2) # Los elementos del nuevo arreglo se mezclan para que pierdan su orden
setup(420, 420, 370, 0)
addshape(ima)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()