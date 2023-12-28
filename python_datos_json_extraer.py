#
#   python_datos_json_extraer.py
#
#   Leer un archivo de texto externo en formato JSON y extraer sus datos
#
#   Requerimientos:
#       Descargar el archivo "texto_004_json_lenguajes.json" del enlace:
#       www.xumarhu.net/texto_004_json_lenguajes.json
#
#   Rogelio Ferreira Escutia - octubre 2022
#

# Bibliotecas a utilizar
import json     # Manejo de archivos JSON

# Cargar archivo de texto a memoria
archivo_en_texto = "texto_004_json_lenguajes.json"
with open(archivo_en_texto,'r') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

# Imprimir texto completo
print ("\nJSON Completo:\n", texto)

# Parsear el JSON
json_memoria = json.loads(texto)

# Imprimir en formato JSON
print ("\nJSON Completo con Tabulación 4:\n", json.dumps(json_memoria, indent=4, sort_keys=True))

# Imprimir todos datos sobre la etiqueta "lenguajes"
print ("\nLista de datos de 'Lenguajes':\n", json_memoria['web']['languages'])

# Imprimir los datos de la primer etiqueta "lenguajes"
print ("\nLista de la primer etiqueta 'Lenguajes':\n", json_memoria['web']['languages'][0])

# Impresión los datos de "lenguajes" por línea
print ("\nLista de datos de 'Lenguajes' por línea:")
data = json_memoria['web']['languages']
for x in data:
	print(x['id'], x['name'], x['website'])