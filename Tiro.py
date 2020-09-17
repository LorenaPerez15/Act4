from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
#Da la señal que aparezca la bolita roja cuando se toca la pantalla
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 350) / 25
        speed.y = (y + 350) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()
#Dibuja los targets (puntos azules)
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
#Dibuja la bola (Bolita roja que golpea los targets)
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    #Movimiento y velocidad de targets
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1
#Movimiento y velocidad de pelotita roja
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
#Cuando el punto rojo golpea los targets, estos se eliminan
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            targets.clear()

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
