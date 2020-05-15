import pygame
import random
from .bloque_base import Bloque_base
from . import ambiente

class Muro(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.type = "muro"
        self.estado =True

    def control_estado(self):
        cambio_estado = random.randrange(0,100)
        if(cambio_estado%3 == 0):
            self.estado = False
            ambiente.alarma_colision_muro = False
        if(cambio_estado%2 == 0):
            self.estado = True
            ambiente.alarma_colision_muro = True
    def update(self):
        self.control_estado()
        super().update()