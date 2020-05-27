import pygame
import random
from .bloque_base import Bloque_base
from . import ambiente
from . import constantes

class Generador_asteroides(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.image = pygame.image.load("./Sprites/generadores/generador_asteroide.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0
        self.generando = False
        self.type = "generado_asteroide"

    def generar(self):
        generador = None
        if not(self.generando):
            generador = random.randint(0,50)
        if(generador == 0):
            ambiente.alarma_generar_asteroide = True
            pos_asteroide_generado = random.randint(20,constantes.ANCHO-20)
            ambiente.origen_asteroide = [pos_asteroide_generado,self.rect.y]

    def update(self):
        self.generar()
        super().update()
