import pygame
import random
from models import ambiente
from models import constantes
from models import utilidades
from models.jugador import Jugador
from models.enemigo1 import Enemigo1
from models.enemigo2 import Enemigo2
from models.asteroide1 import Asteroide1
from models.generador_asteroides import Generador_asteroides
from models.satelite import Satelite
from models.agujero_negro import Agujero_negro
from models.planeta import Planeta
from models.variables import *

#cambios
# 1. creado el generador de asteroides
# 2. organizado la paqueteria de los sprites
# 3. añadida funcionalidad del generador de asteroides
# 4. reparada colision asteroides
# 5. se bajaron los puntos por impactar el asteroide para prevenir bugs
# BUGS
# 1. El jugador solo puede ganar 999 puntos (prueba ponerl 1000 al jugado desde el inicio)
# el error esta en ambiente , en la funcion dibujar puntos
if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    ventana = pygame.display.set_mode([constantes.ANCHO,constantes.ALTO])

    agujero = Agujero_negro([0,-100],constantes.DERECHA)
    planeta = Planeta([50,-200])
    jugador = Jugador([340,620])
    satelite = Satelite([100,100])
    generador_asteroides = Generador_asteroides([50,50])

    elementos_ambientales.add(agujero)
    elementos_ambientales.add(planeta)
    jugadores.add(jugador)
    satelites.add(generador_asteroides)
    satelites.add(satelite)
    utilidades.generar_enemigos(enemigos)

    niveles = [True,True,True]
    en_juego = [True]
    estado = [0]

    while en_juego[0]:
        #Pantalla de inicio
        music_intro.set_volume(0.4)
        music_intro.play(-1)
        while (niveles[0] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,0,en_juego,niveles)
            ventana.blit(PantInit, [0,0])
            ventana.blit(LogoPantInit, [116,150])
            pygame.display.flip()
        music_intro.stop()

        #Nivel 1CD
        music_juego.set_volume(0.5)
        music_juego.play(-1)
        while (niveles[1] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,1,en_juego,niveles)
                jugador.controles(evento,balas_jugador)
            ambiente.gestionar_elementos_ambientales(jugador,elementos_ambientales)
            ambiente.gestionar_disparo_enemigo(balas_enemigos)
            ambiente.gestionar_generacion_asteroide(asteroides)
            elementos_colisionables = [balas_enemigos,enemigos,asteroides]
            ambiente.gestionar_colision_jugador(jugador,elementos_colisionables)
            ambiente.gestionar_colision_enemigo(balas_jugador,elementos_colisionables,jugador,ventana)
            elementos_dibujar = [balas_enemigos,balas_jugador,jugadores,enemigos,satelites,elementos_ambientales,asteroides]
            elementos_borrar = [balas_enemigos,balas_jugador,elementos_ambientales,satelites,asteroides]
            ambiente.protector_memoria(elementos_borrar)
            ambiente.ciclo_de_juego(ventana,elementos_dibujar,jugador,niveles,enemigos,jugadores)
        music_juego.stop()

        #fin de juego
        music_out.set_volume(0.4)
        music_out.play(-1)
        while (niveles[2] and en_juego[0]):
            for evento in pygame.event.get():
                ambiente.controles(evento,2,en_juego,niveles,jugador,estado)
            ventana.fill(constantes.NEGRO)
            cargar = GameOver[estado[0]]
            ventana.blit(cargar, [0,0])
            pygame.display.flip()
        music_out.stop()
