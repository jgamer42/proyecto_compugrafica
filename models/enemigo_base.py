import pygame
from . import constantes
class Enemigo_base(pygame.sprite.Sprite):
    def __init__(self,pos,direccion,agresividad):
        pygame.sprite.Sprite.__init__(self)
        self.velx = 8*direccion
        self.vely = 0
        self.image=pygame.Surface([50,50])
        self.image.fill(constantes.AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.direccion = 1
        self.agresividad = agresividad

    def update(self):
        self.comportamiento_limites()
        self.rect.x = self.rect.x + self.velx*self.direccion
        self.rect.y = self.rect.y + self.vely

    def comportamiento_limites(self):
        if(self.rect.left <= 0) or (self.rect.right >= constantes.ANCHO):
            self.direccion = self.direccion*-1
