import pygame
from .bloque_base import Bloque_base
from . import constantes

class Asteroide1(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.image = pygame.image.load("./Sprites/bloques/Asteroid.png")
        self.rect = self.image.get_rect()
        self.velx = 0
        self.vely = constantes.VELOCIDAD_ENTORNO + 20
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "asteroide"
        self.daño = 2500
        self.salud = 1500
        self.puntos_impacto = 50
        self.puntos_destruir = 300

    def update(self):
        self.rect.y = self.rect.y + self.vely
        self.rect.x = self.rect.x + self.velx
