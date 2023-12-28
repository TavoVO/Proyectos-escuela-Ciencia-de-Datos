#Primer Ejemplo para leer un archivo
""""
archivo_externo = "discursoSteveJobs.txt"

with open(archivo_externo,"rt",encoding='utf8') as archivo_en_memoria:
    filecontets = archivo_en_memoria.read()
    print("\nEl Contenido del archivo: "+archivo_externo+ " es:\n")
    print(filecontets)
"""""
#Segundo ejemplo
"""""
archivo_externo = "temperatura.txt"

with open(archivo_externo,"rt", encoding='utf8') as archivo_en_memoria :
    print("\nEl contenido del archivo: "+archivo_externo+ " es:")
    print("Primer Renglón:")
    primer_renglon = archivo_en_memoria.readline()
    print(primer_renglon)
    print("Segundo Renglón:")
    segundo_renglon = archivo_en_memoria.readline()
    print(segundo_renglon)
"""""

#Ejercicio
archivo_externo = "temperatura.txt"
lista1=[]

with open(archivo_externo,"rt", encoding='utf8') as archivo_en_memoria :
    while archivo_en_memoria.readline():
        renglon = int(archivo_en_memoria.readline())
        lista1.append(renglon)

suma=0
for i in range(len(lista1)):
    suma= suma+lista1[i]

promedio = suma/(len(lista1))
print("Promedio:",promedio)
print(lista1)
    

  
