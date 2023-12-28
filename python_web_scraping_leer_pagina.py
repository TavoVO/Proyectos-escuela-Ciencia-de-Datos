#
#	python_web_scraping_leer_pagina.py
#
#	Lee una página Web y la imprime en pantalla
#
#	Rogelio Ferreira Escutia - junio 2021 - ok
#

import requests
from bs4 import BeautifulSoup
url = "http://sagitario.itmorelia.edu.mx/~rogelio/hola.htm"
#html = requests.get('http://www.aprenderpython.net')
html = requests.get(url)
bs = BeautifulSoup((html.text), 'html.parser')
print("\nExtraer el Código HTML de una página:")
print("\nURL: ", url)
print("\n", bs)
print("Imprimir la primer etiqueta h1")
print("\n", bs.h1, "\n")