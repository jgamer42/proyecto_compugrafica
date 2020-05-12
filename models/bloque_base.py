import pygame
from. import constantes

#se agrega imagen asteroide

class Bloque_base(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.velx = 0
        self.vely = 0
        self.image = pygame.image.load("./Sprites/Asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect.y = self.rect.y + self.vely
        self.rect.x = self.rect.x + self.velx
