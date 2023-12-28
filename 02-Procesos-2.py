# Conexion entre dos Procesos 
from multiprocessing import Process, Pipe
def funcion_cliente(pipe_terminal, nombre):
    print("\nProceso cliente recibe: "+str(nombre))
    mensaje = "Bienvenido a la Matrix"                       #mensaje a regresar
    pipe_terminal.send(mensaje)
    pipe_terminal.close()

if __name__ == "__name__":
    print("\nInicio del Proceso Servidor")
    nombre = "Octavio"
    pipe_servidor, pipe_cliente = Pipe()
    proceso = Process(target=funcion_cliente, args=(pipe_cliente,nombre))
    proceso.start()
    print("\nProceso Servidor recibe del Proceso Clinete: "+pipe_servidor.recv())
    proceso.join()