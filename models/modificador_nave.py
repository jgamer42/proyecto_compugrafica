import pygame
from .bloque_base import Bloque_base
from . import constantes

class Modificador_n(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.image = pygame.image.load("./Sprites/modificadores/ModificadorNave.png")
        self.rect = self.image.get_rect()
        self.velx = 5
        self.vely = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "modificador_nave"

    def update(self):
        self.rect.y = self.rect.y + self.vely
        self.rect.x = self.rect.x + self.velx
