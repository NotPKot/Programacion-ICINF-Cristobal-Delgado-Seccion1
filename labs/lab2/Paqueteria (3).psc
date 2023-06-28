Algoritmo Paqueteria
	Definir b Como Entero
	Escribir "escriba el numero de hacia adonde quiere enviar su paquete, entre las siguientes opciones"
	Escribir "1. Norteamérica"
	Escribir "2. Centroamérica"
	Escribir "3. Sudamérica"
	Escribir "4. Europa"
	Escribir "5. Asia"
	
	Leer b
	
	si b>5 o b<=0 Entonces
		Mientras b>5 o b<=0 Hacer
			Escribir "porfavor ingrese un valor valido"
			leer b
		FinMientras
	FinSi
	
	
	Escribir "ahora mencione que opcion quiere enviar entre un"
	Escribir "1.documento"
	Escribir "2.encomienda"
	Definir c Como Entero
	leer c
	
	si c>2 o c<=0 Entonces
		Mientras c>2 o c<=0 Hacer
			Escribir "porfavor ingrese un valor valido"
			leer c
		FinMientras
	FinSi
	
	Segun c Hacer
		1: a=0
			
		2: a=1
	FinSegun
	
	
	
	segun b Hacer
		1: CoEncomiendo= 40
			CoDocumento= 20
			
			
		2:CoEncomiendo=30
			CoDocumento=15
			
		3:CoEncomiendo= 20
			CoDocumento=10
			
		4:CoEncomiendo=60
			CoDocumento=30
			
		5:CoEncomiendo=70
			CoDocumento=35
			
	FinSegun
	
	Escribir "ahora, ingrese el peso de su paquete en gramos, sin puntos" 
	Escribir "recuerde que su documento no puede superar los 1500 gramos, ni su encomienda los 50000"
	
	Definir pesoGR Como Entero
	Leer pesoGR
	
	si a=0 Entonces
		si pesoGR>=1500 Entonces
			escribir "no aceptamos esa cantidad de peso, lo sentimos mucho"
			
		SiNo
			ValorT= pesoGR*CoDocumento
			Escribir "el coste total de envio seria: " ValorT
			
		FinSi
		
	FinSi
	
	si a=1 Entonces
		si pesoGR>=50000 Entonces
			Escribir "no aceptamos esa cantidad de peso, lo sentimos mucho"
		SiNo
			ValorT= pesoGR*CoEncomiendo
			Escribir "el coste total de envio seria: " ValorT
		FinSi
		
	FinSi
	
	
	
FinAlgoritmo
