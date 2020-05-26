import pygame
import random
from . import constantes
from .bloque_base import Bloque_base
from . import ambiente
from . import utilidades as util

class Planeta(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.frame = 0
        self.type = "planeta"
        sabana = pygame.image.load("./Sprites/bloques/Planeta1.png")
        self.animacion = util.recorte_explosion(sabana,[72,72],5,4)
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.frame = util.animar(self.frame,19)
        self.image = self.animacion[self.frame]
        super().update()
