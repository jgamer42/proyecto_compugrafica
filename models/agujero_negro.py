import pygame
import random
from .bloque_base import Bloque_base
from . import ambiente
from . import utilidades as util

class Agujero_negro(Bloque_base):
    def __init__(self,pos,direccion):
        super().__init__(pos)
        self.frame = 0
        sabana = pygame.image.load("./Sprites/SpriteAgujeroNegro.png")
        self.animacion = util.recorte_imagen(sabana,[153,153],8)
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "agujero"
        self.direccion = direccion

    def update(self):
        self.frame = util.animar(self.frame,8)
        self.image = self.animacion[self.frame]
        super().update()
