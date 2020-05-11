import pygame
from . import constantes

class Jugador(pygame.sprite.Sprite):

    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        #Recorte de imagen
        self.sabana = pygame.image.load("./Sprites/Naves/Sprite_Nave_III.png").convert_alpha()
        self.nave = []
        for c in range(3):
            cuadro = self.sabana.subsurface(120*c,0,120,90)
            self.nave.append(cuadro)
        #Variables
        self.contador = -1
        self.velx = 0
        self.vely = 0
        self.image = self.nave[self.contador]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if self.contador < 2:
            self.contador += 1
        else:
            self.contador = 0
        self.image = self.nave[self.contador]

        self.control_limites()
        self.rect.x = self.velx + self.rect.x
        self.rect.y = self.vely + self.rect.y

    def control_limites(self):
        if(self.rect.left <= 0):
            self.velx=0
            self.rect.x = self.rect.x + 1
        if(self.rect.right >= constantes.ANCHO):
            self.velx = 0
            self.rect.x = self.rect.x - 1

        if(self.rect.top <= constantes.ZONA_JUEGO):
            self.vely = 0
            self.rect.y = self.rect.y + 1
        if(self.rect.bottom >= constantes.ALTO):
            self.vely = 0
            self.rect.y = self.rect.y - 1

    def controles(self,evento):
        if(evento.key == pygame.K_RIGHT):
            self.velx = 5
            self.vely = 0
        if(evento.key == pygame.K_LEFT):
            self.velx = -5
            self.vely = 0
        if(evento.key == pygame.K_UP):
            self.vely = -5
            self.velx = 0
        if(evento.key == pygame.K_DOWN):
            self.vely = 5
            self.velx = 0

    def frenar(self):
        self.velx=0
        self.vely=0
