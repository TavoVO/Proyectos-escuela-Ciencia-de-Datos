#Segmentación de Datos
import re                                   # Manejo de expresiones regulares
import nltk                                 # Paraprocesar lenguaje natural
from nltk.tokenize import word_tokenize     # Para tokenizar un texto
from nltk.corpus import stopwords           # Cargar las "Stopwords" del español

with open('discurso_steve_jobs_stanford_12_junio_2005.txt','r', encoding='utf8') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

texto_sin_simbolos = re.sub(r'[^\w\s]','', texto)
print ('\nEl texto final sin simbolos, ni caracters especiales:\n', texto_sin_simbolos,"\n")

tokens_de_mi_texto = word_tokenize(texto_sin_simbolos)
print("\n impresión de todos los tokens del texto \n\n",tokens_de_mi_texto)
print("\ntokens totales: ", len(tokens_de_mi_texto))

palabras_vacias = set(stopwords.words('spanish'))

#filtramos los tokens eliminados
Lista_final = []
for palabra in tokens_de_mi_texto:
    if palabra not in palabras_vacias:
        Lista_final.append(palabra)

print("\n Lista de tokens sin palabras vacias:\n", Lista_final)

