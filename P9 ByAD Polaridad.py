import re                                   # Manejo de expresiones regulares
import nltk                                 # Paraprocesar lenguaje natural
from nltk.tokenize import word_tokenize     # Para tokenizar un texto
from nltk.corpus import stopwords           # Cargar las "Stopwords" del español

with open('texto_001_don_quijote.txt','r', encoding='utf8') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

texto_en_minusculas = texto.lower()

#Eliminar simbolos y caracteres especiales
texto_sin_simbolos = re.sub(r'[^\w\s]','', texto_en_minusculas)

# Convertimos a tokens todo el texto
tokens_de_mi_texto = word_tokenize(texto_sin_simbolos)
print("\n impresión de todos los tokens del texto \n\n",tokens_de_mi_texto)
print("\ntokens totales: ", len(tokens_de_mi_texto))

#cargamos las stopwords del español
palabras_vacias = set(stopwords.words('spanish'))

#filtramos los tokens eliminados
lista_final = []
for palabra in tokens_de_mi_texto:
    if palabra not in palabras_vacias:
        lista_final.append(palabra)

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
for elemento in lista_final:
    if elemento in palabras_positivas:
        numero_positivas = numero_positivas+1
    if elemento in palabras_negativas:
        numero_negativas = numero_negativas+1

print("\nNúmero de palabras positivas encontradas:\n",numero_positivas)
print("\nNúmero de palabras negativas encontradas:\n",numero_negativas)
print("\n\nPolaridad del Texto:\n")
polaridad = numero_positivas -numero_negativas
if polaridad>0: print("\nPositiva\n")
elif polaridad<0: print("\nNegativa\n")
else :print("\nNeutral\n")




        



