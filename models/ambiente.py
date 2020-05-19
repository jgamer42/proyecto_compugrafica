import pygame

from . import constantes
from models.misil import Misil
from . import utilidades as util


alarma_disparo_enemigo1 = False
alarma_colision_muro = True
alarma_gameover = False
origen_disparo_enemigo =None
posy_fondo = -1380
pygame.mixer.init()
boom = pygame.mixer.Sound("./Sounds/boom.wav")


fondo = pygame.image.load("./Sprites/Background.png")
ambiente = pygame.image.load("./Sprites/Gui/Ambiente.png")
sabana_vidas = pygame.image.load("./Sprites/Gui/SpriteVidas.png")
sabana_salud = pygame.image.load("./Sprites/Gui/SpriteSalud.png")
sprite_salud = util.recorte_imagen(sabana_salud,[80,30],6)
sprite_vidas = util.recorte_imagen(sabana_vidas,[116,30],3)


def ciclo_de_juego(ventana,elementos,reloj,niveles,jugador):
    global alarma_gameover
    condicion_derrota()
    ventana.fill(constantes.NEGRO)
    cargar_gui(ventana,jugador)
    for elemento in elementos:
        elemento.draw(ventana)
        elemento.update()
    pygame.display.flip()
    reloj.tick(constantes.NUMERO_FPS)


def condicion_derrota():
    if(alarma_gameover):
        print("entro")
        niveles[0] = False
        niveles[1] = False
        niveles[2] = True

def cargar_gui(ventana,jugador):
    global posy_fondo
    seleccionar_pos_fondo()
    ventana.blit(fondo,[0,posy_fondo])
    ventana.blit(ambiente,[0,0])
    pos_sprite_salud = seleccionar_sprite_salud(jugador)
    ventana.blit(sprite_salud[pos_sprite_salud],[constantes.ANCHO-80,0])
    ventana.blit(sprite_vidas[jugador.vidas-1],[constantes.ANCHO-196,0])

def seleccionar_sprite_salud(jugador):
    if(0 < jugador.salud < 430):
        return(4)
    elif(430 <= jugador.salud < 472):
        return(3)
    elif(472 <= jugador.salud < 715):
        return(2)
    elif(715 <= jugador.salud < 1000):
        return(1)
    else:
        return(0) 
        
def seleccionar_pos_fondo():
    global posy_fondo
    if(posy_fondo == 0):
        posy_fondo = -1380
    else:
        posy_fondo = posy_fondo + constantes.VELOCIDAD_ENTORNO


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
                    niveles[2] = False
                elif(estado[0] == 1):
                    alarma_gameover = False
                    niveles[0] = True
                    niveles[1] = True
                    niveles[2] = False
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
                jugador.salud -= colision.daño
            elif colision.type == "misil":
                jugador.salud -= colision.daño

#def gestionar_colision_enemigo(enemigo_base, )
