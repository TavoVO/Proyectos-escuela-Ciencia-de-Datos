#Hola mundo con Hilos
from threading import Thread

def funcion_hilo():                          # Función asignada al hilo
    print("Hola Mundo desde un hilo")        # Desde el hilo

print("\nIniciodel programa principal")
hilo_uno = Thread(target=funcion_hilo)       # Creación del hilo
hilo_uno.start()                             # Arranque del hilo
