import pygame
from .bloque_base import Bloque_base
from . import constantes

class Modificador_b(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.image = pygame.image.load("./Sprites/modificadores/ModificadorMisil.png")
        self.rect = self.image.get_rect()
        self.velx = 0
        self.vely = constantes.VELOCIDAD_ENTORNO
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "modificador_bala"

    def update(self):
        self.rect.y = self.rect.y + self.vely
        self.rect.x = self.rect.x + self.velx
