#Tres Hilos
from threading import Thread                    # Libreria

def funcion_hilo():                             # Función asignada al hilo
    print("Hola Mundo desde un hilo")           # Desde el hilo

print("\nIniciodel programa principal")
hilo_uno = Thread(target=funcion_hilo(1))       # Creación del hilo 1
hilo_dos = Thread(target=funcion_hilo(2))       # Creación del hilo 2
hilo_tres = Thread(target=funcion_hilo(3))      # Creación del hilo 3
hilo_uno.start()                                # Arranque hilo 1
hilo_dos.start()                                # Arranque hilo 2
hilo_tres.start()                               # Arranque hilo 3