#cambios
#1. se agrego el metodo animar
#   funcionamiento
#   recibe como parametros frame actual, numero de frames
#   retorna el frame siguiente
#   el cambio se de hace en la clase 

def recorte_imagen(sabana,dimensiones):
        animacion = []
        for c in range(3):
            cuadro = sabana.subsurface(dimensiones[0]*c,0,dimensiones[0],dimensiones[1])
            animacion.append(cuadro)
        return (animacion)
    
def animar(frame_actual,numero_frames):
        if frame_actual < (numero_frames - 1):
            frame_actual = frame_actual + 1
        else:
            frame_actual = 0
        return(frame_actual)

