from covid import Covid

covid=Covid()
print(covid.list_countries())
mexico=covid.get_status_by_country_id(118)
print(mexico)