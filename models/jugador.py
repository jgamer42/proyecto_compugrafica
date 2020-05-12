import pygame
from . import utilidades
from . import constantes
from .misil import Misil

#cambios realizados
#1. creado funcionalidad pedida por JeyP de misiles laterales
#2. la funcion recortar imagen se puso en el archivo utilidades
#motivo: esto porque dicha funcion pude ser reusada en otros elementos del juego
#3. la tecla para cambiar de sprite se cambio por la S
#motivo: la tecla usada previamente esta ocupada por la nueva funcionalidad de disparo
class Jugador(pygame.sprite.Sprite):

    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.animaciones = []
        self.estado = 0
        self.frame = 0
        sabana1 = pygame.image.load("./Sprites/PlayerShipSprite_I.png")
        sabana2 = pygame.image.load("./Sprites/PlayerShipSprite_II.png")
        sabana3 = pygame.image.load("./Sprites/PlayerShipSprite_III.png")
        self.velx = 0
        self.vely = 0
        self.animaciones.append(utilidades.recorte_imagen(sabana1,[90,67]))
        self.animaciones.append(utilidades.recorte_imagen(sabana2,[80,85]))
        self.animaciones.append(utilidades.recorte_imagen(sabana3,[120,90]))
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

    def controles(self,evento,lista_balas):
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
        if(evento.key == pygame.K_s):
            self.cambio_animacion()
        if(evento.key == pygame.K_a):
            origen_disparo = [self.rect.right,self.rect.y]
            self.disparar(lista_balas,origen_disparo)
        if(evento.key == pygame.K_d):
            origen_disparo = [self.rect.left,self.rect.y]
            self.disparar(lista_balas,origen_disparo)

    def frenar(self):
        self.velx=0
        self.vely=0

    def disparar(self,lista_balas,origen_disparo):
        bala = Misil(origen_disparo)
        lista_balas.add(bala)

    def cambio_animacion(self):
        pos_x = self.rect.x
        pos_y = self.rect.y
        self.estado = self.estado + 1
        self.image = self.animaciones[self.estado][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
