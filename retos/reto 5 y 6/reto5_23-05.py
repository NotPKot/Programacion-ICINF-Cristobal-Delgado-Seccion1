Input_Numero = int(input("Ingrese un número: "))

if Input_Numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

Es_Primo = True
if Input_Numero < 2:
    Es_Primo = False
else:
    for i in range(2, Input_Numero):
        if Input_Numero % i == 0:
            Es_Primo = False
            break

if Es_Primo:
    print("El numero es primo")
else:
    print("El numero no es primo")

if Input_Numero > 50:
    print("El numero es mayor que 50")
elif Input_Numero < 50:
    print("El numero es menor que 50")
else:
    print("El numero es igual a 50")



