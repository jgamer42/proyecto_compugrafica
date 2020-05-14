import pygame
import random
from .enemigo_base import Enemigo_base
from . import utilidades
from . import ambiente
#cambios
#1. se encapsulo el metodo animar en el paquete de utilidades
# ver nueva logica de animacion en el update
class Enemigo1(Enemigo_base):
    def __init__(self,pos,direccion,agresividad):
        super().__init__(pos,direccion,agresividad)
        self.frame = 0
        sabana = pygame.image.load("./Sprites/enemigos/SpriteEnemyShip_I.png")
        self.animacion = (utilidades.recorte_imagen(sabana,[62,95],3))
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.atacando = False

    def atacar(self):
        ataque = None
        if not(self.atacando):
            ataque = random.randint(0,self.agresividad)
        if(ataque == 0):
            ambiente.alarma_disparo_enemigo1 = True
            ambiente.origen_disparo_enemigo = self.rect.center
    def update(self):
        self.atacar()
        self.frame = utilidades.animar(self.frame,3)
        self.image = self.animacion[self.frame]
        super().update()
