import pygame
import ambiente
import random

from models import constantes
from models.jugador import Jugador
from models.enemigo1 import Enemigo1
from models.enemigo2 import Enemigo2
from models.asteroide1 import Asteroide1

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([constantes.ANCHO,constantes.ALTO])
    reloj = pygame.time.Clock()
    jugador = Jugador([340,400])
    jugadores = pygame.sprite.Group()
    jugadores.add(jugador)
    enemigos = pygame.sprite.Group()
    balas_enemigos = pygame.sprite.Group()
    balas_jugador = pygame.sprite.Group()
    PantInit = pygame.image.load("./Sprites/UniversePantInit.png")
    LogoPantInit = pygame.image.load("./Sprites/LogoPantInit.png")
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
    asteroide = Asteroide1([50,50])
    asteroides = pygame.sprite.Group()
    asteroides.add(asteroide)

    niveles = [True,True,True,True,True]
    en_juego = False

    #Pantalla de inicio
    while((not en_juego) and niveles[0]):
        ventana.blit(PantInit, [0,0])
        ventana.blit(LogoPantInit, [180,90])
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                #jugador.controles(evento,balas_jugador)
                if evento.key == pygame.K_SPACE:
                    niveles[0] = False
            #if evento.type == pygame.KEYUP:
                #if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                    
                    '''jugador.frenar()
        elementos_dibujar =  [balas_enemigos,balas_jugador,jugadores,enemigos,asteroides]
        elementos_borrar = [balas_enemigos,balas_jugador,asteroides]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.MORADO)'''

    #Nivel 1
    while((not en_juego) and niveles[1]):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                jugador.controles(evento,balas_jugador)
                if evento.key == pygame.K_SPACE:
                    niveles[1] = False
            if evento.type == pygame.KEYUP:
                jugador.frenar()
        elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides]
        elementos_borrar = [balas_enemigos,balas_jugador]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.BLANCO)

    #Nivel 2
    while((not en_juego) and niveles[2]):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                jugador.controles(evento,balas_jugador)
                if evento.key == pygame.K_SPACE:
                    niveles[2] = False
            if evento.type == pygame.KEYUP:
                if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                    jugador.frenar()

        elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides]
        elementos_borrar = [balas_enemigos,balas_jugador]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.AZUL)

    #Nivel 3
    while((not en_juego) and niveles[3]):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                jugador.controles(evento,balas_jugador)
                if evento.key == pygame.K_SPACE:
                    niveles[3] = False
            if evento.type == pygame.KEYUP:
                if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                    jugador.frenar()

        elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides]
        elementos_borrar = [balas_enemigos,balas_jugador]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.NARANJA)

    #fin de juego
    while((not en_juego) and niveles[4]):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                jugador.controles(evento,balas_jugador)
                if evento.key == pygame.K_SPACE:
                    niveles[4] = False
            if evento.type == pygame.KEYUP:
                if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                    jugador.frenar()
        elementos_dibujar = [balas_enemigos,balas_jugador,jugadores]
        elementos_borrar = [balas_enemigos,balas_jugador]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.ROJO)
