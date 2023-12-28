datos = [89,74,93,80,78,70,69,100]

def promedio(lista):
    suma=0
    for i in lista:
        suma = suma + i
    promedio = suma/len(lista)
    return promedio
print("Lista de datos:\n"+datos)
print("\nElpromedio es:"+promedio(datos)+"\n")