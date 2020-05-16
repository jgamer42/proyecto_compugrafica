import random
from .enemigo2 import Enemigo2
from .enemigo1 import Enemigo1
from .asteroide1 import Asteroide1

def recorte_imagen(sabana,size,frames,filas=1):
    '''
    sabana: imagen completa
    size: tamaño del que desea el cuadrado
    frames: cantidad de columnas
    filas: cantidad de filas, si no es una matriz no requiere valor
    '''
    animacion = []
    animacion2 = []
    if filas == 1:
        for c in range(frames):
            cuadro = sabana.subsurface(size[0]*c,0,size[0],size[1])
            animacion.append(cuadro)
        return animacion
    elif filas > 1:
        filas -= 1
        for f in range(filas):
            for c in range(frames):
                cuadro = sabana.subsurface(size[0]*c,size[1]*f,size[0],size[1])
                animacion.append(cuadro)
            animacion2.append(animacion)
        return animacion2

def animar(frame_actual,numero_frames):
        if frame_actual < (numero_frames - 1):
            frame_actual = frame_actual + 1
        else:
            frame_actual = 0
        return(frame_actual)

def generar_enemigos(enemigos):
    for i in range(1):
        posx = random.randint(10,200)
        posy = random.randint(10,200)
        direccion = random.choice([-1,1])
        enemigo = Enemigo2([posx,posy],direccion,100)
        enemigos.add(enemigo)
    for i in range(1):
        posx = random.randint(10,200)
        posy = random.randint(10,200)
        direccion = random.choice([-1,1])
        enemigo = Enemigo1([posx,posy],direccion,10)
        enemigos.add(enemigo)

def generar_asteroides(asteroides):
    asteroide = Asteroide1([50,-100])
    asteroides.add(asteroide)
