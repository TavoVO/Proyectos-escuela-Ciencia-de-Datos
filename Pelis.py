import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#1) Objetivo
# Recomendación de peliculas
print("\nRecomendar películas")

#2) Extracción
df_peliculas = pd.read_csv('movies.csv')

#3) Análisis
# Imprimimos los primeros registros

print("\nPrimeros registros:\n",df_peliculas.head())
print("\nCantidad de datos:\n",df_peliculas.shape)

#4) Pre-procesamiento
#Se seleccionan las caracteristicas más importantes
caracteristicas_importantes = ['genres','keywords','tagline','cast','director']

#Reemplazar los valores que sean nulos de las caracteristicas seleccionadas
for i in caracteristicas_importantes:
    df_peliculas[i] = df_peliculas[i].fillna('')

#Uniendo varias caracteristicas en un solo campo
union_caracteristicas = df_peliculas['genres']+''+df_peliculas['keywords']+''+df_peliculas['tagline']+''+df_peliculas['cast']+''+df_peliculas['director']
print("\nUnion de caracteristicas:\n",union_caracteristicas)

#5) Modelado
#Vectorizador ( convirtiendo texto a valores numéricos)
vectorizar = TfidfVectorizer()
vectores = vectorizar.fit_transform(union_caracteristicas)
print("\nTexto ya vectorizado:\n",vectores)

#Aplicar "similitud Coseno" para comprar todos los vectores
matriz_similitud = cosine_similarity(vectores)
#Imprimir la Matriz de similitud
print("\nMatriz de Similitud:\n",matriz_similitud)

#Preguntar al usuario el nombre de su película favorita
pelicula_usuario = input("\nEscribe el nombre de tu película favorita:")

#Crear una lista de todas las peliculas del dataset
lista_peliculas = df_peliculas['title'].tolist()

#Encontrar las pelicular parecidas
peliculas_parecidas = difflib.get_close_matches(pelicula_usuario, lista_peliculas)
print("\nPeliculas parecidas:\n",peliculas_parecidas)

#Encontrando la pelicula más parecida
pelicula_mas_parecida = peliculas_parecidas[0]

#Buscando el índice de la pelicula más parecida
indice_pelicula = df_peliculas[df_peliculas.title == pelicula_mas_parecida]['index'].values[0]
print("\nIndice de la pelicula más parecidas: ",indice_pelicula)

#Crear una lista de las peliculas parecidas (comparando sus vectores por similitud coseno)
similitud_peliculas = list(enumerate(matriz_similitud[indice_pelicula]))
print("\nVectores de Similitud:\n",similitud_peliculas)

#Ordenar los vectores
similitud_peliculas_ordenado = sorted(similitud_peliculas, key=lambda x:x[1], reverse=True)
print("\nvectores de Similitud Ordenados:\n",similitud_peliculas_ordenado)

#6) Resultados
#Imprimir peliculas recomendadas
print("\nPelículas Recomendadas:\n")
i=1
for pelicula in similitud_peliculas_ordenado:
    indice = pelicula[0]
    titulo_pelicula = df_peliculas[df_peliculas.index==indice]['title'].values[0]
    if(i<30):
        print(i, '.- ',titulo_pelicula)
        i+=1