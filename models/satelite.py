import pygame
import random
from .bloque_base import Bloque_base
from . import ambiente
from . import constantes

class Satelite(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.image = pygame.image.load("./Sprites/generadores/Satelite.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.generando = 0
        self.type = "satelite"

    def cant_mod(self):
        cantidad = [30,90,120]
        if self.generando in cantidad:
            self.generando += 1
            return 0
        else:
            self.generando += 1
            return self.generando

    def generar(self):
        generador = self.cant_mod()
        if(generador == 0):
            ambiente.alarma_generar_modif_b = True
            ambiente.alarma_generar_modif_n = True
            pos_modif_n_generado = random.randint(20,constantes.ANCHO-20)
            pos_modif_b_generado = random.randint(20,constantes.ANCHO-20)
            ambiente.origen_modif_b = [pos_modif_b_generado,self.rect.y]
            ambiente.origen_modif_n = [pos_modif_n_generado,self.rect.y]

    def update(self):
        self.generar()
        super().update()
