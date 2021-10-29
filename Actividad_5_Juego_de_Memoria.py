from random import *
from turtle import *
from freegames import path


ima = 'bha.gif'
tiles = list(range(32)) * 2
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
    global tapCount
    tapCount = tapCount + 1
    print(tapCount)
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
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
        goto(x + 26, y + 7)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align="center")

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(ima)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()