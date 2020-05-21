import pygame
import random
from . import constantes
from .bloque_base import Bloque_base
from . import ambiente

class Planeta(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.type = "planeta"
        self.image.fill(constantes.AZUL)
    
    def update(self):
        super().update()