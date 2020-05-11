# Galaxy War survival

## REQUERIMIENTOS

* [ ] intro :sunglasses:

* [ ] final :sunglasses:

* [ ] imagenes de fondo y musica :headphones:

* [ ] barra de información (gui) :eye:

* [ ] implementar 2 enemigos diferentes :space_invader: 

* [ ] implementar 2 elementos ambientales :seedling:

* [ ] implementar generadores de enemigos :anger:

* [ ] implementar modificadores :dizzy:

* [ ] implementar como minimo 3 niveles (nota cada nivel con el triple de tamaño de la pantalla)

## ELEMENTOS DE JUEGO

### Jugador
![imagen jugador](https://raw.githubusercontent.com/jgamer42/proyecto_compugrafica/master/Cosas_Jeyp/naves/Nave_I.png)
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
  * tamaño del sprite = 80 X 85
  * frames de animacion = 3
  * estados posibles = ??

#### anexos

* #### maquina de estados

* #### sprites de cada estados

---

### Enemigos

#### tipo 1 (nombre)

* ##### Atributos

  * vida = cuanta vida tienen
  * daño = tipo de bala disparado
  * velocidad = 20 px

* ##### comportamiento

  * rebotan contra los limites laterales
  * no tienen movimiento vertical

#### tipo 2 (nombre)

* ##### Atributos

  * vida = cuanta vida tienen
  * daño = tipo de bala disparado
  * velocidad = 20 px

* ##### comportamiento
  
  * no dispara
  * rebota contra los limites de la pantalla
  * de manera aleatoria embiste al jugador para hacerle daño
  * la embestida solo permite movimiento vertical

---

### Balas

#### tipo 1 (nombre)

* ##### Atributos

  * daño = tipo de bala disparado
  * velocidad = 50 px

* ##### comportamiento

  * rebota contra los limites de la pantalla

#### tipo 2 (nombre)

* ##### Atributos

  * daño = 20 puntos
  * velocidad = 50 px

* ##### comportamiento
 

#### tipo 3 (nombre)

* ##### Atributos

  * daño = tipo de bala disparado
  * velocidad = 50 px

* ##### comportamiento


-----

### spawner

  * #### atributos
    * vida = (si puede morir)
    * que enemigos spawnea

  * #### comportamiento 
    * proceso de spawn de elementos
----

### bloques

#### tipo 1 (nombre)

  * caracteristicas
    * efectos
    * aparicion

#### tipo 2 (nombre )
  *  caracteristicas
    * efectos
    * aparicion

----

### modificadores

#### tipo 1 (nombre)
  * sprite
  * aparicion
  * efectos


## MECANICAS

* ### desplazamiento del escenario

* ### condicion victoria

* ### condicion fin de juego

* ### condicion cambio de nivel

## DISEÑOS

* ### gui

### niveles

* #### nivel 1

* ### nivel 2

* ### nivel 3


