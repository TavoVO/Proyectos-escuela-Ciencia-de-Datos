#Liempieza caracter por caracter
#importar Librerias
import nltk              #procesamiento del lenguaje 

#cargar archivo de texto a memoria
with open('discurso_steve_jobs_stanford_12_junio_2005.txt',"r",encoding='utf8') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

#Eliminar simbolos y caracteres especiales
eliminar = '`.;,:-_!¡¿?/$%&<>|¨""'
texto_sin_simbolos = ""
for caracter in texto:
    if(caracter not in eliminar):
        texto_sin_simbolos = texto_sin_simbolos+caracter

#Cantidad de caracteres
caracteres = len(texto)
print("\nLa cantidad de caracteres: ", caracteres)

#Cantidad de palabras
palabras = len(set(texto))
print("\nCantidad de palabras: ", palabras)

# Divesidad Léxica
diversidad = palabras/caracteres
print("\nDivesidad Léxica: ",diversidad)

"""""
Diversidad Léxica = palabras/caracteres
"""""