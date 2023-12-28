#
#   python_data_science_covid_v3.py
#
#   Lee los últimos datos del COVID en México del repositorio orifical de Johns Hopkins University
#
#   Se requiere la biblioteca covid para Python: https://pypi.org/project/covid/
#   Documentación completa de la biblioteca: https://ahmednafies.github.io/covid/
#   Desde la consola se requiere instalar la biblioteca: covid
#       > pip3 install covid
#
#   Rogelio Ferreira Escutia - abril 2021 - ok
#

# Cargamos la biblioteca para el manejo de datos de Covid
from covid import Covid 

# Creamos nuestro objeto para hacer consultas
covid = Covid()

# Cargamos e imprimimos la lista de "id" de cada país 
lista_id_pais = covid.list_countries()
print("\nLista de id por país:\n\n", lista_id_pais)

# Para extraer los últimos datos sobre México (el id de México = 115)
mexico_casos = covid.get_status_by_country_id(115)
print("\nÚltimos datos sobre México:\n\n", mexico_casos,"\n")