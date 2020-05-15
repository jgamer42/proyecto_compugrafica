# Galaxy War survival

![logo del juego](https://raw.githubusercontent.com/jgamer42/proyecto_compugrafica/master/Sprites/fondos/LogoPantInit.png)

## REQUERIMIENTOS

* [x] intro :sunglasses:

* [x] final :sunglasses:

* [x] imagenes de fondo y musica :headphones:

* [ ] barra de información (gui) :eye:

* [x] implementar 2 enemigos diferentes :space_invader: 

* [ ] implementar 2 elementos ambientales :seedling:

* [ ] implementar generadores de enemigos :anger:

* [ ] implementar modificadores :dizzy:

* [x] implementar como minimo 3 niveles (nota cada nivel con el triple de tamaño de la pantalla)

## ELEMENTOS DE JUEGO

### Jugador
![imagen jugador](https://raw.githubusercontent.com/jgamer42/proyecto_compugrafica/master/Sprites/jugador/PlayerShipSprite_I.png)
#### atributos

* vida/ salud = ??
* daño = Varia segund el bala (ver tipos de balas)
* velocidad = 5 px
#### comportamiento

* colisiona con los bordes
* no puede pasar de cierto punto de la pantalla
* dispara proyectiles
* posee diferentes estados

#### detalles tecnicos
  * frames de animacion = 3
  * estados posibles = 3

---

### Enemigos

#### tipo 1 (nombre)

![enemigo basico](https://raw.githubusercontent.com/jgamer42/proyecto_compugrafica/master/Sprites/enemigos/SpriteEnemyShip_I.png)

* ##### Atributos

  * vida = ??
  * daño = misil 1
  * velocidad = 5 px

* ##### comportamiento

  * rebotan contra los limites laterales
  * no tienen movimiento vertical

#### tipo 2 (nombre)

* ##### Atributos

  * vida = cuanta vida tienen
  * daño = 
  * velocidad = 5 px

* ##### comportamiento
  
  * no dispara
  * rebota contra los limites de la pantalla
  * de manera aleatoria embiste al jugador para hacerle daño
  * la embestida solo permite movimiento vertical

---

### Balas

#### Misil
 
 ![balas tipo1](https://raw.githubusercontent.com/jgamer42/proyecto_compugrafica/master/Sprites/balas/SpritePlayerMisil_I.png)

* ##### Atributos

  * daño = ???
  * velocidad = 50 px

* ##### comportamiento

  * se mueve de manera vertical hasta salir de la pantalla

#### tipo 2 (nombre)

* ##### Atributos

  * daño = 20 puntos
  * velocidad = 50 px

* ##### comportamiento


-----

### spawner

----

### bloques

#### asteroide
 
![asteoride](https://raw.githubusercontent.com/jgamer42/proyecto_compugrafica/master/Sprites/bloques/Asteroid.png)

  * caracteristicas
    * genera daño con la colision
    * aparece por fuera de la pantalla y de desplaza acorde a la velocidad del entorno
----

### modificadores

## MECANICAS

* ### escenario

  * El escenario posee varios elementos ambientales
  * se desplaza a una velocidad de 20 px

* ### condicion victoria

  * superar el ultimo nivel

* ### condicion fin de juego
  * que el jugadro se quede sin vidas

* ### condicion cambio de nivel

## DISEÑOS

* ### gui

### niveles

* #### nivel 1

* ### nivel 2

* ### nivel 3


