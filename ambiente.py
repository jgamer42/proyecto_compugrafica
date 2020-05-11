import pygame
from models import constantes

def ciclo_de_juego(ventana,elementos,reloj,color):
    ventana.fill(color)
    for elemento in elementos:
        elemento.draw(ventana)
        elemento.update()
    pygame.display.flip()
    reloj.tick(20)

def protector_memoria(elementos):
    for elemento in elementos:
        for e in elemento:
            if(e.rect.bottom <= 0) or (e.rect.top > constantes.ALTO):
                print("borrado")
                elemento.remove(e)
            if(e.rect.x <= 0) or (e.rect.x > constantes.ANCHO):
                elemento.remove(e)
