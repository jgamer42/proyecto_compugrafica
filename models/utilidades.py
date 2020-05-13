import random
from .enemigo2 import Enemigo2
from .enemigo1 import Enemigo1
from .asteroide1 import Asteroide1
def recorte_imagen(sabana,dimensiones,numero_frames):
        animacion = []
        for c in range(numero_frames):
            cuadro = sabana.subsurface(dimensiones[0]*c,0,dimensiones[0],dimensiones[1])
            animacion.append(cuadro)
        return (animacion)
    
def animar(frame_actual,numero_frames):
        if frame_actual < (numero_frames - 1):
            frame_actual = frame_actual + 1
        else:
            frame_actual = 0
        return(frame_actual)

def generar_enemigos(enemigos,balas_enemigos):
    for i in range(4):
        posx = random.randint(10,200)
        posy = random.randint(10,200)
        direccion = random.choice([-1,1])
        enemigo = Enemigo2([posx,posy],direccion,100)
        enemigos.add(enemigo)
    for i in range(8):
        posx = random.randint(10,200)
        posy = random.randint(10,200)
        direccion = random.choice([-1,1])
        enemigo = Enemigo1([posx,posy],direccion,balas_enemigos,100)
        enemigos.add(enemigo)
    
def generar_asteroides(asteroides):
    asteroide = Asteroide1([50,50])
    asteroides.add(asteroide)

