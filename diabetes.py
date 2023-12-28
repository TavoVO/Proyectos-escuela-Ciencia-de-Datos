import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# 1) Objetivo 
"""
Predicción de casos de Diabetes
"""
print("\nPredicción casos de Diabetes\n")

# 2) Extracción
#leer el dataset
df_diabetes = pd.read_csv('diabetes.csv')

# 3) Analisis
print("\nDataSet:\n",df_diabetes.head())
# Donde
"""
1 -> outcome = Tiene Diabetes
0 -> outcome = No Tiene Diabetes
"""

print("\nCantidad de Datos:\n",df_diabetes)
print("\nEstadíticas del Dataset:\n",df_diabetes.describe())
print("\nCantidad de personas con diabetes:\n",df_diabetes['Outcome'].value_counts())
print("\nValores Promedios de No Diabéticos y Diabéticos:\n",df_diabetes.groupby('Outcome').mean())

# 4) Pre-procesamiento
X = df_diabetes.drop(columns='Outcome',axis=1)
Y = df_diabetes['Outcome']

# Estandarizado de lso datos(Normalización de los datos, Promedio = 0 y Desviación estandar = 1)
escalador = StandardScaler()
escalador.fit(X)
datos_estandarizados = escalador.transform(X)
print("\nDatos Estandarizados:\n",datos_estandarizados)

X = datos_estandarizados
Y = df_diabetes['Outcome']

# 5) Modelado
# Separando datos para el entrenamiento y prueba
X_entrenamiento, X_pruebas, Y_entrenamiento, Y_pruebas = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)
print("\nImprimiendo datos totales, datos de entrenamiento y de prueba:\n",X.shape, X_entrenamiento.shape, X_pruebas.shape)

# Sleccionando  y confugurando el Modelo a utilizar
modelo = svm.SVC(kernel='linear')
# Entrenamiento del Modelo
modelo.fit(X_entrenamiento, Y_entrenamiento)

# 6) Resultados
# Porcentaje de Exactitud de los datos de entrenamiento
X_entrenamiento_prediccion = modelo.predict(X_entrenamiento)
entrenamiento_exactitud = accuracy_score(X_entrenamiento_prediccion, Y_entrenamiento)
print("\nPorcentaje de Eaxctitud con datos de entrenamiento: ",entrenamiento_exactitud)
# Porcentaje de Exactitud de los datos de Pruebas
X_prueba_prediccion = modelo.predict(X_pruebas)
prueba_exactitud = accuracy_score(X_prueba_prediccion, Y_pruebas)
print("\nPorcentaje de Eaxctitud con datos de Prueba: ",prueba_exactitud)

#Predicción con nuevos datos
"""
Pregnancies = 0
Glucose = 85
BloodPressure = 69
SkinThickness = 15
Insulin = 100
BMI = 23
DiabetesPedigreeFunction = 0.009
Age = 22
"""
# Datos de entrada
datos_entreda = (0,85,69,15,100,23,0.009,22)

# Cambiando los datos de entrada a un arreglo en numpy
datos_entreda_erreglo_numpy = np.asanyarray(datos_entreda)

# Redimensionar el arreglo
datos_entrada_redimensionados = datos_entreda_erreglo_numpy.reshape(1,-1)

# Estandarizando los datos ( normalizando los datos)
datos_entrada_estandarizados = escalador.transform(datos_entrada_redimensionados)

# Haciendo la predicción
prediccion = modelo.predict(datos_entrada_estandarizados)
print("\nPredicción:",prediccion)
