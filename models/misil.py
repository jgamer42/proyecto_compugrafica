from .bala_base import Bala_base
from . import utilidades
import pygame

class Misil(Bala_base):

    def __init__(self,pos):
        super().__init__(pos)
        pos_x = self.rect.x
        pos_y = self.rect.y
        sabana = pygame.image.load("./Sprites/balas/SpritePlayerMisil_I.png")
        self.animacion = utilidades.recorte_imagen(sabana,[19,88],3)
        self.frame = 0
        self.vely = -50
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.type = "misil"
        self.daño = 130

    def update(self):
        super().update()
        self.frame = utilidades.animar(self.frame,3)
        self.image = self.animacion[self.frame]
