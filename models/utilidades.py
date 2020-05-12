def recorte_imagen(sabana,dimensiones):
        animacion = []
        for c in range(3):
            cuadro = sabana.subsurface(dimensiones[0]*c,0,dimensiones[0],dimensiones[1])
            animacion.append(cuadro)
        return (animacion)
