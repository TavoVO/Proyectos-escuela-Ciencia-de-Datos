#
#   python_xml_itunes_2.py
#
#   Lee el archivo XML de iTunes App Reviews e imprime si el primer comentario es positivo o negativo
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
import string                   # Importamos "string" para el manejo de cadenas

print("\nANALISIS DE SENTIMIENTOS EN LOS APPs REVIEWs de iTunes")

# Leemos el archivo XML que se encuentra en Internet
url = "https://itunes.apple.com/mx/rss/customerreviews/page=1/id=284882215/sortBy=mostrecent/xml"
print("\nLEYENDO ARCHIVO XML: " + url)
datos_xml = requests.get(url).content

# Parseamos el archivo XML utilizando "lxml" y lo cargamos en "BeautifulSoup"
print("\nPARSEANDO Y CARGANDO EN BEAUTIFULSOUP...")
datos_bs = BeautifulSoup(datos_xml, "lxml")

# Buscamos e imprimimos el contenido del primer comentario encontrado (etiqueta "content")
resultado = datos_bs.find("content")
primer_comentario = resultado.text
print("\nPRIMER COMENTARIO ENCONTRADO: \n" + primer_comentario + "\n")

# Convertimos todo el comentario a minúsculas para mejor procesamiento
primer_comentario = primer_comentario.lower()

# Lista de frases positivas y negativas a encontrar
frases_positivas = ["Bueno","excelente","si"]
frases_negativas = ["Malo","mal","no"]

# Buscar si el comentario tiene frases positivas
evaluacion = ""
for elemento in frases_positivas:
    if(primer_comentario.find(elemento)) >= 0:
        evaluacion = "positivo"
        print("Frase positiva encontrada: " + elemento)

# Buscar si el comentario tiene frases negativas
for elemento in frases_negativas:
    if(primer_comentario.find(elemento)) >= 0:
        evaluacion = "negativo"
        print("Frase negativa encontrada: " + elemento)

# Determinar que no se pudo encontrar ni positivo ni negativo
if(evaluacion == ""):
    evaluacion = "No se pudo detectar ni positivo ni negativo"

# Imprimir el resultado de la evaluación
print("\nRESULTADO DE LA EVALUACION: " + evaluacion + "\n")