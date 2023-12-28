# Lee archivo XML de iTunes App e imprime el primer comentario encontrado 
import requests                   #Importamos para procesar la página Web
import lxml                       #Importamos para parsear XML
from bs4 import BeautifulSoup     #Importamos para procesar páginas web

#Leemos el archivo XML que se encuentra en Internet
print("\nLeyendo el archivo XML: ")
url = "https://itunes.apple.com/mx/rss/customerreviews/page=1/id=284882215/sortBy=mostrecent/xml"
datos_xml = requests.get(url).content

# Parseamos el archivo XML utilizando "lxml" y lo cargamos en "BeautifulSoup"
print("PARSEANDO Y CARGANDO EN BEAUTIFULSOUP:")
datos_bs = BeautifulSoup(datos_xml, "lxml")

# Buscamos e imprimimos el contenido del primer comentario encontrado (etiqueta "content")
resultado = datos_bs.find("content")
print("\nPrimer Comentario encontrado: \n" + resultado.text)