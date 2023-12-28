from random import randint
import matplotlib.pyplot as plt

grupo=[["Jenny",0],["Jessica",0],["Karla",0],["Roy",0],["Jorge",0],["Jacky",0],["Axel",0],["Kenneth",0],["Angel",0],["Ivan",0],["Octavio",0],["Alexandro",0],["Maria",0]]
ganadores = []

for x in range(0,100):
    valor = int(randint(1,len(grupo)))
    ganadores.append(grupo[valor-1][0])

for x in ganadores:
    if x == "Jenny":
        grupo[0][1] = grupo[0][1]+1
    elif x == "Jessica":
        grupo[1][1] = grupo[1][1]+1
    elif x == "Karla":
        grupo[2][1] = grupo[2][1]+1
    elif x == "Roy":
        grupo[3][1] = grupo[3][1]+1
    elif x == "Jorge":
        grupo[4][1] = grupo[4][1]+1
    elif x == "Jacky":
        grupo[5][1] = grupo[5][1]+1
    elif x == "Axel":
        grupo[6][1] = grupo[6][1]+1
    elif x == "Kenneth":
        grupo[7][1] = grupo[7][1]+1
    elif x == "Angel":
        grupo[8][1] = grupo[8][1]+1
    elif x == "Ivan":
        grupo[9][1] = grupo[9][1]+1
    elif x == "Octavio":
        grupo[10][1] = grupo[10][1]+1
    elif x == "Alexandro":
        grupo[11][1] = grupo[11][1]+1
    else:
        grupo[12][1] = grupo[12][1]+1


print("\nLista de participantes:\n"+str(grupo))

persona = []
veces = []
vecesg = []
for x,y in  grupo:
    persona.append(x)
    veces.append(y)
    vecesg.append(y)
    print("\n"+x+" gano: "+str(y)+" veces")

for x,y in grupo:
    vecesg.sort(reverse=True)
    i = vecesg[0]
    if i == y:
        print("El ganador es "+x+" con "+str(y))


contador = 0
for ciclo in persona:
    plt.plot(ciclo, veces[contador], marker="o", color="red")
    contador = contador + 1

# Colocamos un título a nuestra gráfica y a nuestros ejes
plt.title("Gráfica de Personas y Veces que gano la rifa")
plt.xlabel("Persona")
plt.ylabel("Veces ganadas")

# Mostramos la gráfica en pantalla
plt.show()