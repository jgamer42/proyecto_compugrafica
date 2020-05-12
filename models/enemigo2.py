from .enemigo_base import Enemigo_base
from . import constantes
import random
class Enemigo2(Enemigo_base):
    def __init__(self,pos,direccion,agresividad):
        super().__init__(pos,direccion)
        self.daño = 20
        self.atacando = False
        self.posy_inicial = pos[1]
        self.image.fill(constantes.NARANJA)
        self.agresividad = agresividad
    
    def comportamiento(self):
        ataque=None
        if not(self.atacando):
            ataque = random.randint(0,self.agresividad)
        if(ataque == 0):
            self.velx = 0
            self.vely = 60
            self.atacando = True
        
    def comportamiento_limites(self):
        self.comportamiento()
        if(self.atacando):
            if(self.rect.y > constantes.ZONA_JUEGO) and(self.vely >0):
                self.vely = -1*self.vely
            if(self.rect.y == self.posy_inicial) and (self.vely < 0):
                self.vely = 0
                self.velx = 20
                self.atacando = False
        super().comportamiento_limites()


