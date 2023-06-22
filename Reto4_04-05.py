nombre1 = input("ingrese nombre del primer paciente: ")
nombre2 = input("ingrese nombre del segundo paciente: ")
nombre3 = input("ingrese nombre del tercer paciente: ")


Peso1 = input("ingrese el peso del primer paciente: ")
Peso2 = input("ingrese el peso del segundo paciente: ")
Peso3 = input("ingrese el peso del tercer paciente: ")
Estatura1 = input("ingrese la estatura del primer paciente: ")
Estatura2 = input("ingrese la estatura del segundo paciente: ")
Estatura3 = input("ingrese la estatura del tercer paciente: ")


Edad1 = int(input("ingrese la edad del primer paciente: "))
while Edad1<=0 :
    Edad1 = int(input(" ingrese un numero valido"))



Edad2 = int(input("ingrese la edad peso del segundo paciente: "))
while Edad2<=0 :
    Edad2 = int(input(" ingrese un numero valido"))


Edad3 = int(input("ingrese la edad peso del tercer paciente: "))
while Edad3<=0 :
    Edad3 = int(input(" ingrese un numero valido"))


Pacientes = nombre1, nombre2, nombre3
PesoPacientes = Peso1, Peso2, Peso3
EstaturaPacientes = Estatura1, Estatura2, Estatura3
EdadPacientes = Edad1, Edad2, Edad3

print(type(Pacientes))
print(type(PesoPacientes))
print(type(EstaturaPacientes))
print(type(EdadPacientes))

print(" los pacientes", Pacientes, "respectivamente pesan: ", PesoPacientes, ". miden: ", EstaturaPacientes, ". miden: ", EdadPacientes )