Algoritmo PromedioEstudiantes
	
	Escribir "ingrese la nota del parcial 1"
	leer nota1
	Escribir "ingrese la nota de parcial 2"
	leer nota2
	Escribir "ingrese la nota de las tareas"
	leer tareas
	Escribir "ingrese la nota de los laboratorios"
	Leer laboratorios
	si ValorValido = NotaFinal>7 y NotaFinal<1 Entonces
		ValorValido=Verdadero
	FinSi
	
	si ValorValido =Falso Entonces
		NotaFinal<-nota1*0.3+nota2*0.5+tareas*0.1+laboratorios*0.1
		Escribir "la nota final del estudiantes es: " NotaFinal
		si NotaFinal < 4.0 Entonces
			desaprobado = Verdadero
			Escribir "El estudiante a desaprobado"
		FinSi
		
		si NotaFinal >= 5.0 Entonces 
			eximido = Verdadero
			Escribir "El estudiante queda eximido"
		FinSi
		
		si eximido=Falso y desaprobado=falso Entonces
			si NotaFinal >= 4 o NotaFinal <=4.9 Entonces
				Escribir "El estudiante debe rendir prueba"
				
			FinSi
			
		FinSi
	FinSi
	
	si ValorValido =Verdadero Entonces
		Escribir  "porfavor ingrese valores validos"
		
	FinSi


	
	//el archivo si toma numeros decimales, ejemplo= 4.6 - 1.2 - 5,6 - 6,7 - Etcetera
	 FinAlgoritmo
