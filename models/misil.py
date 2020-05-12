from .bala_base import Bala_base
from . import utilidades
import pygame
#Cambios realizados
#1. se adapto para recortar una imagen o otra segun quien dispara el misil
class Misil(Bala_base):

    def __init__(self,pos,mod):
        super().__init__(pos,mod)
        pos_x = self.rect.x
        pos_y = self.rect.y
        sabana = None
        if(mod > 0):
            sabana = pygame.image.load("./Sprites/SpriteEnemyMisil_I.png")
        else:
            sabana = pygame.image.load("./Sprites/SpritePlayerMisil_I.png")
        self.animacion = utilidades.recorte_imagen(sabana,[19,88])
        self.frame = 0
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
