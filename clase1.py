#esto es declarar una variable

nombre = "PKot"
name = "Chaos"

#llamando a la variable ya usada

print("hola soy", nombre)

edad = "18"

#imprimiendo 2 variables en una misma sentencia
# + "" + es para hacer un espacio y str es para que la computadera pueda leer numeros
print("hola soy"+ " "+ nombre + ", " + "tengo" +" "+ str(edad ) )

print("mi nuevo nombre es", name)

#utilizando la instruccion input
name= input("¿cual es tu nuevo nombre?\n")
print("tu nombre es:", name)

#datos de tipo numerico
estatura = 1.75
peso = 70
complejo = 1 + 4j

#datos de tipo cadena
imc = peso/estatura
print("mi imc es de", imc,"\n")

print ("mi IMC es de: {:.2f}".format(imc,"\n"))


#datos de tipo cadena de caracteres
asignatura= "programacion"
carrera = "Ingenieria civil en informatica"

#datos de tipo string
print("hola,soy estudiante de la carrera de", carrera, "estoy en la clase de", asignatura, "un (1) cordial saludo")
print("la cantidad de caracteres ")

#valores booleanos
ampolleta = False
interruptor = True
print("la variable ampolleta es de tipo :",type(interruptor),"\n")

print(type(ampolleta) )
print (type(imc))
print(type(carrera))
print(type(peso))

#datos tipo array
estudiantes = ["Cristobal", "Marco", "Jose", "Yaeger", "Marco"]
num = [1,2,3,4,5,6]
lenguaje = ["python"]
print(estudiantes)
print(num)
print(estudiantes.count("Marco"))

print("posicion (3)",estudiantes[3])
print ("posicion (-2)",estudiantes[-2])


#declarando e inicalizando una lita
nueva_lista = []
print("Esta es una lista vacia:",nueva_lista)

otra_lista = []
print("esta es otra lista vacia:",otra_lista)
print(type(otra_lista))

#lista datos compuestos, basicamente otra forma de inicalizar una lista
lista_compuesta = list()
print("esta es una lista compuesta:", lista_compuesta)

lenguaje = ["javascript"]
print ("nuevo valor del arreglo de un elemento:",lenguaje)

# le dimos un valor a estos valores de forma rapida
data_asig = [1,"cristobal", True, 100, "chaos"]
cod, minombre, estado, peso, nombre2 = data_asig


print(list("phyton"))
print(list(range(10)))
print("\n")

#tuplas o tuple
grupo1= ("daniel", "cristian", 10, False, 300)
print(type(grupo1))

print("daniel se repite", grupo1.count("daniel"), "veces")
print("daniel esta en la posicion", grupo1.index("daniel"))

#obteniendo trozo de la tuple
print(grupo1)

#¿como modifico una tuple entonces?
list(grupo1)
print(type(grupo1))

#sets, formas de inicializar

ConjuntoVacio = set()
ConjuntoVacio = {}
print(type(ConjuntoVacio))
conjunto_colores = set({"azul", "rojo", "verde"})
conjunto_animales = {"gato", "perro","loro" }
print(type(conjunto_animales))
print("el segundo set contiene los siguientes animales", conjunto_animales)
