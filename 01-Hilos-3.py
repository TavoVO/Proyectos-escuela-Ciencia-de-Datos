#Hilos y variables globales
from threading import Thread                    # Libreria
suma = 0

def funcion_hilo():
    print("\nIniciando Hilo")
    global suma 
    suma +=5
    print("Variable global modicifacada")

print("\nInicio del programa")
print("\nValor Inicial: "+str(suma))
hilo_uno = Thread(target=funcion_hilo)        # Creación del hilo
hilo_uno.start()                              # Arranque
hilo_uno.join()                               # Esperando que termine el hilo
print("\nValor Final: "+str(suma))