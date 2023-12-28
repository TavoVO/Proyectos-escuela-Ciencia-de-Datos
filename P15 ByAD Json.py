import json

archivo_en_texto = "lenguajes.json"
with open(archivo_en_texto,'r') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

#Parsear Json
json_memoria = json.loads(texto)

#Imprimir en formato json
print(json.dumps(json_memoria, indent=4, sort_keys=True))

#Imprimir los lenguajes
print(json_memoria ['web']['lenguages'][0])

#Impresión por linea
data = json_memoria ['web']['lenguages']
for x in data:
    print(x['id'],x['name'],x['website'])