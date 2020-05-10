import pygame 
from. import constantes

class Bloque_base(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.velx = 0
        self.vely = 0
        self.image = pygame.Surface([10,50])
        self.image.fill(constantes.ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect.y = self.rect.y + self.vely
        self.rect.x = self.rect.x + self.velx