import re                                   # Manejo de expresiones regulares
import nltk                                 # Paraprocesar lenguaje natural
from nltk.tokenize import word_tokenize     # Para tokenizar un texto
from nltk.corpus import stopwords           # Cargar las "Stopwords" del español


############################################## Parte 1 Examen ################################################


with open('parte_1.txt','r', encoding='utf8') as archivo_en_memoria1:
    texto1 = archivo_en_memoria1.read()

texto_en_minusculas1 = texto1.lower()

#Eliminar simbolos y caracteres especiales
texto_sin_simbolos1 = re.sub(r'[^\w\s]','', texto_en_minusculas1)

# Convertimos a tokens todo el texto
tokens_de_mi_texto1 = word_tokenize(texto_sin_simbolos1)

#cargamos las stopwords del español
palabras_vacias1 = set(stopwords.words('spanish'))

#filtramos los tokens eliminados
lista_final1 = []
for palabra in tokens_de_mi_texto1:
    if palabra not in palabras_vacias1:
        lista_final1.append(palabra)

# Palabras Positivas y negativas para analizar un texto
palabras_positivas = []
with open('texto_002_palabras_positivas.txt','r', encoding='utf8') as archivo_en_memoria:
    while True:
        renglon = archivo_en_memoria.readline()
        if not renglon:
         break
        else: 
            elemento = renglon.strip("\n")
            palabras_positivas.append(elemento)

palabras_negativas = []
with open('texto_003_palabras_negativas.txt','r', encoding='utf8') as archivo_en_memoria:
    while True:
        renglon = archivo_en_memoria.readline()
        if not renglon:
         break
        else: 
            elemento = renglon.strip("\n")
            palabras_negativas.append(elemento)


#inicializamos el contador de palabras
numero_positivas = numero_negativas = 0
#Buscamos las palabras positivas y negativas en el texto
for elemento in lista_final1:
    if elemento in palabras_positivas:
        numero_positivas = numero_positivas+1
    if elemento in palabras_negativas:
        numero_negativas = numero_negativas+1

print("Texto 1")
print("\nNúmero de palabras positivas encontradas en:\n",numero_positivas)
print("\nNúmero de palabras negativas encontradas:\n",numero_negativas)
print("\nPolaridad del Texto:\n")
polaridad = numero_positivas -numero_negativas
if polaridad>0: print("Positiva\n")
elif polaridad<0: print("Negativa\n")
else :print("Neutral\n")

#Texto 2
with open('parte_2.txt','r', encoding='utf8') as archivo_en_memoria2:
    texto2 = archivo_en_memoria2.read()

texto_en_minusculas2 = texto2.lower()

#Eliminar simbolos y caracteres especiales
texto_sin_simbolos2 = re.sub(r'[^\w\s]','', texto_en_minusculas2)

# Convertimos a tokens todo el texto
tokens_de_mi_texto2 = word_tokenize(texto_sin_simbolos2)

#cargamos las stopwords del español
palabras_vacias2 = set(stopwords.words('spanish'))

#filtramos los tokens eliminados
lista_final2 = []
for palabra in tokens_de_mi_texto2:
    if palabra not in palabras_vacias2:
        lista_final2.append(palabra)
# Palabras Positivas y negativas para analizar un texto
palabras_positivas = []
with open('texto_002_palabras_positivas.txt','r', encoding='utf8') as archivo_en_memoria:
    while True:
        renglon = archivo_en_memoria.readline()
        if not renglon:
         break
        else: 
            elemento = renglon.strip("\n")
            palabras_positivas.append(elemento)

palabras_negativas = []
with open('texto_003_palabras_negativas.txt','r', encoding='utf8') as archivo_en_memoria:
    while True:
        renglon = archivo_en_memoria.readline()
        if not renglon:
         break
        else: 
            elemento = renglon.strip("\n")
            palabras_negativas.append(elemento)


#inicializamos el contador de palabras
numero_positivas = numero_negativas = 0
#Buscamos las palabras positivas y negativas en el texto
for elemento in lista_final2:
    if elemento in palabras_positivas:
        numero_positivas = numero_positivas+1
    if elemento in palabras_negativas:
        numero_negativas = numero_negativas+1

print("Texto 2")
print("\nNúmero de palabras positivas encontradas en:\n",numero_positivas)
print("\nNúmero de palabras negativas encontradas:\n",numero_negativas)
print("\nPolaridad del Texto:\n")
polaridad = numero_positivas -numero_negativas
if polaridad>0: print("Positiva\n")
elif polaridad<0: print("Negativa\n")
else :print("Neutral\n")


