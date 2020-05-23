import pygame
from. import constantes


class Bloque_base(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.posActual = pos
        self.velx = 0
        self.vely = constantes.VELOCIDAD_ENTORNO
        self.image = pygame.Surface([50,100])
        self.image.fill(constantes.ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.posActual[0] = self.rect.x + self.velx
        self.rect.x = self.posActual[0]
        self.posActual[1] = self.rect.y + self.vely
        self.rect.y = self.posActual[1]
