import pygame
import random
from .bloque_base import Bloque_base
from . import ambiente

class Satelite(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.image = pygame.image.load("./Sprites/enemigos/Satelite.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.generando = False
        self.type = "satelite"
        self.estado =True

    def generar(self):
        generador = None
        if not(self.generando):
            generador = random.randint(0,10)
        if(generador == 0):
            ambiente.alarma_generar_modif = True
            ambiente.origen_modif = self.rect.center
            print("Generar")

    def update(self):
        self.generar()
        super().update()
