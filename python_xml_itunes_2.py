#
#   python_xml_itunes_2.py
#
#   Lee el archivo XML de iTunes App Reviews e imprime todos los comentarios encontrados
#
#   Rogelio Ferreira Escutia - noviembre 2020
#
#   Requisitos:
#   Se requiere instalar "lxl", un parser de XML
#       En consola: pip3 install lxml
#   Se requiere instalar "BeautifulSoup"
#       En consola: pip3 install bs4

import requests                 # Importamos "request" para accesar a páginas Web
import lxml                     # Importamos "lxml" que nos servirá para parsear XML
from bs4 import BeautifulSoup   # Importamos "BeautifulSoup" para procesar páginas Web

# Leemos el archivo XML que se encuentra en Internet
print("\nLEYENDO ARCHIVO XML:")
url = "https://itunes.apple.com/mx/rss/customerreviews/page=1/id=284882215/sortBy=mostrecent/xml"
datos_xml = requests.get(url).content

# Parseamos el archivo XML utilizando "lxml" y lo cargamos en "BeautifulSoup"
print("PARSEANDO Y CARGANDO EN BEAUTIFULSOUP:")
datos_bs = BeautifulSoup(datos_xml, "lxml")

# Almacenamos todos los comentarios en una lista (etiqueta "content") y las imprimimos
lista_comentarios = []
lista_comentarios = datos_bs.find_all("content")
contador = 0
for elemento in lista_comentarios:
    contador = contador + 1
    print("\nComentario " + str(contador) + ":\n" + elemento.text)
print("\nComentarios totales: " + str(len(lista_comentarios)))