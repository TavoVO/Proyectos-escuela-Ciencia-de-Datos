from collections import defaultdict

datos = [1,3,2,5,7,0,2,3]

def moda(lista):
    contador = defaultdict(lambda:0)
    print(contador)
    for s in lista:
        contador[s] += 1
        print(contador) 
    
    contador_max = max(contador.values())
    print(contador_max)
    modas = [v for v in set(lista) if contador[v] == contador_max]
    return modas

print(moda(datos))