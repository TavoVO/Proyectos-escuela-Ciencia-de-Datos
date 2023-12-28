#Procesos
from multiprocessing import Process
def funcion_proceso(numero):
    print("\nHola Crayola!!")
    print("\nDesde el proceso "+str(numero))

if __name__ == "__name__":                                            # Definiendo el programa principal
    print("\nInicio del  programa Principal")                         
    numero=1
    proceso_uno = Process(target=funcion_proceso, args=(numero,))     # Creación del proceso
    proceso_uno.start()                                               # Arranque del Proceso