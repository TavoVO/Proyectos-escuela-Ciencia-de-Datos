#importar la biblioteca de "pandas"
import pandas as pd

#cargar la hoja de excel en un data frame y seleccionar la hoja 1
df = pd.read_excel("prueba_py1.xls","Hoja1")

print("\nDataFrame:\n",df)

#obtener las filas
filas = df.shape[0]
print("\nFilas: "+str(filas))

#obtener columnas
columnas = df.shape[1]
print("\nColumnas: "+str(columnas))

print("\nExtraer un elemento:")
print(df.loc[0][0])

promedio = 0.0

for prom in range(0,int(str(filas))):
    promedio += int(df.loc[prom][5])

print("\nPromedio:",promedio/filas)