Edad = []
Nombre = []
Ciudad = []

nregistros = int(input("Cuantos registros: "))

for x in range(nregistros):
    age= int(input("Edad: "))
    name= input("Nombre: ")
    city= input("Ciudad: ")
    Edad.append(age)
    Nombre.append(name)
    Ciudad.append(city)

suma=0
for i in range(len(Edad)):
    suma= suma+Edad[i]

promedio = suma/nregistros
print("Edad promedio: ",promedio)

Edad.sort(reverse=True)
print("Edad Mayor: ", Edad[0] )

#ciclo para comparar las palabras
print("Ciudades diferentes: ")


