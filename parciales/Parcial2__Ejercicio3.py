Temperaturas_Minimas = {9, 5, 2, 7, 6, 1}
Temperaturas_Maximas = {12, 14, 11, 10, 15, 9}

temperaturas_iguales = Temperaturas_Maximas.intersection(Temperaturas_Minimas)

print("el numero:",temperaturas_iguales, " si esta en ambos sets")

Temperaturas = Temperaturas_Maximas.union(Temperaturas_Minimas)

if 6 or 17 in Temperaturas:
    print("el numero 6 o 17 si se encuentra en alguna de estas listas")

Temperaturas_Elevadas_maximas = {i * i for i in Temperaturas_Maximas}
Temperaturas_Elevadas_minimas = {i * i for i in Temperaturas_Minimas}

print("las temperaturas maximas elevadas por si mismas dan:",Temperaturas_Elevadas_maximas)
print("las temperaturas minimas elevadas por si mismas dan:", Temperaturas_Elevadas_minimas)

print("las temperaturas juntas dan:",Temperaturas)