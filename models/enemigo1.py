import pygame
import random
from .enemigo_base import Enemigo_base
from . import utilidades as util
from . import ambiente


class Enemigo1(Enemigo_base):
    def __init__(self,pos,direccion,agresividad):
        super().__init__(pos,direccion,agresividad)
        self.frame = 0
        sabana = pygame.image.load("./Sprites/enemigos/SpriteEnemyShip_I.png")
        self.animacion = util.recorte_imagen(sabana,[87,75],3,2)
        self.fila_animacion = 0
        self.image =  self.animacion[self.fila_animacion][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.atacando = False
        self.type = "enemigo1"
        self.salud = 500
        self.puntos_impacto = 10
        self.puntos_morir = 18

    def atacar(self):
        ataque = None
        if not(self.atacando):
            ataque = random.randint(0,self.agresividad)
        if(ataque == 0):
            ambiente.origen_disparo_enemigo = self.rect.center
            ambiente.alarma_disparo_enemigo = True

    def update(self):
        self.atacar()
        super().update()
        self.frame = util.animar(self.frame,3)
        self.cambio_animacion()
        self.image = self.animacion[self.fila_animacion][self.frame]

    def cambio_animacion(self):
        self.frame = util.animar(self.frame,3)
        if self.direccion > 0:
            self.fila_animacion = 0
        elif self.direccion < 0:
            self.fila_animacion = 1
