import pygame
import ambiente
import random

from models import constantes
from models.bala_especifica import Bala_especifica
from models.jugador import Jugador
from models.enemigo_especifico import Enemigo_especifico

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([constantes.ANCHO,constantes.ALTO])
    reloj = pygame.time.Clock()
    jugador = Jugador([340,400])
    jugadores = pygame.sprite.Group()
    jugadores.add(jugador)
    enemigos = pygame.sprite.Group()
    for i in range(10):
        posx = random.randint(10,200)
        posy = random.randint(10,200)
        direccion = random.choice([-1,1])
        enemigo = Enemigo_especifico([posx,posy],direccion)
        enemigos.add(enemigo)

    balas_enemigos = pygame.sprite.Group()
    balas_jugador = pygame.sprite.Group()
    niveles = [True,True,True,True,True]
    en_juego = False

    #Pantalla de inicio
    while((not en_juego) and niveles[0]):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                jugador.controles(evento)
                if evento.key == pygame.K_SPACE:
                    niveles[0] = False
                if evento.key == pygame.K_z:
                    bala = Bala_especifica([jugador.rect.x,jugador.rect.y])
                    balas_jugador.add(bala)
            if evento.type == pygame.KEYUP:
                if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                    jugador.frenar()
        elementos_dibujar =  [balas_enemigos,balas_jugador,jugadores,enemigos]
        elementos_borrar = [balas_enemigos,balas_jugador]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.MORADO)

    #Nivel 1
    while((not en_juego) and niveles[1]):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                jugador.controles(evento)
                if evento.key == pygame.K_SPACE:
                    niveles[1] = False
            if evento.type == pygame.KEYUP:
                jugador.frenar()

        elementos_dibujar = [balas_enemigos,balas_jugador,jugadores]
        elementos_borrar = [balas_enemigos,balas_jugador]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.BLANCO)

    #Nivel 2
    while((not en_juego) and niveles[2]):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                jugador.controles(evento)
                if evento.key == pygame.K_SPACE:
                    niveles[2] = False
            if evento.type == pygame.KEYUP:
                if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                    jugador.frenar()

        elementos_dibujar = [balas_enemigos,balas_jugador,jugadores]
        elementos_borrar = [balas_enemigos,balas_jugador]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.AZUL)

    #Nivel 3
    while((not en_juego) and niveles[3]):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                jugador.controles(evento)
                if evento.key == pygame.K_SPACE:
                    niveles[3] = False
            if evento.type == pygame.KEYUP:
                if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                    jugador.frenar()

        elementos_dibujar = [balas_enemigos,balas_jugador,jugadores]
        elementos_borrar = [balas_enemigos,balas_jugador]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.NARANJA)

    #fin de juego
    while((not en_juego) and niveles[4]):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = True
            if evento.type == pygame.KEYDOWN:
                jugador.controles(evento)
                if evento.key == pygame.K_SPACE:
                    niveles[4] = False
            if evento.type == pygame.KEYUP:
                if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                    jugador.frenar()

        elementos_dibujar = [balas_enemigos,balas_jugador,jugadores]
        elementos_borrar = [balas_enemigos,balas_jugador]
        ambiente.protector_memoria(elementos_borrar)
        ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.ROJO)
