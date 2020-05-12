import pygame
from . import constantes

class Jugador(pygame.sprite.Sprite):

    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.animaciones = []
        self.estado = 0
        self.frame = 0
        sabana1 = pygame.image.load("./Sprites/Jugador/jugador1.png")
        sabana2 = pygame.image.load("./Sprites/Jugador/jugador2.png")
        self.velx = 0
        self.vely = 0
        self.animaciones.append(self.recorte_imagen(sabana1,80,85))
        self.animaciones.append(self.recorte_imagen(sabana2,80,85))
        self.image = self.animaciones[self.estado][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.animar()
        self.control_limites()
        self.rect.x = self.velx + self.rect.x
        self.rect.y = self.vely + self.rect.y

    def animar(self):
        if self.frame < 2:
            self.frame = self.frame + 1
        else:
            self.frame = 0
        self.image = self.animaciones[self.estado][self.frame]

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
        if(evento.key == pygame.K_a):
            self.cambio_animacion()

    def frenar(self):
        self.velx=0
        self.vely=0
    
    def cambio_animacion(self):
        pos_x = self.rect.x 
        pos_y = self.rect.y
        self.estado = self.estado + 1
        self.image = self.animaciones[self.estado][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def recorte_imagen(self,sabana,x,y):
        animacion = []
        for c in range(3):
            cuadro = sabana.subsurface(x*c,0,x,y)
            animacion.append(cuadro)
        return (animacion)
        
