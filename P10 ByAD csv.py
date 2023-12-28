# Tipos de Archivo
import csv
from csv import reader

with open('COVID.csv','r', encoding='utf8') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

csv = reader(archivo_en_memoria)
lista = list(csv)

print(lista[0][0])

promedio = 0.0

for edad in range (1, len (lista)):
    promedio += int(lista[edad][15])

print("Promedio: ", promedio/edad)