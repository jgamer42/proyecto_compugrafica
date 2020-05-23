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
        self.animacion = util.recorte_imagen(sabana,[80,70],8)
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.type = "agujero"
        self.direccion = direccion

    def animar(self):
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = self.posActual[0]
        self.rect.y = self.posActual[1]

    def update(self):
        self.frame = util.animar(self.frame,8)
        self.animar()
        super().update()
