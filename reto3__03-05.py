lista_ciudades = ["Santiago", "Temuco", "Osorno", "Punta arena"]
lista_indiceAire = ["134", "99", "234", "50"]

minimo = lista_indiceAire.index(min(lista_indiceAire))
print(f"la ciudad con el indice mas bajo es {lista_ciudades[minimo]} con un indice de {lista_indiceAire}")
