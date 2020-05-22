import pygame
from . import utilidades as util
from .enemigo_base import Enemigo_base
from . import constantes
import random
class Enemigo2(Enemigo_base):
    def __init__(self,pos,direccion,agresividad):
        super().__init__(pos,direccion,agresividad)
        self.frame = 0
        sabana = pygame.image.load("./Sprites/enemigos/SpriteEnemyBoomShip.png")
        self.animacion = util.recorte_imagen(sabana,[73,121],3)
        self.image =  self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.atacando = False
        self.posy_inicial = pos[1]
        self.agresividad = agresividad
        self.type = "enemigo2"
        self.daño = 1500
        self.salud = 100

    def atacar(self):
        ataque=None
        if not(self.atacando):
            ataque = random.randint(0,self.agresividad)
        if(ataque == 0):
            self.velx = 0
            self.vely = 60
            self.atacando = True

    def comportamiento_limites(self):
        if(self.atacando):
            if(self.rect.y > constantes.ALTO) and(self.vely >0):
                self.vely = -1*self.vely
            if(self.rect.y == self.posy_inicial) and (self.vely < 0):
                self.vely = 0
                self.velx = 20
                self.atacando = False
        super().comportamiento_limites()

    def update(self):
        self.atacar()
        super().update()
