import pygame
from . import constantes
from models.misil_enemigo import Misil_enemigo
from . import utilidades as util
from . import variables

#alarmas
alarma_disparo_enemigo = False
alarma_gameover = False
alarma_planeta = False


def ciclo_de_juego(ventana,elementos,jugador):
    condicion_derrota()
    ventana.fill(constantes.NEGRO)
    cargar_gui(ventana,jugador)
    for elemento in elementos:
        elemento.draw(ventana)
        elemento.update()
    pygame.display.flip()
    variables.reloj.tick(constantes.NUMERO_FPS)


def condicion_derrota():
    if(alarma_gameover):
        variables.niveles[0] = False
        variables.niveles[1] = False
        variables.niveles[2] = True

def cargar_gui(ventana,jugador):
    seleccionar_pos_fondo()
    ventana.blit(variables.fondo,[0,variables.pos_fondo])
    ventana.blit(variables.saba_puntos,[0,0])
    pos_sprite_salud = seleccionar_sprite_salud(jugador)
    ventana.blit(variables.sprite_salud[pos_sprite_salud],[constantes.ANCHO-80,0])
    ventana.blit(variables.sprite_vidas[jugador.vidas-1],[constantes.ANCHO-196,0])

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
    if(variables.pos_fondo == 0):
        variables.pos_fondo = -1380
    else:
        variables.pos_fondo = variables.pos_fondo + constantes.VELOCIDAD_ENTORNO


def protector_memoria(elementos):
    for elemento in elementos:
        for e in elemento:
            if(e.type == "asteroide" or e.type == "agujero" or e.type =="planeta" or e.type == "satelite"):
                if(e.rect.y > constantes.ALTO):
                    elemento.remove(e)
            else:
                if(e.rect.bottom <= 0) or (e.rect.top > constantes.ALTO):
                    elemento.remove(e)
                if(e.rect.x <= 0) or (e.rect.x > constantes.ANCHO):
                    elemento.remove(e)

def controles(evento,nivel,en_juego,niveles,jugador=None,estado=None):
    global alarma_gameover
    if(evento.type == pygame.KEYDOWN):
        if (nivel==2):
            if (evento.key == pygame.K_SPACE):
                if(estado[0] == 0):
                    en_juego[0] = False
                    niveles[2] = False
                    print(nivel,en_juego,estado)
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
    global alarma_disparo_enemigo
    if(alarma_disparo_enemigo == True):
        misil = Misil_enemigo(variables.origen_disparo_enemigo)
        balas_enemigos.add(misil)
        alarma_disparo_enemigo=False

def gestionar_colision_jugador(jugador,lista_elementos_colisionables):
    for lista_colisiones in lista_elementos_colisionables:
        colisiones = pygame.sprite.spritecollide(jugador,lista_colisiones,True)
        for colision in colisiones:
            if (colision.type == "asteroide"):
                jugador.salud -= colision.daño
            elif colision.type == "misil":
                jugador.salud -= colision.daño

def gestionar_colision_enemigo(balas_jugador, lista_elementos_colisionables):
    for bala in balas_jugador:
        for lista_colisiones in lista_elementos_colisionables:
            colisiones = pygame.sprite.spritecollide(bala,lista_colisiones,False)
            for colision in colisiones:
                if colision.type == "enemigo1":
                    colision.salud = colision.salud - bala.daño 
                    if(colision.salud <= 0):
                        lista_colisiones.remove(colision)
                balas_jugador.remove(bala)
                if colision.type == "enemigo2":
                    colision.salud = colision.salud - bala.daño 
                    if(colision.salud <= 0):
                        lista_colisiones.remove(colision)
                balas_jugador.remove(bala)

def gestionar_elementos_ambientales(jugador,elementos_ambientales):
    for elemento in elementos_ambientales:
        if(elemento.type == "agujero"):
            logica_agujero_negro(elemento,jugador)
        if(elemento.type == "planeta"):
            logica_planeta(elemento)

def logica_agujero_negro(elemento,jugador):
    if(0 < elemento.rect.y < constantes.ALTO):
        if(elemento.rect.top< jugador.rect.y < elemento.rect.bottom):
            jugador.velx = 5*elemento.direccion

def logica_planeta(elemento):
    global alarma_planeta
    if(0 < elemento.rect.y < constantes.ALTO):
        alarma_planeta = True
    else:
        alarma_planeta = False