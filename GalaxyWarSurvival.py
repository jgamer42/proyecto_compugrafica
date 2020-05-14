import pygame
import ambiente
import random

from models import constantes
from models.jugador import Jugador
from models.enemigo1 import Enemigo1
from models.enemigo2 import Enemigo2
from models.asteroide1 import Asteroide1
from models import utilidades

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init() #Inicia el mezclador de música
    ventana = pygame.display.set_mode([constantes.ANCHO,constantes.ALTO])
    reloj = pygame.time.Clock()
    jugador = Jugador([340,400])
    niveles = [True,True,True,True,True]
    en_juego = [True]

    jugadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    balas_enemigos = pygame.sprite.Group()
    balas_jugador = pygame.sprite.Group()
    asteroides = pygame.sprite.Group()
    jugadores.add(jugador)

    music_intro = pygame.mixer.Sound('./Sounds/Brave Pilots (Menu Screen).ogg')

    PantInit = pygame.image.load("./Sprites/fondos/UniversePantInit.png")
    LogoPantInit = pygame.image.load("./Sprites/fondos/LogoPantInit.png")
    sabana_game_over = pygame.image.load("./Sprites/fondos/SpriteGameOver.png")
    GameOver = utilidades.recorte_imagen(sabana_game_over,[765,1000],2)
    estado = 0
    cargar = GameOver[estado]

    utilidades.generar_enemigos(enemigos,balas_enemigos)
    utilidades.generar_asteroides(asteroides)

    while (en_juego[0]):
        #Pantalla de inicio
        music_intro.set_volume(0.1) #float, valores entre 0 y 1
        music_intro.play(-1)

        while (niveles[0] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,niveles,estado,0,en_juego)
            if (not niveles[0]):
                music_intro.stop()
            ventana.blit(PantInit, [0,0])
            ventana.blit(LogoPantInit, [180,90])
            pygame.display.flip()

        #Nivel 1
        while (niveles[1] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,niveles,estado,1,en_juego)
                jugador.controles(evento,balas_jugador)
            elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides,enemigos]
            elementos_borrar = [balas_enemigos,balas_jugador]
            ambiente.protector_memoria(elementos_borrar)
            ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.BLANCO)

        #Nivel 2
        while (niveles[2] and en_juego[0]):
            for evento in pygame.event.get():
                jugador.controles(evento,balas_jugador)
                ambiente.controles(evento,niveles,estado,2,en_juego)
            elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides]
            elementos_borrar = [balas_enemigos,balas_jugador]
            ambiente.protector_memoria(elementos_borrar)
            ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.AZUL)

        #Nivel 3
        while (niveles[3] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,niveles,estado,3,en_juego)
                jugador.controles(evento,balas_jugador)
            elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides]
            elementos_borrar = [balas_enemigos,balas_jugador]
            ambiente.protector_memoria(elementos_borrar)
            ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.NARANJA)

        #fin de juego
        niveles[4] = True
        while (niveles[4] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,niveles,estado,4,en_juego)
                if evento.type == pygame.KEYDOWN:
                    if (evento.key == pygame.K_SPACE):
                        if(estado == 0):
                            niveles[4] = False
                            en_juego = False
                        elif(estado == 1):
                            niveles[0] = True
                            niveles[1] = True
                            niveles[2] = True
                            niveles[3] = True
                            niveles[4] = False
                    if (evento.key == pygame.K_RIGHT):
                        estado = 1
                    if (evento.key == pygame.K_LEFT):
                        estado = 0
            cargar=GameOver[estado]
            ventana.fill(constantes.NEGRO)
            ventana.blit(cargar, [0,0])
            pygame.display.flip()
