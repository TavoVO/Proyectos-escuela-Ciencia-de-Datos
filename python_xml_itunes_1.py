#
#   python_xml_itunes_1.py
#
#   Lee el archivo XML de iTunes App Reviews e imprime el primer comentario encontrado
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
url = "https://itunes.apple.com/us/rss/customerreviews/page=1/id=284882215/sortBy=mostrecent/xml"
datos_xml = requests.get(url).content

# Parseamos el archivo XML utilizando "lxml" y lo cargamos en "BeautifulSoup"
print("PARSEANDO Y CARGANDO EN BEAUTIFULSOUP:")
datos_bs = BeautifulSoup(datos_xml, "lxml")

# Buscamos e imprimimos el contenido del primer comentario encontrado (etiqueta "content")
resultado = datos_bs.find("content")
print("\nPrimer Comentario encontrado: \n" + resultado.text)