#Limpieza de texto con expresiones regulares
#Biblioteca a utilizar
import re
texto = 'discurso_steve_jobs_stanford_12_junio_2005.txt'
#texto ="Hola! me llamo octavio, tengo 22 años y tengo $16,000.00 pesos en el banco, con un %57 porciento de interes (invesión en el banco) = ¡Cúal es tu pregunta?-*+¨"
texto_sin_simbolos = re.sub(r'[^\w\s]','', texto)
print ('\nEltexto final sin simbolos, ni caracters especiales:\n', texto_sin_simbolos,"\n")
