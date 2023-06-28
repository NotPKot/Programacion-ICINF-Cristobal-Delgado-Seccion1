Algoritmo reloj
	
	Escribir "Primero introdusca la hora en cuestion"
	Leer HoraInicial
	
	si HoraInicial >24 Entonces
		ValorValido = Falso
	FinSi
	
	si ValorValido= falso Entonces
		Escribir "porfavor ingrese un valor valido"
	FinSi
	
	si ValorValido = Verdadero Entonces
		Escribir  "Ahora introdusca los minutos en cuestion"
		leer minutos1
		si minutos1 > 59 Entonces
			ValorValido2 = Falso
		FinSi
		
		si ValorValido2= falso entonces 
			Escribir "porfavor introdusca un valor valido"
		FinSi
		
		si ValorValido2= Verdadero entonces 
			escribir "ingrese la segunda hora en cuestion"
			leer HoraInicial2
			
			si HoraInicial2 >59 Entonces
				valorvalido3 = Falso
			FinSi
			
			si valorvalido3= falso Entonces
				Escribir "ingrese un valor valido"
			FinSi
			
			si valorvalido3= verdadero Entonces
				escribir "porfavor ingrese los minutos en cuestion"
				leer minutos2
				
				si minutos2 >59
					valorvalido4=Falso
				FinSi
				
				si valorvalido4=falso entonces 
					escribir "porfavor ingrese un valor valido"
				FinSi
				
				si valorvalido4=verdadero Entonces
					
					Escribir HoraInicial-HoraInicial2 ":" minutos1-minutos2
					
				FinSi
				
				
				
			FinSi
			
			
			
			
			
		FinSi
		
		
		
		
		
		
	FinSi
	
	
	
	

	
FinAlgoritmo
