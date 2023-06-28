Algoritmo EstudiantesPaseo
	Definir Estudiantes Como Entero
	Escribir "¿cuantos estudiantes van a ir a el paseo?"
	Leer Estudiantes
	
	si Estudiantes >= 100 Entonces
		Pasaje=15000
		a=0
	SiNo
		si Estudiantes >=50 Entonces
			Pasaje=17000
			a=1
		SiNo
			si Estudiantes >=30
				Pasaje =19500
				a=2
			SiNo
				Pasaje= 550000
				a=3
			FinSi
			
		FinSi
	FinSi
	
	Escribir Estudiantes
	
	Segun a Hacer
		0: b=10
			
		1: b=5
			
		2: b=0
			
		3: b=0
			
		4: b=0
			
	FinSegun
	
	
	vaAbs = Pasaje*Estudiantes 
	Escribir "habria que cobrarle a cada estudiante :" Pasaje
	

	
	descuento = b/ 100
	
	descABS = vaAbs* descuento
	
	Escribir "el valor total seria: " vaAbs " mas un decuento del: " b "%"  
	Escribir "seria un total de: "  vaAbs-descABS
	
	
FinAlgoritmo
