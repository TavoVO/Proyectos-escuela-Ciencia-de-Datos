#
#   python_web_scraping_extraer_etiquetas.py
#
#   Extrae varias etiquetas de una página Web
#
#   Se requiere instalar "Beautifulsoup"
#       Mac: pip3 install beautifulsoup4
#       Linux: sudo apt-get install python-bs4
#
#   Rogelio Ferreira Escutia - junio 2021 - ok
#

from urllib.request import urlopen
from bs4 import BeautifulSoup

print("\nExtraer el contenido de algunas etiquetas de una página Web")
html = urlopen('http://sagitario.itmorelia.edu.mx/~rogelio/hola.htm')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.title)
print(bs.h1)
print(bs.h2)
print(bs.h3)