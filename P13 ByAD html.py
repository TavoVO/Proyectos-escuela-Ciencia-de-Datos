#Web Scrapping
from urllib.request import urlopen
from bs4 import BeautifulSoup

pagina_inicial = "http://sagitario.itmorelia.edu.mx/~rogelio/hola.htm"

url = urlopen(pagina_inicial)
print("\nExtraer los enlaces de la página web: "+pagina_inicial)

bs = BeautifulSoup(url.read(),'html.parser')
for enlaces in bs.find_all("a"):
    print(enlaces)

print(bs.title)
print(bs.h1)
print(bs.h2)
print(bs.h3)

