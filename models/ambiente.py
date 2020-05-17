import pygame
from models import constantes
from models.misil import Misil
from . import jugador
from . import utilidades as util


alarma_disparo_enemigo1 = False
alarma_colision_muro = True
alarma_gameover = False
origen_disparo_enemigo =None

pygame.mixer.init()
boom = pygame.mixer.Sound("./Sounds/boom.wav")

fondo = pygame.image.load("./Sprites/Background.png")
ambiente = pygame.image.load("./Sprites/Gui/Ambiente.png")
vidas = pygame.image.load("./Sprites/Gui/SpriteVidas.png")
sabana_salud = pygame.image.load("./Sprites/Gui/SpriteSalud.png")
salud = util.recorte_imagen(sabana_salud,[80,30],4)


def ciclo_de_juego(ventana,elementos,reloj,color,niveles):
    global alarma_gameover
    if(alarma_gameover):
        print("entro")
        niveles[0] = False
        niveles[1] = False
        niveles[2] = False
        niveles[3] = False
        niveles[4] = True
    else:
        ventana.fill(color)
        ventana.blit(fondo,[0,0])
        for elemento in elementos:
            elemento.draw(ventana)
            elemento.update()
        cargar_gui(ventana)
        pygame.display.flip()
        reloj.tick(constantes.NUMERO_FPS)

def cargar_gui(ventana):
    ventana.blit(ambiente,[0,0])
    ventana.blit(vidas,[500,0])
    ventana.blit(salud[0],[655,0])


def protector_memoria(elementos):
    for elemento in elementos:
        for e in elemento:
            if(e.type == "asteroide"):
                if(e.rect.y > constantes.ALTO):
                    elemento.remove(e)
                    print("asteroide limpiado")
            else:
                if(e.rect.bottom <= 0) or (e.rect.top > constantes.ALTO):
                    elemento.remove(e)
                if(e.rect.x <= 0) or (e.rect.x > constantes.ANCHO):
                    elemento.remove(e)

def controles(evento,niveles,estado,nivel,en_juego,jugador=None):
    global alarma_gameover
    if(evento.type == pygame.KEYDOWN):
        if (nivel==4):
            if (evento.key == pygame.K_SPACE):
                if(estado[0] == 0):
                    en_juego[0] = False
                    niveles[4] = False
                elif(estado[0] == 1):
                    alarma_gameover = False
                    niveles[0] = True
                    niveles[1] = True
                    niveles[2] = True
                    niveles[3] = True
                    niveles[4] = False
            if (evento.key == pygame.K_RIGHT):
                estado[0] = 1
            if (evento.key == pygame.K_LEFT):
                estado[0] = 0
        else:
            if (evento.key == pygame.K_SPACE):
                niveles[nivel]=False
    if evento.type == pygame.QUIT:
        en_juego[0] = False

def gestionar_disparo_enemigo(balas_enemigos):
    global alarma_disparo_enemigo1
    if(alarma_disparo_enemigo1 == True):
        misil = Misil(origen_disparo_enemigo,1)
        balas_enemigos.add(misil)
        alarma_disparo_enemigo1=False

def gestionar_colision_jugador(jugador,lista_elementos_colisionables):
    for lista_colisiones in lista_elementos_colisionables:
        colisiones = pygame.sprite.spritecollide(jugador,lista_colisiones,True)
        for colision in colisiones:
            if (colision.type == "asteroide"):
                boom.play()
                jugador.salud = jugador.salud - colision.daño
