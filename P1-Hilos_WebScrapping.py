from urllib.request import urlopen  # Importamos "urlopen" para abrir una página Web
from bs4 import BeautifulSoup       # Importamos "BeautifulSoup" para hacer WebScraping
from threading import Thread                    # Libreria

def funcion_hilo1():
    pagina_inicial = "http://www.xumarhu.net/"
    print("\nPAGINA WEB: " + pagina_inicial)

    # Cargar página en memoria
    url = urlopen(pagina_inicial)

    # Parsear la página usando HTML
    bs = BeautifulSoup(url.read(), 'html.parser')

    # Extraer e imprimir el título de la página
    print("\nTITULO: " + bs.title.text + "\n")

    # Extraer todos los enlaces de la página
    todos_los_enlaces = bs.find_all('a')

    # Creamos 2 arreglos para almacenar los enlaces y su texto correspondiente
    enlace = []
    texto = []

    # Inicializamos el puntero del arreglo
    j = 0

    # Se van leyendo todos los enlaces y se almacenan en el arreglo
    for ciclo in todos_los_enlaces:
        texto.append(ciclo.get_text())
        enlace.append(ciclo.get('href'))
        j = j + 1

    # Extraer la PRIMER noticia importante
    j = 9
    print("NOTICIA 1 - Texto: " + texto[j] + " Enlace: " + enlace[j])

    # Extraer la SEGUNDA noticia importante
    j = 11
    print("NOTICIA 2 - Texto: " + texto[j] + " Enlace: " + enlace[j])

    # Extraer la SEGUNDA noticia importante
    j = 13
    print("NOTICIA 3 - Texto: " + texto[j] + " Enlace: " + enlace[j])

    # Descargar imagen a la computadora
    import requests 
    url_imagen = pagina_inicial + enlace[9]
    nombre_local_imagen = enlace[9]
    imagen = requests.get(url_imagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)

    # Abrir Modo Gráfico usando la biblioteca "Tkinter"
    import tkinter as tk
    from tkinter import ttk, PhotoImage, Label
    from PIL import ImageTk, Image
    ventana = tk.Tk()
    ventana.title("Imprimir noticias importantes")
    ttk.Label(ventana, text = "NOTICIA 1: " + texto[9]).grid(column = 0, row = 0)
    path = enlace[9]
    img = ImageTk.PhotoImage(Image.open(path))
    fondo=Label(ventana,image=img).place(x=100,y=100)
    ventana.mainloop()

def funcion_hilo2():
    pagina_inicial = "https://firebase.google.com/?hl=es-419"
    print("\nPAGINA WEB: " + pagina_inicial)

    # Cargar página en memoria
    url = urlopen(pagina_inicial)

    # Parsear la página usando HTML
    bs = BeautifulSoup(url.read(), 'html.parser')

    # Extraer e imprimir el título de la página
    print("\nTITULO: " + bs.title.text + "\n")

    # Extraer todos los enlaces de la página
    todos_los_enlaces = bs.find_all('a')

    # Creamos 2 arreglos para almacenar los enlaces y su texto correspondiente
    enlace = []
    texto = []

    # Inicializamos el puntero del arreglo
    j = 0

    # Se van leyendo todos los enlaces y se almacenan en el arreglo
    for ciclo in todos_los_enlaces:
        texto.append(ciclo.get_text())
        enlace.append(ciclo.get('href'))
        j = j + 1

    # Extraer la PRIMER noticia importante
    j = 9
    print("NOTICIA 1 - Texto: " + texto[j] + " Enlace: " + enlace[j])

    # Extraer la SEGUNDA noticia importante
    j = 11
    print("NOTICIA 2 - Texto: " + texto[j] + " Enlace: " + enlace[j])

    # Extraer la SEGUNDA noticia importante
    j = 13
    print("NOTICIA 3 - Texto: " + texto[j] + " Enlace: " + enlace[j])

    # Descargar imagen a la computadora
    import requests 
    url_imagen = pagina_inicial + enlace[9]
    nombre_local_imagen = enlace[9]
    imagen = requests.get(url_imagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)

    # Abrir Modo Gráfico usando la biblioteca "Tkinter"
    import tkinter as tk
    from tkinter import ttk, PhotoImage, Label
    from PIL import ImageTk, Image
    ventana = tk.Tk()
    ventana.title("Imprimir noticias importantes")
    ttk.Label(ventana, text = "NOTICIA 1: " + texto[9]).grid(column = 0, row = 0)
    path = enlace[9]
    img = ImageTk.PhotoImage(Image.open(path))
    fondo=Label(ventana,image=img).place(x=100,y=100)
    ventana.mainloop()

print("\nInicio del programa")
hilo_uno = Thread(target=funcion_hilo1)        # Creación del hilo
hilo_dos = Thread(target=funcion_hilo2)
hilo_uno.start()                              # Arranque
hilo_dos.start()                              # Arranque