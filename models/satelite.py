import pygame
import random
from .bloque_base import Bloque_base
from . import ambiente

class Satelite(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.image = pygame.image.load("./Sprites/enemigos/Satelite.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "satelite"
        self.estado =True

    def generar(self):
        pass
    
    def update(self):
        self.generar()
        super().update()
