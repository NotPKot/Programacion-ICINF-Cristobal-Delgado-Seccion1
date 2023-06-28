palabra1= input("ingrese su palabra: ")

palabra_revertida = palabra1[::-1]

if palabra_revertida == palabra1:
    print("su palabra ", palabra1 ," es palindromo")
else:
    print("su palabra", palabra1 ,"no es palindromo")