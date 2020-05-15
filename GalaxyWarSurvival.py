import pygame
import random

from models import ambiente
from models import constantes
from models.jugador import Jugador
from models.enemigo1 import Enemigo1
from models.enemigo2 import Enemigo2
from models.asteroide1 import Asteroide1
from models.misil import Misil
from models import utilidades

#CAMBIOS
#1. se rediseño el sistema de disparo del enemigo (ver ambiente.py y enemigo1.py)
#2. se agrego el primer prototipo de sistema de colision (ver ambiente.py)
#3. se ordeno un poco los cambios previos de la musica
#4. se agrego el atributo typer a los misiles y al asteroide (ver clases respectivas)
#5. se agrego la forma de limpieza de asterorides (ver ambiente.py proteger_memoria)
if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
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

    music_out = pygame.mixer.Sound("./Sounds/Game Over.ogg")
    PantInit = pygame.image.load("./Sprites/fondos/UniversePantInit.png")
    LogoPantInit = pygame.image.load("./Sprites/fondos/LogoPantInit.png")
    sabana_game_over = pygame.image.load("./Sprites/fondos/SpriteGameOver.png")
    GameOver = utilidades.recorte_imagen(sabana_game_over,[768,690],2)
    estado = [0]
    cargar = GameOver[estado[0]]

    utilidades.generar_enemigos(enemigos)
    utilidades.generar_asteroides(asteroides)

    while (en_juego[0]):
        #Pantalla de inicio
        music_intro.set_volume(0.3)
        music_intro.play(-1)
        while (niveles[0] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,niveles,estado,0,en_juego)
            ventana.blit(PantInit, [0,0])
            ventana.blit(LogoPantInit, [180,90])
            pygame.display.flip()
        music_intro.stop()

        #Nivel 1
        while (niveles[1] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,niveles,estado,1,en_juego)
                jugador.controles(evento,balas_jugador)
            ambiente.gestionar_disparo_enemigo(balas_enemigos)
            elementos_colisionables = [balas_enemigos,enemigos,asteroides]
            ambiente.gestionar_colision_jugador(jugador,elementos_colisionables)
            elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides,enemigos]
            elementos_borrar = [balas_enemigos,balas_jugador,asteroides]
            ambiente.protector_memoria(elementos_borrar)
            ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.BLANCO)

        #Nivel 2
        while (niveles[2] and en_juego[0]):
            for evento in pygame.event.get():
                jugador.controles(evento,balas_jugador)
                ambiente.controles(evento,niveles,estado,2,en_juego)
            ambiente.gestionar_disparo_enemigo(balas_enemigos)
            elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides]
            elementos_borrar = [balas_enemigos,balas_jugador,asteroides]
            ambiente.protector_memoria(elementos_borrar)
            ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.AZUL)

        #Nivel 3
        while (niveles[3] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,niveles,estado,3,en_juego)
                jugador.controles(evento,balas_jugador)
            ambiente.gestionar_disparo_enemigo(balas_enemigos)
            elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides]
            elementos_borrar = [balas_enemigos,balas_jugador,asteroides]
            ambiente.protector_memoria(elementos_borrar)
            ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.NARANJA)

        #fin de juego
        music_out.set_volume(0.3)
        music_out.play(-1)
        niveles[4] = True
        while (niveles[4] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,niveles,estado,4,en_juego)
            cargar=GameOver[estado[0]]
            ventana.fill(constantes.NEGRO)
            ventana.blit(cargar, [0,0])
            pygame.display.flip()
        music_out.stop()
