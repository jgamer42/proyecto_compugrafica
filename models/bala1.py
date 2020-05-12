from .bala_base import Bala_base
import pygame
class Bala1(Bala_base):

    def __init__(self,pos):
        super().__init__(pos)
        pos_x = self.rect.x
        pos_y = self.rect.y
        sabana = pygame.image.load("./Sprites/balas/bala1.png")
        self.animacion = self.recorte_imagen(sabana,19,88)
        self.frame = 0
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    
    def recorte_imagen(self,sabana,x,y):
        animacion = []
        for c in range(3):
            cuadro = sabana.subsurface(x*c,0,x,y)
            animacion.append(cuadro)
        return (animacion)
        
    