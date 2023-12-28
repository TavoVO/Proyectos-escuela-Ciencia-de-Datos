import mysql.connector
import re
import nltk #Procesar lenguaje natural
from nltk.tokenize import word_tokenize #Tokenizar texto
from nltk.corpus import stopwords #Cargar stopwords
from urllib import request

palabra1 = 'messi'
palabra2 = 'albiceleste'
palabra3 = 'argentina'
texto_enlace = []

def conectar_dbms():
    import mysql.connector
    servidor="localhost"
    usuario="root"
    clave=""
    base="motor"
    print("Conectándose al DBMS con los siguientes datos: ")
    print("Servidor=",servidor,"- Usuario=",usuario,"- Clave=",clave,"- Base=",base)
    mi_conexion = mysql.connector.connect(
        host=servidor,
        user=usuario,
        passwd=clave,
        database=base
    )
    return mi_conexion
#Conectarse a Base de datos
mi_conexion = conectar_dbms()

def leer_primer_enlace(mi_conexion):
    try:
        if mi_conexion.is_connected():
            operacion = mi_conexion.cursor()
            operacion.execute("SELECT * FROM indice WHERE analizado=0 LIMIT 1")
            for url, analizado, palabra1, palabra2, palabra3 in operacion.fetchall():
                primer_enlace = url
    except Error as e:
        print("Error al conectarse a MySQL: ",e)
    return primer_enlace

#Extraer el primer enlace
primer_enlace = leer_primer_enlace(mi_conexion)
print("Primer Enlace: ",primer_enlace)

def extraer_enlaces(enlace):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    url=urlopen(enlace)
    print("\nExtraer los enlaces de la página web: ",enlace)
    bs = BeautifulSoup(url.read(),'html.parser')

    for titulos in bs.find_all("h1"):
        texto = re.sub(r'<.*?>','',str(titulos))
        texto = texto.replace("\n","")
        texto = texto.replace("\t","")
        texto = texto.strip()
        texto_enlace.append(texto)
    
    for titulos in bs.find_all("h2"):
        texto = re.sub(r'<.*?>','',str(titulos))
        texto = texto.replace("\n","")
        texto = texto.replace("\t","")
        texto = texto.strip()
        texto_enlace.append(texto)

    for textos in bs.find_all("p"):
        texto = re.sub(r'<.*?>','',str(textos))
        texto = texto.replace("\n","")
        texto = texto.replace("\t","")
        texto = texto.strip()
        texto_enlace.append(texto)

    textos_enlaces = " ".join(texto_enlace)
    texto_minusculas = str.lower(textos_enlaces)

       #Eliminar caracteres especiales usando expreciones regulares
    texto_sin_simbolos = re.sub(r'[^\w\s]','', texto_minusculas)

    #Convertir el texto a tokens
    tokens_de_mi_texto = word_tokenize(texto_sin_simbolos)
    
    #Cargar stopwords del español
    palabras_vacias = set(stopwords.words('spanish'))

    lista_final=[]
    lista_enlaces_chidos = []

    #Eliminando stopwords
    for palabra in tokens_de_mi_texto:
        if palabra not in palabras_vacias:
            lista_final.append(palabra)
    
    
    enlaces_encontrados = []
    contador = 0
    for enlaces in bs.find_all("a"):
        enlace = format(enlaces.get("href"))
        if enlace[-3:]!="jpg" and enlace[-3:]!="png" and enlace[-3:]!="svg" and enlace[-3:]!="pdf" and enlace[-3:]!="ppt" and enlace[-4:]!="pptx" and enlace[-3:]!="txt" and enlace[-3:]!="xls" and enlace[-4:]!="docx" and enlace[-3:]!="doc"  and enlace[-4:]!="xlsx" and enlace[-3:]!="wmv" and enlace[-3:]!="mp3" and enlace[-3:]!="mp4" :
            enlaces_encontrados.append("{}".format(enlaces.get("href")))
            print("{}".format(enlaces.get("href")))
            contador = contador+1
        
        if palabra1 in lista_final and palabra2 in lista_final and palabra3 in lista_final:
            print("Estan las tres palabras")
            lista_enlaces_chidos.append(enlace)
            almacenar_enlaces_chidos (mi_conexion,lista_enlaces_chidos,lista_final)
        
    print("Enlaces con palabras")
    print(lista_enlaces_chidos)
    print("\nEnlaces encontrados: ",contador)

    texto_enlace.clear()
    textos_enlaces=''
    lista_final.clear()
    lista_enlaces_chidos.clear()

    return enlaces_encontrados,lista_enlaces_chidos,lista_final

#Encontrar y extraer los enlaces encontrados
enlaces_encontrados = extraer_enlaces(primer_enlace)

def almacenar_enlaces_chidos (mi_conexion,enlaces_encontrados):
    try:
        if mi_conexion.is_connected():
            operacion = mi_conexion.cursor()
            for i in range(len(enlaces_encontrados)):
                sql="INSERT INTO indice2 (url, texto) VALUES('"+enlaces_encontrados[i]+"',0,'','','')"
                print(sql)
                operacion.execute("INSERT INTO indice2 (url, texto) VALUES('"+enlaces_encontrados[i]+"','"++"',)")
                mi_conexion.commit()

    except Error as e:
        print("Error al conectarse a MySQL: ",e)
    return

def almacenar_enlaces(mi_conexion, enlaces_encontrados):
    try:
        if mi_conexion.is_connected():
            operacion = mi_conexion.cursor()
            for i in range(len(enlaces_encontrados)):
                sql="INSERT INTO indice (url, analizado, palabra, palabra1, palabra2, palabra3) VALUES('"+enlaces_encontrados[i]+"',0,'','','')"
                print(sql)
                operacion.execute("INSERT INTO indice (url, analizado, palabra, palabra1, palabra2, palabra3) VALUES('"+enlaces_encontrados[i]+"',0,'','','')")
                mi_conexion.commit()

    except Error as e:
        print("Error al conectarse a MySQL: ",e)
    return



def marcar_enlace_revisado(mi_conexion, enlace_a_marcar):
    try:
        if mi_conexion.is_connected():
            operacion = mi_conexion.cursor()
            sql = "UPDATE indice SET analizado=1 WHERE url='"+enlace_a_marcar+"' LIMIT 1"
            operacion.execute(sql)
            mi_conexion.commit()
    except Error as e:
        print("Error al conectarse a MySQL: ",e)
    return

mi_conexion = conectar_dbms()
for x in range(10):
    primer_enlace = leer_primer_enlace(mi_conexion)
    print("Primer Enlace: ", primer_enlace)
    # Encontrar y extraer los enlaces encontrados
    enlaces_encontrados = extraer_enlaces(primer_enlace)
    #Maracar enlace como revisado
    #Almacenar enlaces
    almacenar_enlaces(mi_conexion, enlaces_encontrados)
    enlace_a_marcar = primer_enlace
    marcar_enlace_revisado(mi_conexion, enlace_a_marcar)

