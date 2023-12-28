#Primera practica de Busqueda y Almacenamiento de Datos
"""
Octavio Vieyra Orozco
"""
from traceback import format_tb


print("Hola Octavio")
print('Hola Mundo')

nombre=input("Como te llamas? ")
print("Hola",nombre)

calificacion = 80
if calificacion >=70:
    print("Aprobado")
else:
    print("Reprobado")

#For imprimir 5 numeros
for x in range(5):
    print(x)

for y in range(1,5):
    print(y)

#Leer cadena
for z in "Ponys!":
    print(z)

Cadena = "Ponys!"
for x in Cadena:
    print(x)

#Listas
for x in ["Yo","Tu","El"]:
    print(x)

Lista = ["Yo","Tu","El"]
for i in Lista:
    print(i)

lista = [22, "Octavio", 8.9]
print(lista)

lista1 = []
lista1.append(14)
lista1.append("Morelia")
lista1.append('Octavio')
print(lista)


Edad = []
Nombre = []
Ciudad = []

nregistros = int(input("Cuantos registros"))

for x in nregistros:
    age= input("¿Edad?")
    name= input("Nombre")
    city= input("Ciudad")
    Edad.append(age)
    Nombre.append(name)
    Ciudad.append(city)

suma=0
for Edad in range(nregistros):
    suma=suma+Edad

print("Edad promedio: ")
print("Edad Mayor: ")
print("Ciudades diferentes")


