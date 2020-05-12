from .bala_base import Bala_base
from . import utilidades
import pygame
#Cambios realizados
#1. se cambio el nombre a misil
#2. la funcion recortar imagen se puso en el archivo utilidades
#motivo: esto porque dicha funcion pude ser reusada en otros elementos del juego
class Misil(Bala_base):

    def __init__(self,pos):
        super().__init__(pos)
        pos_x = self.rect.x
        pos_y = self.rect.y
        sabana = pygame.image.load("./Sprites/SpritePlayerMisil_I.png")
        self.animacion = utilidades.recorte_imagen(sabana,[19,88])
        self.frame = 0
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

