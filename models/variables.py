import pygame
from . import utilidades
#sprites groups
jugadores = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
elementos_ambientales = pygame.sprite.Group()
balas_enemigos = pygame.sprite.Group()
balas_jugador = pygame.sprite.Group()
satelites = pygame.sprite.Group()
modificadores = pygame.sprite.Group()
asteroides = pygame.sprite.Group()
tipo_misil = "misil"
estado_nave = 0

#sonido
pygame.mixer.init()
music_intro = pygame.mixer.Sound('./Sounds/Brave Pilots (Menu Screen).ogg')
music_juego = pygame.mixer.Sound('./Sounds/Juego.ogg')
music_out = pygame.mixer.Sound("./Sounds/Game Over.ogg")

disparo = pygame.mixer.Sound('./Sounds/shoot.wav')
explosion_jugador = pygame.mixer.Sound('./Sounds/boom.wav')

sound_Fireworks1 = pygame.mixer.Sound("./Sounds/Fireworks1.wav")
sound_Fireworks2 = pygame.mixer.Sound("./Sounds/Fireworks2.ogg")

#imagenes
PantInit = pygame.image.load("./Sprites/fondos/Universe2PantInit.png")
LogoPantInit = pygame.image.load("./Sprites/fondos/Logo2PantInit.png")

sabana_game_over = pygame.image.load("./Sprites/fondos/SpriteGameOver.png")
GameOver = utilidades.recorte_imagen(sabana_game_over,[768,690],2)

sabana_victoria = pygame.image.load("./Sprites/SpriteVictoria.png")
Victoria = utilidades.recorte_imagen(sabana_victoria,[768,690],2)

fondo = pygame.image.load("./Sprites/Background.png")
saba_puntos = pygame.image.load("./Sprites/Gui/Ambiente.png")
sabana_vidas = pygame.image.load("./Sprites/Gui/SpriteVidas.png")
sabana_salud = pygame.image.load("./Sprites/Gui/SpriteSalud.png")
sprite_salud = utilidades.recorte_imagen(sabana_salud,[80,30],6)
sprite_vidas = utilidades.recorte_imagen(sabana_vidas,[116,30],3)

sabana_muerte_enemigos = pygame.image.load("./Sprites/enemigos/SpriteEnemyExplosion.png")
animacion_muerte_enemigos = utilidades.recorte_imagen(sabana_muerte_enemigos,[90,80],6)

#otros
reloj = pygame.time.Clock()
pos_fondo = -3450
