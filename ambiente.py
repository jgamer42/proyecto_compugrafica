import pygame
from models import constantes

def ciclo_de_juego(ventana,elementos,reloj,color):
    ventana.fill(color)
    for elemento in elementos:
        elemento.draw(ventana)
        elemento.update()
    pygame.display.flip()
    reloj.tick(constantes.NUMERO_FPS)

def protector_memoria(elementos):
    for elemento in elementos:
        for e in elemento:
            if(e.rect.bottom <= 0) or (e.rect.top > constantes.ALTO):
                elemento.remove(e)
            if(e.rect.x <= 0) or (e.rect.x > constantes.ANCHO):
                elemento.remove(e)

def controles(evento,niveles,estado,nivel,en_juego):
    if(evento.type == pygame.KEYDOWN):
        if (nivel==4):
            pass
        else:
            if (evento.key == pygame.K_SPACE):
                niveles[nivel]=False
    if evento.type == pygame.QUIT:
        en_juego[0] = False
            
