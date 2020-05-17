import pygame
from . import utilidades as util
from . import constantes
from .misil import Misil

#1. se agrega la variable salud, esta sirve para medir la cantidad de impactos y cuando debe explotar
#2. se agrega sabana_explosion donde estara el sprite
#3. se agrega "explosion" donde quedara la animacion de la explosion
#4 se agrega la variable vidas donde se mediran los intentos (vidas) que tiene
#5 se agrega la cancelacion del mixer para limpiar memoria, de hecho no se si sea necesario inicializarlo ahi, en efecto al usarlo sin esa inicializacion funciona perfecto. al parecer esta implicito en import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.animaciones = []
        self.explosion =[]
        self.vidas = 3
        self.salud = 1000
        self.estado = 0
        self.frame = 0
        sabana1 = pygame.image.load("./Sprites/jugador/PlayerShipSprite_I.png")
        sabana2 = pygame.image.load("./Sprites/jugador/PlayerShipSprite_II.png")
        sabana3 = pygame.image.load("./Sprites/jugador/PlayerShipSprite_III.png")
        sabana_explosion = pygame.image.load("./Sprites/jugador/PlayerShipExplosion.png")
        self.animaciones.append(util.recorte_imagen(sabana1,[90,67],3))
        self.animaciones.append(util.recorte_imagen(sabana2,[80,85],3))
        self.animaciones.append(util.recorte_imagen(sabana3,[120,90],3))
        self.explosion = util.recorte_explosion(sabana_explosion,[256,200],4,3)
        self.image = self.animaciones[self.estado][self.frame]
        self.rect = self.image.get_rect()
        self.velx = 0
        self.vely = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if self.salud <= 0:
            self.frenar()
            self.frame = util.animar(self.frame,9)
            self.image = self.explosion[self.frame]
        else:
            self.frame = util.animar(self.frame,3)
            self.image = self.animaciones[self.estado][self.frame]
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

    def controles(self,evento,lista_balas):
        if(evento.type == pygame.KEYDOWN):
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
            if(evento.key == pygame.K_d):
                origen_disparo = [self.rect.right-20,self.rect.y]
                self.disparar(lista_balas,origen_disparo)
                self.reproducir_sonido()
            if(evento.key == pygame.K_a):
                origen_disparo = [self.rect.left,self.rect.y]
                self.disparar(lista_balas,origen_disparo)
                self.reproducir_sonido()
        if evento.type == pygame.KEYUP:
            if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                self.frenar()

    def frenar(self):
        self.velx=0
        self.vely=0

    def disparar(self,lista_balas,origen_disparo):
        bala = Misil(origen_disparo,-1)
        lista_balas.add(bala)

    def cambio_animacion(self):
        pos_x = self.rect.x
        pos_y = self.rect.y
        self.estado += 1
        self.image = self.animaciones[self.estado][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def reproducir_sonido(self):
        disparo = pygame.mixer.Sound('./Sounds/shoot.wav')
        disparo.play()
