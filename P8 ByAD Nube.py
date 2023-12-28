#Palabras importantes de un pagina web
import wikipedia
import re                                   # Manejo de expresiones regulares
import nltk                                 # Paraprocesar lenguaje natural
from nltk.tokenize import word_tokenize     # Para tokenizar un texto
from nltk.corpus import stopwords           # Cargar las "Stopwords" del español
from wordcloud import WordCloud, STOPWORDS  # Crear nubes de ideas
import matplotlib.pyplot as plt             # Graficar

"""""
with open('Salvese Quien Pueda.txt','r', encoding='utf8') as archivo_en_memoria:
    texto = archivo_en_memoria.read()
"""""

# Seleccionar Wikipedia en Español
wikipedia.set_lang("es")

# Extraer información de una página de Wikipedia
texto = wikipedia.summary("Mundial de futbol")

# Impresión completa del texto
print("\Texto Completo\n\n", texto)
#Eliminar simbolos y caracteres especiales
texto_sin_simbolos = re.sub(r'[^\w\s]','', texto)

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
        lista_final.append(palabra.lower())

print("\nLista final eliminando las palabras vacías (norelevantes):\n\n",lista_final)
print("\nTotal de tokens sin las stopswords",len(lista_final))

# Convertir la lista de tokens  a un solo texto separados por un espacio
texto_final = " ".join(lista_final)

# Imprimir el texto final
print("Texto final:\n",texto_final)

#Formato de la "Nube de Ideas"
nube_de_ideas = WordCloud(
    width = 500,
    height = 500,
    random_state = 1,
    background_color = "salmon",
    colormap = "Pastel1",
    collocations = False,
    stopwords = STOPWORDS,
).generate(texto_final)

# Grafica para generar "Nube de ideas"
plt.imshow(nube_de_ideas, interpolation="bilinear")
plt.axis("off")
plt.show()
