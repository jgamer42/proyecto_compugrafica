import pygame
import random
from .enemigo_base import Enemigo_base
from .misil import Misil
from . import utilidades
#cambios
#1. agregadas funcionalidad de disparo
#2. sprite y animacion
class Enemigo1(Enemigo_base):
    def __init__(self,pos,direccion,lista_balas,agresividad):
        super().__init__(pos,direccion,agresividad)
        self.frame = 0
        sabana = pygame.image.load("./Sprites/SpriteEnemyShip_I.png")
        self.animacion = (utilidades.recorte_imagen(sabana,[62,95]))
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.lista_balas = lista_balas
        self.atacando = False

    def atacar(self):
        ataque = None
        if not(self.atacando):
            ataque = random.randint(0,self.agresividad)
        if(ataque == 0):
            bala = Misil(self.rect.center,1)
            self.lista_balas.add(bala)

    def update(self):
        self.animar()
        self.atacar()
        super().update()

    def animar(self):
        if self.frame < 2:
            self.frame = self.frame + 1
        else:
            self.frame = 0
        self.image = self.animacion[self.frame]
