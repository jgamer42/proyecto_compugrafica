import pygame
import random

from models import ambiente
from models import constantes
from models import utilidades
from models.jugador import Jugador
from models.enemigo1 import Enemigo1
from models.enemigo2 import Enemigo2
from models.asteroide1 import Asteroide1
from models.misil import Misil
from models.muro import Muro

#*CAMBIOS
#1. mecanica de morir terminada
#2. conflicto arreglados
#*
#*PENDIENTE
#1. hacer el cambio de sprite cada que se pierde vida
#2. hacer el cambio de sprite cada que se pierde durabilidad*
#NOTA: en este momento el jugador solo tiene una vida y
# 50 de durabilidad, esto con el fin de hacer pruebas ,
# si cambian los valores funciona correctamene

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    ventana = pygame.display.set_mode([constantes.ANCHO,constantes.ALTO])
    reloj = pygame.time.Clock()
    jugador = Jugador([340,620])
    niveles = [True,True,True]
    en_juego = [True]

    jugadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    balas_enemigos = pygame.sprite.Group()
    balas_jugador = pygame.sprite.Group()
    asteroides = pygame.sprite.Group()
    muros = pygame.sprite.Group()

    jugadores.add(jugador)
    muro = Muro([100,100])
    muros.add(muro)

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

    while en_juego[0]:
        #Pantalla de inicio
        music_intro.set_volume(0.4)
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
            elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,asteroides,enemigos,muros]
            elementos_borrar = [balas_enemigos,balas_jugador,asteroides]
            ambiente.protector_memoria(elementos_borrar)
            ambiente.ciclo_de_juego(ventana,elementos_dibujar,reloj,constantes.BLANCO,niveles,jugador)

        #fin de juego
        music_out.set_volume(0.4)
        music_out.play(-1)
        niveles[2] = True
        while (niveles[2] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,niveles,estado,4,en_juego,jugador)
            cargar=GameOver[estado[0]]
            ventana.fill(constantes.NEGRO)
            ventana.blit(cargar, [0,0])
            pygame.display.flip()
        music_out.stop()
