from .bala_base import Bala_base
from . import utilidades
import pygame
#cambios
#1. se encapsulo el metodo animar en el paquete de utilidades
# ver nueva logica de animacion en el update
class Misil(Bala_base):

    def __init__(self,pos,mod):
        super().__init__(pos,mod)
        pos_x = self.rect.x
        pos_y = self.rect.y
        sabana = None
        if(mod > 0):
            sabana = pygame.image.load("./Sprites/balas/SpriteEnemyMisil_I.png")
        else:
            sabana = pygame.image.load("./Sprites/balas/SpritePlayerMisil_I.png")
        self.animacion = utilidades.recorte_imagen(sabana,[19,88])
        self.frame = 0
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        super().update()
        self.frame = utilidades.animar(self.frame,3)
        self.image = self.animacion[self.frame]   
