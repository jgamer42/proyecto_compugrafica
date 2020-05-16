import pygame
from models import constantes
from models.misil import Misil
from . import jugador

alarma_disparo_enemigo1 = False
alarma_colision_muro = True
origen_disparo_enemigo =None

#necesitamos saber el tipo de colision que esta sucediendo para asi saber que tanta salud le quitamos al jugador

ambiente = pygame.image.load("./Sprites/ambiente/Ambiente.png")

def ciclo_de_juego(ventana,elementos,reloj,color):
    ventana.fill(color)
    for elemento in elementos:
        elemento.draw(ventana)
        elemento.update()
    ventana.blit(ambiente,[0,0])
    pygame.display.flip()
    reloj.tick(constantes.NUMERO_FPS)

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

def controles(evento,niveles,estado,nivel,en_juego):
    if(evento.type == pygame.KEYDOWN):
        if (nivel==4):
            if (evento.key == pygame.K_SPACE):
                if(estado[0] == 0):
                    en_juego[0] = False
                    niveles[4] = False
                elif(estado[0] == 1):
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
                 jugador.salud = 0
                 jugador.vidas -= 1
