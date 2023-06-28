diccionario ={ 
"NEstudiante": "" ,
"Nasignatura" : "" ,
"Nota lab 1": "" ,
"Nota lab 2" : "" ,
}
diccionario["nombre del estudiante"] = input("Nombre del estudiante ")
diccionario["Nombre asignatura"] = input("Nombre asignatura")
diccionario["Nota lab 1"] = input("Nota lab 1")
diccionario["Nota lab 2"] = input("Nota lab 2")
Notafinal =float(diccionario["Nota laboratorio 1"]) *0.3 + float(diccionario["Nota lab 2"]) * 0.7

diccionario["promedio ponderado"] = f"{Notafinal:.1f}"

print(diccionario)