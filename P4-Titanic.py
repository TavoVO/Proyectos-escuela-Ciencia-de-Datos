import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

print("\nTitanic\n")
# 1) Objetivo
"""
Preddecir si una persona podria sobrevivir al naufragio del Titanic
"""
# 2) Extracción
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

# 3) Análisis
print("\nCantidad de Datos: ")
print("\nEntrenamiento - Número de (Filas, Columnas)",df_train.shape)
print("\nPrueba - Número de (Filas, Columnas)",df_test.shape)

print("\nTipos de Datos:")
print("\nEntrenamiento: ",df_train.info)
print("\nPruebas: ",df_test.info)

print("\nDatos faltantes:")
print("\nDatos entrenamiento: ",pd.isnull(df_train).sum())
print("\nDatos Pruebas: ",pd.isnull(df_test).sum())

print("\nEstadsticas del Dataset:")
print("\nEntrenamiento: \n", df_train.describe())
print("\nPruebas: \n",df_test.describe())


# 4) Pre-Procesamiento

# Cambiar el sexo por números (0 para mujeres y 1 para hombres)
df_train['Sex'].replace(['female','male'],[0,1],inplace=True)
df_test['Sex'].replace(['female','male'],[0,1],inplace=True)

#Cambiar datos de embarque
df_train['Embarked'].replace(['Q','S','C'],[0,1,2],inplace=True)
df_test['Embarked'].replace(['Q','S','C'],[0,1,2],inplace=True)

#Remplazo de los datos faltantes en la edad por media de esta columna
print("Promedio de Edad (Entrenamiento):",df_train['Age'].mean())
print("Promedio de Edad (Prueba):",df_test['Age'].mean())

# Entrenamiento: 29.69911764705882 - Pruebas: 30.272590361445783
#   por lo tanto redondeamos todo a 30
promedio = 30
df_train['Age'] = df_train['Age'].replace(np.nan,promedio)
df_test['Age'] = df_train['Age'].replace(np.nan,promedio)

# Crear varios grupos de acuerdo a las edades
# Bandas: 0-8 9-15 16-18 19-25 26-40 41-60 61-100
bandas = [0, 8, 15, 18, 25, 40, 60, 100]
etiquetas = ['1','2','3','4','5','6','7']
df_train["Age"] = pd.cut(df_train["Age"],bandas,labels=etiquetas)
df_test["Age"] = pd.cut(df_test["Age"],bandas,labels=etiquetas)

# Eliminar la columna de "Cabin" ya que tinen muchos datos perdidos
df_train.drop(['Cabin'],axis=1,inplace=True)
df_test.drop(['Cabin'],axis=1,inplace=True)

# Eliminar columnas inecesarias
df_train.drop(['PassengerId','Name','Ticket'],axis=1)
df_test.drop(['Name','Ticket'],axis=1)

# Eliminar las filas que contienen datos perdidos
df_train.dropna(axis=0,how='any',inplace=True)
df_test.dropna(axis=0, how='any',inplace=True)
# Verificar los datos
print("\nimpresión de datos verificados:\n")
print(pd.isnull(df_train.sum()))
print(pd.isnull(df_test.sum()))
print(df_train.shape)
print(df_test.shape)
print(df_train.head())
print(df_test.head())

# 5) Modelado
# Separar ña columna con la información de los sobrevivientes
X = np.array(df_train.drop(['Survived'], 1))
y = np.array(df_train['Survived'])

# En este caso se definio un tamaño de 80% entrenamiento y 20% prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Regresión logística
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
Y_pred = logreg.predict(X_test)
print('\nPrecisión Regresión Logística: ', logreg.score(X_train, y_train))

# Support Vector Machines
svc = SVC()
svc.fit(X_train, y_train)
Y_pred = svc.predict(X_test)
print('Precisión Soporte de Vectores: ', svc.score(X_train, y_train))

# KNN
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, y_train)
Y_pred = knn.predict(X_test)
print('Precisión Vecinos más Cercanos: ', knn.score(X_train, y_train))
# 6) Resultados
