#Segmentación de Datos, Palabras más importantes
import re                                   # Manejo de expresiones regulares
import nltk                                 # Paraprocesar lenguaje natural
from nltk.tokenize import word_tokenize     # Para tokenizar un texto
from nltk.corpus import stopwords           # Cargar las "Stopwords" del español
from collections import Counter             # Para poder contar palabras repetidas
from collections import OrderedDict         # para ordenar el conteo de las palabras repetida

with open('discurso_steve_jobs_stanford_12_junio_2005.txt','r', encoding='utf8') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

texto_sin_simbolos = re.sub(r'[^\w\s]','', texto)

tokens_de_mi_texto = word_tokenize(texto_sin_simbolos)
print("\n impresión de todos los tokens del texto \n\n",tokens_de_mi_texto)
print("\ntokens totales: ", len(tokens_de_mi_texto))

palabras_vacias = set(stopwords.words('spanish'))

#filtramos los tokens eliminados
lista_final = []
for palabra in tokens_de_mi_texto:
    if palabra not in palabras_vacias:
        lista_final.append(palabra.lower())

print("\nLista final eliminando las palabras vacías (norelevantes):\n\n",lista_final)
print("\nTotal de tokens sin las stopswords",len(lista_final))

contador = Counter(lista_final)
print("\nLista de palabras y cuantas veces se repiten en orden descendente por cantidad de repeticiones:\n", contador)
print("Total: ",len(contador))

contador_ordenado = OrderedDict(contador)
print("\nLista de palabras y cuantas veces se repiten conforme van apareciendo en el texto:\n",contador_ordenado)
print("Total: ",len(contador))
