frase = input("Ingresa una frase: ")

def division_frase(frase):
    palabras = frase.split()
    diccionario = {}
    
    for i in palabras:
            diccionario[i] = len(i)
    return diccionario

resultado = division_frase(frase)

print(resultado)