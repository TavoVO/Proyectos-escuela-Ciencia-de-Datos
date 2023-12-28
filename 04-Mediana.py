datos = [40,17,35,16]
datos = [40,17,35,16,30]

def mediana(lista):
    lista_orednada = sorted(lista)
    print("Lista Ordenada: "+lista_orednada)
    if len(lista_orednada)%2 == 0:
        i = int(len(lista_orednada))/2 - 1
        j = i + 1
        mediana = (lista_orednada[i]+lista_orednada[j])/2
    else:
        i = int(len(lista_orednada))/2
        mediana = lista_orednada[i]
    return mediana

print("\n Lista de datos: ",datos)
print("\nLa mediana es: "+mediana(datos))