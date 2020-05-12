import pygame
from .bloque_base import Bloque_base
from . import constantes
#cambios
#1 . se implemento comportamiento basico del primer asteroide
# FIXME: revisar como descargar solo cuando salga por el borde inferior de la pantalla

#2 sprite asteroide1

class Asteroide1(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.image = pygame.image.load("./Sprites/Asteroid.png")
        self.rect = self.image.get_rect()
        self.velx = 0
        self.vely = constantes.VELOCIDAD_ENTORNO
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect.y = self.rect.y + self.vely
        self.rect.x = self.rect.x + self.velx
