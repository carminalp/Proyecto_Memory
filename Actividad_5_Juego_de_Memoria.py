import string
from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2

# Se crea un nuevo arreglo con símbolos y letras que permiten una mayor diferenciación entre sí
tiles2 = ['#', '$', '%', '&', '?', '~']
tiles2.extend(list(string.ascii_uppercase))
tiles2 = tiles2 * 2

state = {'mark': None}
hide = [True] * 64

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
    spot = index(x, y)
    mark = state['mark']

    #if mark is None or mark == spot or tiles[mark] != tiles[spot]:
    if mark is None or mark == spot or tiles2[mark] != tiles2[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles2[mark], font=('Arial', 30, 'normal'), align="center")

    update()
    ontimer(draw, 100)

#shuffle(tiles)
shuffle(tiles2) # Los elementos del nuevo arreglo se mezclan para que pierdan su orden
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()