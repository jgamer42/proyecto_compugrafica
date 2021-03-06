import pygame
from . import utilidades as util
from . import ambiente
from . import constantes
from .misil import Misil
from .misil2 import Misil2
from . import variables

class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.animaciones = []
        self.explosion =[]
        self.vidas = 3
        self.salud = 1000
        self.puntos = 0
        self.estado = 0
        self.frame = 0
        self.pos_inicial = pos
        sabana1 = pygame.image.load("./Sprites/jugador/PlayerShipSprite_I.png")
        sabana2 = pygame.image.load("./Sprites/jugador/PlayerShipSprite_II.png")
        sabana3 = pygame.image.load("./Sprites/jugador/PlayerShipSprite_III.png")
        sabana_explosion = pygame.image.load("./Sprites/jugador/PlayerShipExplosion.png")
        self.animaciones.append(util.recorte_imagen(sabana1,[90,67],3))
        self.animaciones.append(util.recorte_imagen(sabana2,[80,85],3))
        self.animaciones.append(util.recorte_imagen(sabana3,[120,90],3))
        self.animaciones.append(util.recorte_imagen(sabana_explosion,[128,100],4))
        self.image = self.animaciones[self.estado][self.frame]
        self.rect = self.image.get_rect()
        self.velx = 0
        self.vely = 0
        self.speed = False
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.repeticiones = 0

    def update(self):
        self.frame = util.animar(self.frame,3)
        self.cambio_animacion()
        self.control_limites()
        self.evaluar_vida()
        self.animacion_muerte()
        self.jugador_en_juego()
        self.rect.x = self.velx + self.rect.x
        self.rect.y = self.vely + self.rect.y

    def evaluar_vida(self):
        if self.salud <= 0:
            self.reproducir_sonido("boom")
            self.frenar()
            self.estado = 3

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
            if(evento.key == pygame.K_s):
                self.speed = True
            if(evento.key == pygame.K_RIGHT):
                if self.speed:
                    self.velx = 15 * (self.estado + 1)
                    self.vely = 0
                else:
                    self.velx = 5 * (self.estado + 1)
                    self.vely = 0
            if(evento.key == pygame.K_LEFT):
                if self.speed:
                    self.velx = -15 * (self.estado + 1)
                    self.vely = 0
                else:
                    self.velx = -5 * (self.estado + 1)
                    self.vely = 0
            if(evento.key == pygame.K_UP):
                if self.speed:
                    self.vely = -15 * (self.estado + 1)
                    self.velx = 0
                else:
                    self.vely = -5 * (self.estado + 1)
                    self.velx = 0
            if(evento.key == pygame.K_DOWN):
                if self.speed:
                    self.vely = 15 * (self.estado + 1)
                    self.velx = 0
                else:
                    self.vely = 5 * (self.estado + 1)
                    self.velx = 0
            if(evento.key == pygame.K_d and not ambiente.alarma_planeta):
                origen_disparo = [self.rect.right-20,self.rect.y]
                self.disparar(lista_balas,origen_disparo,variables.tipo_misil)
                self.reproducir_sonido("bala")
            if(evento.key == pygame.K_a and not ambiente.alarma_planeta):
                origen_disparo = [self.rect.left,self.rect.y]
                self.disparar(lista_balas,origen_disparo,variables.tipo_misil)
                self.reproducir_sonido("bala")
        if evento.type == pygame.KEYUP:
            if(evento.key == pygame.K_UP) or (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                self.frenar()
            if evento.key == pygame.K_s:
                self.speed = False

    def frenar(self):
        self.velx=0
        self.vely=0

    def disparar(self,lista_balas,origen_disparo,tipo_misil):
        if tipo_misil == "misil":
            bala = Misil(origen_disparo)
        else:
            bala = Misil2(origen_disparo)
        lista_balas.add(bala)

    def cambio_animacion(self):
        pos_x = self.rect.x
        pos_y = self.rect.y
        self.image = self.animaciones[self.estado][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def reproducir_sonido(self,tipo):
        if tipo == "bala":
            variables.disparo.play()
        elif tipo == "boom":
            variables.explosion_jugador.play()


    def animacion_muerte(self):
        if(self.estado == 3):
            if(self.frame == 2 and self.repeticiones == 3):
                self.reiniciar()
                self.vidas -= 1
            elif(self.frame == 2):
                self.repeticiones += 1

    def reiniciar(self):
        self.salud = 1000
        self.estado = variables.estado_nave
        self.repeticiones = 0
        self.rect.x = self.pos_inicial[0]
        self.rect.y = self.pos_inicial[1]
        self.velx = 0
        self.vely = 0

    def jugador_en_juego(self):
        if(self.vidas > 0):
            pass
        else:
            ambiente.alarma_gameover = True
