from .bala_base import Bala_base
from . import utilidades
import pygame
#cambios
#1. se encapsulo el metodo animar en el paquete de utilidades
# ver nueva logica de animacion en el update
class Misil_enemigo(Bala_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.posActual = pos
        pos_x = self.rect.x
        pos_y = self.rect.y
        sabana = pygame.image.load("./Sprites/balas/SpriteEnemyMisil_I.png")
        self.animacion = utilidades.recorte_imagen(sabana,[19,88],3)
        self.frame = 0
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.type = "misil_enemigo"
        self.daño = 130
        self.puntos = 6
