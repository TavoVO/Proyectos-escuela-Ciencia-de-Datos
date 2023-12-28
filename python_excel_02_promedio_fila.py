#
#   python_excel_02_promedio_fila.py
#
#   Lee una hoja de cálculo en formato de Excel y calcula el promedio de la primer fila
#
#   Rogelio Ferreira Escutia - diciembre 2021
#
#   Se requiere "pandas" > pip3 install pandas
#   Se requiere "xlrd" > pip3 install xlrd
#

# Cargar la biblioteca de "pandas"
import pandas as pd

# cargar la hoja de excel en un dataframe y seleccionar la Hoja1
df = pd.read_excel("excel_hoja_01_calificaciones.xls", "Hoja1")

# Calcular el promedio de todas las filas
promedio = df.mean(axis=1)

# Imprimir el promedio de la primer fila
print("\nEl promedio de la primer fila es:", promedio[0], "\n")