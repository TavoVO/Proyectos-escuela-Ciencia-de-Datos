#
# python_datascience_fake_news.py
#
# https://www.kaggle.com/c/fake-news/data?select=train.csv
#   train.csv.zip
#   fakenews.csv
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
print("\nDetección de Fake News\n")
#   1) Objetivo
#       Detectar si una noticia es falsa
#   2) Extracción
df_fakenews = pd.read_csv("fakenews.csv")
# Nota: Las etiquetas de cada noticia ("label") son:
#   1: Noticia falsa (Fake news)
#   0: Noticia verdadera
#   3) Análisis
print("Cantidad de datos: ", df_fakenews.shape)
print("Tipos de datos:\n", df_fakenews.info)
print("Datos de ejemplo:\n", df_fakenews.head())
print("Datos Faltantes:\n", pd.isnull(df_fakenews).sum())
#   4) Pre-Procesamiento
# Reemplazar valores nulos con valores vacíos
df_fakenews = df_fakenews.fillna('')
# Uniendo columnas del nombre de autor y el título
df_fakenews['contenido'] = df_fakenews['author'] + df_fakenews['title']
# Imprimir las datos ya con las columnas unidas
print(df_fakenews['contenido'])
# Separamos datos y etiquetas
X = df_fakenews.drop(columns='label', axis=1)
Y = df_fakenews['label']
# Para reducir la complejidad se reducirán las palabras a su palabra raíz
#   Este proceso en inglés se denomina "steemming" (derivación)
port_stem = PorterStemmer()
def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content
df_fakenews['contenido'] = df_fakenews['contenido'].apply(stemming)
print("Después del Stemming:\n", df_fakenews['contenido'])
#   5) Modelado
# Separando los datos y las etiquetas
X = df_fakenews['contenido'].values
Y = df_fakenews['label'].values
# Vectorizando (convirtiendo texto a valores numéricos)
vectorizer = TfidfVectorizer()
vectorizer.fit(X)
X = vectorizer.transform(X)
print("\nTexto ya vectorizado:\n", X)

#Separado de datos para entrenamiento y prueba
X_entrenamiento, X_pruebas, Y_entrenamiento, Y_pruebas = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)

#Entrenamiento
modelo = LogisticRegression()
modelo.fit(X_entrenamiento,Y_entrenamiento)

#Porcentaje de Exactitud de los datos de entrenamiento
X_entrenamiento_prediccion = modelo.predict(X_entrenamiento)
entrenamiento_exactitud = accuracy_score(X_entrenamiento_prediccion, Y_entrenamiento)
print("\nPorcentaje de Exactitud con datos de entrenamiento: ",entrenamiento_exactitud)

#Porcentaje de Exactitud de los datos de prueba
X_pruebas_prediccion = modelo.predict(X_pruebas)
pruebas_exactitud = accuracy_score(X_pruebas_prediccion,Y_pruebas)
print("\nPorcentaje de Exactitud con datos de prueba: ",pruebas_exactitud)

#6) Resultados
X_prediccion = X_pruebas[0]
prediccion = modelo.predict(X_prediccion)
print("\nResultado de la predicción:",prediccion)

if(prediccion[0]==0):
    print("\nLa notiica es ReaL!\n")
else:
    print("\nLa noticia es Falsa!\n")