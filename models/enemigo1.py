import random
from .enemigo_base import Enemigo_base
from .misil import Misil
#cambios
#1. agregadas funcionalidad de disparo
class Enemigo1(Enemigo_base):
    def __init__(self,pos,direccion,lista_balas,agresividad):
        super().__init__(pos,direccion,agresividad)
        self.lista_balas = lista_balas
        self.atacando = False
    
    def atacar(self):
        ataque=None
        if not(self.atacando):
            ataque = random.randint(0,self.agresividad)
        if(ataque == 0):
            bala = Misil(self.rect.center,1)
            self.lista_balas.add(bala)
    
    def update(self):
        self.atacar()
        super().update()