import json
# Cargar archivo de texto a memoria
archivo_en_texto = "agenda.json"
with open(archivo_en_texto,'r') as archivo_en_memoria:
    texto = archivo_en_memoria.read()

# Parsear el JSON
json_memoria = json.loads(texto)
data = json_memoria['agenda']['contactos']

var=input("¿Nombre del contacto o Ciudad?:")


for x in data:
    if var == x['nombre']:
        print(x['nombre'], x['ciudad'], x['edad'])
    elif var == x['ciudad']:
        print(x['nombre'], x['ciudad'], x['edad'])