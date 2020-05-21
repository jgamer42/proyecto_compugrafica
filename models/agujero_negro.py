import pygame
import random
from .bloque_base import Bloque_base
from . import ambiente

class Agujero_negro(Bloque_base):
    def __init__(self,pos,direccion):
        super().__init__(pos)
        self.type = "agujero"
        self.direccion = direccion
    
    def update(self):
        super().update()