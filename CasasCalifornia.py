import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1) Objetivo
"""
Predecir el costo de las casas
"""
# 2) Extracción
# Cargar el archivo
df_casas = pd.read_csv('housing.csv')

# 3) Análisis
print("\nCatidad de Datos (Filas,Columnas):",df_casas.shape)
print("\nTipos de datos:", df_casas.info)
print("\nDatos Faltantes:",pd.isnull(df_casas).sum())
print("\nEstadisticas:\n",df_casas.describe())

print("\nCampo ocean_proximity:",df_casas['ocean_proximity'])
print("\nCantidad ocean_proximity:\n", df_casas['ocean_proximity'].value_counts())

def grafica_1(datos, x, y):
    plt.plot(datos[x], datos[y],'o')
    plt.xlabel(x, size=15)
    plt.ylabel(y, size=15)
    plt.title(x+' vs '+y,size=20)
    plt.show

grafica_1(df_casas,'median_house_value','median_income')
grafica_1(df_casas,'median_house_value','housing_median_age')
grafica_1(df_casas,'median_house_value','total_rooms')
grafica_1(df_casas,'median_house_value','population')

print("\nCorrelación:\n", df_casas.corr())
matriz_de_correlaciones = df_casas.corr()
print("\nCorrelación General: ", matriz_de_correlaciones)
print("\nCorrelación de 'median_house_value': ",matriz_de_correlaciones['median_house_value'].sort_values(ascending=False))
# 4) Pre-Procesamiento


# 5) Modelado


# 6) Resultados
