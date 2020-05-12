from .bloque_base import Bloque_base
from . import constantes
#cambios
#1 . se implemento comportamiento basico del primer asteroide
# FIXME: revisar como descargar solo cuando salga por el borde inferior de la pantalla
class Asteroide1(Bloque_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.vely = constantes.VELOCIDAD_ENTORNO
        
