from enemigo_base import Enemigo_base
class Enemigo_especifico(Enemigo_base):
    def __init__(self,pos,direccion):
        super().__init__(pos,direccion)