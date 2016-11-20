#Clase que maneja las funciones necesarias para crear la maquina virtual.
from funcionVM import funcionVM
from Cuadruplo import Cuadruplo
from Memoria import Memoria
from turtle import *
import sys
import turtle 
listaFunc = []
listaCuadruplos = []
tipoActual = 0 
diccionarioConstantes = {}
diccionarioGlobal = {}
listaMemoria = []
contCuadruplos = 0
size = 100
#Funcion que recibe la direccion de memoria de un entero y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varEntero(variable):
	global tipoActual
	tipoActual = 0
	return int(variable) - 8001
#Funcion que recibe la direccion de memoria de un cuadrado y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varCuadrado(variable):
	global tipoActual
	tipoActual = 1
	return int(variable) - 9001
#Funcion que recibe la direccion de memoria de un rectangulo y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varRectangulo(variable):
	global tipoActual
	tipoActual = 2
	return int(variable) - 10001
#Funcion que recibe la direccion de memoria de un circulo y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varCirculo(variable):
	global tipoActual
	tipoActual = 3
	return int(variable) - 11001
#Funcion que recibe la direccion de memoria de un linea y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varLinea(variable):
	global tipoActual
	tipoActual = 4
	return int(variable) - 12001
#Funcion que recibe la direccion de memoria de un estrella y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varEstrella(variable):
	global tipoActual
	tipoActual = 5
	return int(variable) - 13001
#Funcion que recibe la direccion de memoria de un decimal y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varDecimal(variable):
	global tipoActual
	tipoActual = 6
	return int(variable) - 14001
#Funcion que recibe la direccion de memoria de un bool y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varBool(variable):
	global tipoActual
	tipoActual = 7
	return int(variable) - 15001
#Funcion que recibe la direccion de memoria de un entero temporal y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varEntTemp(variable):
	global tipoActual
	tipoActual = 8
	return int(variable) - 16001
#Funcion que recibe la direccion de memoria de un cuadrado temporal y regresa su offset, asi como 
#guarda el tipo actual para poder accesar de forma rapida a el en memoria.
def varCuadTemp(variable):
	global tipoActual
	tipoActual = 9
	return variable - 17001
#Funcion que recibe la direccion de memoria de un rectangulo temporal y regresa su offset, asi como 
#guarda el tipo actual para poder accesar de forma rapida a el en memoria.
def varRectTemp(variable):
	global tipoActual
	tipoActual = 10
	return int(variable) - 18001
#Funcion que recibe la direccion de memoria de un circulo temporal y regresa su offset, asi como 
#guarda el tipo actual para poder accesar de forma rapida a el en memoria.
def varCircTemp(variable):
	global tipoActual
	tipoActual = 11
	return variable - 19001
#Funcion que recibe la direccion de memoria de una linea temporal y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varLineaTemp(variable):
	global tipoActual
	tipoActual = 12
	return int(variable) - 20001
#Funcion que recibe la direccion de memoria de una estrella temporal y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varEstrTemp(variable):
	global tipoActual
	tipoActual = 13
	return int(variable) - 21001
#Funcion que recibe la direccion de memoria de un decimal temporal y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varDecTemp(variable):
	global tipoActual
	tipoActual = 14
	return int(variable) - 22001
#Funcion que recibe la direccion de memoria de un bool temporal y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
def varBoolTemp(variable):
	global tipoActual
	tipoActual = 15
	return int(variable) - 23001
#Funcion que recibe la direccion de memoria de un apuntador temporal y regresa su offset, asi como guarda
#el tipo actual para poder accesar de forma rapida a el en memoria.
#Estos apuntadores son usados para accesar a la memoria que se indica.
def varApuntTemp(variable):
	global tipoActual
	tipoActual = 16
	return int(variable) - 24001

#Estructura de diccionario que funciona como un switch donde su valor es la llamada de funcion de cada
#uno de sus tipo de datos que regresan su offset correspondiente.
tipodato = {
	8 : varEntero,
	9 : varCuadrado,
	10 : varRectangulo,
	11 : varCirculo,
	12 : varLinea,
	13 : varEstrella,
	14 : varDecimal,
	15 : varBool,
	16 : varEntTemp,
	17 : varCuadTemp,
	18 : varRectTemp,
	19 : varCircTemp,
	20 : varLineaTemp,
	21 : varEstrTemp,
	22 : varDecTemp,
	23 : varBoolTemp,
	24 : varApuntTemp,
}
#Funcion que recibe las direcciones de los operandos y resultado. Genera la suma correspondiente a sus
#tipos de datos.
def suma(operando1, operando2, resultado):
	global pilaMemoria
	global diccionarioConstantes
	print "entra suma", operando1, operando2, resultado
	global contCuadruplos
	global tipoActual
	global listaMemoria
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	auxMem = listaMemoria.pop()
	#Accede a la memoria que se ocupa de acuerdo a su operacion actual y anterior. Si es un parametro,
	#Accede a la memoria de donde se esta llamando y no de la que acaba de generar.
	if listaCuadruplos[contCuadruplos - 2].operador == '30':
		memoria = listaMemoria.pop()
	elif listaCuadruplos[contCuadruplos].operador == '31':
		print len(memoria.listaMem)
		print  len(auxMem.listaMem)
	else:
		memoria = auxMem
	



	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
	auxResultado = tipodato[int(resultado)/1000](resultado)	
	print auxResultado, resultado	
	#En caso de que se tenga que guardar el resultado en un apuntador temporal se suma el valor1 mas 
	#la direccion del operando 2.
	if tipoActual == 16:
		memoria.listaMem[tipoActual][auxResultado] = int(valor1) + int(operando2)
	else:
		if diccionarioConstantes.has_key(operando2):
			valor2 = diccionarioConstantes[operando2]
		else:
			aux2 = tipodato[int(operando2)/1000](operando2)
			if tipoActual == 16:
				valor2 = memoria.listaMem[tipoActual][aux2]
				operando2 = valor2
				aux2 = tipodato[int(operando2)/1000](operando2)
				valor2  = memoria.listaMem[tipoActual][aux2]
			else:
				valor2  = memoria.listaMem[tipoActual][aux2] 
	 	auxResultado = tipodato[int(resultado)/1000](resultado)

	 	#genera la operacion de suma con los valores que se optuvieron.
	 	if '.' in str(valor1) or '.' in str(valor2):
	 		memoria.listaMem[tipoActual][auxResultado] = float(valor1) + float(valor2)
	 	else:
			memoria.listaMem[tipoActual][auxResultado] = int(valor1) + int(valor2)
	listaMemoria.append(memoria)
	print "la suma es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe las direcciones de los operandos y resultado. Genera la resta correspondiente a sus
#tipos de datos.
def resta(operando1, operando2, resultado):
	global pilaMemoria
	global diccionarioConstantes
	print "entra resta", operando1, " ", operando2
	global contCuadruplos
	global tipoActual
	global listaMemoria
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	auxMem = listaMemoria.pop()
	#Accede a la memoria que se ocupa de acuerdo a su operacion actual y anterior. Si es un parametro,
	#Accede a la memoria de donde se esta llamando y no de la que acaba de generar.
	if listaCuadruplos[contCuadruplos - 2].operador == '30':
		print "entraaa"
		memoria = listaMemoria.pop()
	elif listaCuadruplos[contCuadruplos].operador == '31':
		print len(memoria.listaMem)
		print len(auxMem.listaMem)
	else:
		memoria = auxMem

	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2] 
	auxResultado = tipodato[int(resultado)/1000](resultado)
	#genera el resultado de la resta de los dos operandos.
	print "valor1: ", valor1, "valor2: ",valor2
	if '.' in str(valor1) or '.' in str(valor2):
		memoria.listaMem[tipoActual][auxResultado] = float(valor1) - float(valor2)
	else:
		memoria.listaMem[tipoActual][auxResultado] = int(valor1) - int(valor2)
	if listaCuadruplos[contCuadruplos].operador == '31':
		listaMemoria.append(memoria)
		listaMemoria.append(auxMem)
	else:
		listaMemoria.append(memoria)	
	print "la resta es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe las direcciones de los operandos y resultado. Genera la multiplicacion correspondiente a sus
#tipos de datos.
def multiplicacion(operando1, operando2, resultado):
	global pilaMemoria
	global diccionarioConstantes
	print "entra multiplicacion", operando1, " ", operando2
	global contCuadruplos
	global tipoActual
	global listaMemoria
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	auxMem = listaMemoria.pop()
	#Accede a la memoria que se ocupa de acuerdo a su operacion actual y anterior. Si es un parametro,
	#Accede a la memoria de donde se esta llamando y no de la que acaba de generar.
	if listaCuadruplos[contCuadruplos - 2].operador == '30':
		print "entraaa"
		memoria = listaMemoria.pop()
	elif listaCuadruplos[contCuadruplos].operador == '31':
		print memoria.listaMem
		print auxMem.listaMem
	else:
		memoria = auxMem
	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2] 
	auxResultado = tipodato[int(resultado)/1000](resultado)
	#genera el resultado de la multiplicacion de los valores.
	print "valor1: ", valor1, "valor2: ",valor2
	if '.' in str(valor1) or '.' in str(valor2):
		memoria.listaMem[tipoActual][auxResultado] = float(valor1) * float(valor2)
	else:
		memoria.listaMem[tipoActual][auxResultado] = int(valor1) * int(valor2)
	if listaCuadruplos[contCuadruplos].operador == '31':
		listaMemoria.append(memoria)
		listaMemoria.append(auxMem)
	else:
		listaMemoria.append(memoria)
	print "la multiplicacion es", memoria.listaMem[tipoActual][auxResultado]
	
#Funcion que recibe las direcciones de los operandos y resultado. Genera la division correspondiente a sus
#tipos de datos.
def division(operando1, operando2, resultado):
	global pilaMemoria
	global diccionarioConstantes
	print "entra division", operando1, " ", operando2
	global contCuadruplos
	global tipoActual
	global listaMemoria
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	auxMem = listaMemoria.pop()
	#Accede a la memoria que se ocupa de acuerdo a su operacion actual y anterior. Si es un parametro,
	#Accede a la memoria de donde se esta llamando y no de la que acaba de generar.
	if listaCuadruplos[contCuadruplos - 2].operador == '30':
		print "entraaa"
		memoria = listaMemoria.pop()
	elif listaCuadruplos[contCuadruplos].operador == '31':
		print memoria.listaMem
		print auxMem.listaMem
	else:
		memoria = auxMem
	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	print "Operando 1 = ", operando1 , " Operando 2 = ", operando2
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2] 
	auxResultado = tipodato[int(resultado)/1000](resultado)
	#genera el resultado de la division de los dos valores 
	print "valor1: ", valor1, "valor2: ",valor2
	if '.' in str(valor1) or '.' in str(valor2):
		memoria.listaMem[tipoActual][auxResultado] = float(valor1) / float(valor2)
	else:
		memoria.listaMem[tipoActual][auxResultado] = int(valor1) / int(valor2)
	if listaCuadruplos[contCuadruplos].operador == '31':
		listaMemoria.append(memoria)
		listaMemoria.append(auxMem)
	else:
		listaMemoria.append(memoria)
	print "la division es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe las direcciones del operanod 1 y resultado. Genera la asignacion del operando uno
#al resultado.
def asignacion(operando1, operando2, resultado):
	print "entra asignacion", operando2, " ", operando1, " ", resultado
	global contCuadruplos
	global pilaMemoria
	global diccionarioConstantes
	global tipoActual
	global listaMemoria
	memoria = listaMemoria.pop()
	valor1 = 0
	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		aux1 = tipodato[int(operando1)/1000](operando1)
		if tipoActual == 16:
			valor1  = memoria.listaMem[tipoActual][aux1] 
			operando1 = str(valor1)
			if diccionarioConstantes.has_key(operando1):
				valor1 = diccionarioConstantes[operando1]
			else:
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1] 
		else:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 

	contCuadruplos = contCuadruplos + 1
	print "CONTADOR CUADRUPLOS  = ", contCuadruplos
	auxp = int(resultado)
	#Optiene la direccion de memoria a donde se le va a guardar el valor, genera la asignacion 
	if diccionarioConstantes.has_key(str(auxp)):
		auxResultado = diccionarioConstantes[str(auxp)]
	else:
		auxResultado = tipodato[int(resultado)/1000](resultado)
		if tipoActual == 16:
			auxR = memoria.listaMem[tipoActual][auxResultado]
			resultado = auxR
			auxResultado = tipodato[int(resultado)/1000](resultado)

	memoria.listaMem[tipoActual][auxResultado] = valor1
	listaMemoria.append(memoria)
	print "asignacion ", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe el operando uno y el resultado el cual indica que cuadruplo se debe de comenzar
#a leer
def goto(operando1, operando2, resultado):
	global contCuadruplos
	global listaCuadruplos
	global size
	size = size + 25
	print "entra goto \n"
	print resultado
	if listaCuadruplos[int(resultado)].operador == 17:
		print "----- entraaaa "
	contCuadruplos =  int(resultado)

#Funcion que recibe los operandos y el resultado donde sera almacenado el resultado de la comparacion
#menor
def comparacionMenor(operando1, operando2, resultado):
	print "entra comparacionMenor"
	global pilaMemoria
	global diccionarioConstantes
	global contCuadruplos
	global tipoActual
	global listaMemoria
	contCuadruplos = contCuadruplos + 1
	print "CONTADOR CUADRUPLOS  = ", contCuadruplos
	valor1 = 0
	valor2 = 0
	memoria = listaMemoria.pop()
	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)

 	if float(valor1) < float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		auxResultado = tipodato[int(resultado)/1000](resultado)
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion menor  es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe los operandos y el resultado donde sera almacenado el resultado de la comparacion
#mayor
def comparacionMayor(operando1, operando2, resultado):
	print "entra comparacionMayor"
	global pilaMemoria
	global diccionarioConstantes
	global contCuadruplos
	global listaMemoria
	global tipoActual
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	memoria = listaMemoria.pop()

	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2]  
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) > float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion mayor  es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe los operandos y el resultado donde sera almacenado el resultado de la comparacion
#menor igual
def comparacionMenorIgual(operando1, operando2, resultado):
	print "entra comparacionMenorIgual"
	global pilaMemoria
	global diccionarioConstantes
	global contCuadruplos
	global listaMemoria
	global tipoActual
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	memoria = listaMemoria.pop()

	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2]
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) <= float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion menor igual  es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe los operandos y el resultado donde sera almacenado el resultado de la comparacion
#mayor igual
def comparacionMayorIgual(operando1, operando2, resultado):
	print "entra comparacionMayorIgual"
	global pilaMemoria
	global diccionarioConstantes
	global listaMemoria
	global contCuadruplos
	global tipoActual
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	memoria = listaMemoria.pop()

	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
			
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2]
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) >= float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion mayor igual  es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe los operandos y el resultado donde sera almacenado el resultado de la comparacion
#igual
def comparacionIgual(operando1, operando2, resultado):
	print "entra comparacionIgual"
	global pilaMemoria
	global diccionarioConstantes
	global listaMemoria
	global contCuadruplos
	global tipoActual
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	memoria = listaMemoria.pop()

	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) == float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion igual igual  es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe los operandos y el resultado donde sera almacenado el resultado de la comparacion
#diferente
def comparacionDiferente(operando1, operando2, resultado):
	print "entra comparacionDiferente"
	global pilaMemoria
	global diccionarioConstantes
	global contCuadruplos
	global listaMemoria
	global tipoActual
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	memoria = listaMemoria.pop()

	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2]

 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) != float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion diferente es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe los operandos y el resultado donde sera almacenado el resultado de la comparacion
#or
def comparacionOR(operando1, operando2, resultado):
	print "entra comparacionOR"
	global pilaMemoria
	global diccionarioConstantes
	global contCuadruplos
	global tipoActual
	global listaMemoria
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	memoria = listaMemoria.pop()

	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2]

 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) or float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion OR es", memoria.listaMem[tipoActual][auxResultado]

#Funcion que recibe los operandos y el resultado donde sera almacenado el resultado de la comparacion
#and
def comparacionAND(operando1, operando2, resultado):
	print "entra comparacionAND"
	global pilaMemoria
	global diccionarioConstantes
	global contCuadruplos
	global tipoActual
	global listaMemoria
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	memoria = listaMemoria.pop()

	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			if tipoActual == 16:
				valor1 = memoria.listaMem[tipoActual][aux1]
				operando1 = valor1
				aux1 = tipodato[int(operando1)/1000](operando1)
				valor1  = memoria.listaMem[tipoActual][aux1]
			else:
				valor1  = memoria.listaMem[tipoActual][aux1]
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux2 = tipodato[int(operando2)/1000](operando2)
		if tipoActual == 16:
			valor2 = memoria.listaMem[tipoActual][aux2]
			operando2 = valor2
			aux2 = tipodato[int(operando2)/1000](operando2)
			valor2  = memoria.listaMem[tipoActual][aux2]
		else:
			valor2  = memoria.listaMem[tipoActual][aux2]

 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) and float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion AND es", memoria.listaMem[tipoActual][auxResultado]

#Funcion la cual recibe el resultado a donde se va a dirigir el nuevo cuadruplo en caso de ser falso
def gotoFalso(operando1, operando2, resultado):
	global contCuadruplos
	global diccionarioConstantes
	global listaMem
	memoria = listaMemoria.pop()
	valor1 = 0

	#Optiene el valor correspondiente a su direccion de memoria.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	if valor1 == 0:
		contCuadruplos = int(resultado)
	else:
		contCuadruplos = contCuadruplos + 1
	listaMemoria.append(memoria)
	print "entra gotoFalsor", resultado," ", operando2

#Funcion que maneja el mostrar de una variable, recibe el operando1 que es el valor a mostrar. Se
#obtiene su valor de la memoria y se muestra en la ventana
def imprimir(operando1, operando2, resultado):
	global contCuadruplos
	global listaMemoria
	valor1 = 0
	memoria = listaMemoria.pop()
	print "Imprimir"
	
	#Optiene el valor correspondiente a su direccion de memoria.
	try:
		aux1 = tipodato[int(operando1)/1000](operando1)
		valor1  = memoria.listaMem[tipoActual][aux1] 
	except KeyError:
		print "Variable no tiene valor asignado"
		sys.exit()
	listaMemoria.append(memoria)
	turtle.write(valor1, align = "center", font =("Herculanum",72,"bold"))
	contCuadruplos = contCuadruplos + 1 

#Funcion que recibe el id del color que se quiere usar y lo asigna a la funcion de turtle.color y
#fillcolor
def defineColor(color):
	if int (color) == 20:
		turtle.fillcolor('#ffd750')
		turtle.color('#ffd750')
	elif int (color) == 21:
		turtle.fillcolor('#07dc47')
		turtle.color('#07dc47')
	elif int (color) == 22:
		turtle.fillcolor('red')
		turtle.color('red')
	elif int (color) == 23:
		turtle.fillcolor("#002e9e")
		turtle.color("#002e9e")
	elif int (color) == 34:
		turtle.fillcolor("#ff5079")
		turtle.color("#ff5079")
	elif int (color) == 35:
		turtle.fillcolor("#7864ed")
		turtle.color("#7864ed")

#Funcion que recibe la posicion en un string de dos valores, separa los valores en X y Y y 
#optiene su valor para establecer la posicion en turtle
def definePosicion(posicion):
	global diccionarioConstantes
	pos1 = 0
	pos2 = 0
	posicion = posicion.strip('(')
	posicion = posicion.strip(')')
	posicion1 = posicion.split(',')
	
	
	if diccionarioConstantes.has_key(posicion1[0]):
		pos1 = diccionarioConstantes[posicion1[0]]

	if diccionarioConstantes.has_key(posicion1[1]):
		pos2 = diccionarioConstantes[posicion1[1]]

	print pos1, pos2
	turtle.penup()
	setpos(int(pos1),int(pos2))
	turtle.pendown()

#Funcion que la posicion y color del cuadrado que se quiere dibujar. Crea el cuadrado con la posicion
#y color dados.
def dibujarCuadrado(pos, color):
	definePosicion(pos)
	defineColor(color)
	begin_fill()
	for i in range(4):
		turtle.fd(size)
		turtle.left(90)
	end_fill()

#Funcion que la posicion y color del rectangulo que se quiere dibujar. Crea el rectangulo con la posicion
#y color dados.
def dibujarRectangulo(pos, color):
	definePosicion(pos)
	defineColor(color)	
	begin_fill()
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size / 2)
	turtle.left(90)
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size / 2)
	turtle.left(90)
	end_fill()

#Funcion que la posicion y color del circulo que se quiere dibujar. Crea el circulo con la posicion
#y color dados.
def dibujarCirculo(pos, color):
	definePosicion(pos)
	defineColor(color)
	turtle.circle(size)

#Funcion que la posicion y color de la linea que se quiere dibujar. Crea la linea con la posicion
#y color dados.
def dibujarLinea(pos, color):
	definePosicion(pos)
	defineColor(color)
	turtle.forward(size)

#Funcion que la posicion y color de la estrella que se quiere dibujar. Crea la estrella con la posicion
#y color dados.
def dibujarEstrella(pos, color):
	global contCuadruplos
	print pos
	definePosicion(pos)
	defineColor(color)
	angulo = 120
	begin_fill()
	for i in range(5):
	    turtle.forward(size / 2)
	    turtle.right(angulo)
	    turtle.forward(size / 2)
	    turtle.right(72 - angulo)
	end_fill()
	pass

#Funcion que recibe la memoria de lo que se quiere dibujar, posicion y el color. Estos se traduce en su
#valor y se llama a las funciones correspondientes para desplegar el dibujo.
def dibujar(operando1, operando2, resultado):
	global contCuadruplos
	global diccionarioConstantes
	global tipoActual
	try:
		aux1 = tipodato[int(operando1)/1000](operando1)
	except KeyError:
		print "Variable no tiene valor asignado"
		sys.exit()

	print tipoActual
	if tipoActual == 1:
		dibujarCuadrado(operando2,resultado)
	elif tipoActual == 2:
		dibujarRectangulo(operando2,resultado)
	elif tipoActual == 3:
		dibujarCirculo(operando2,resultado)
	elif tipoActual  == 4:
		dibujarLinea(operando2,resultado)
	elif tipoActual ==5:
		print "estrella"
		dibujarEstrella(operando2,resultado)
	contCuadruplos = contCuadruplos + 1

#Funcion que maneja las direcciones a donde se quiere mover la tortuja. Recibe la direccion y la 
#cantidad que se movera.
def direccion(dir,cantidad):
	print dir,cantidad
	turtle.color('#0e7582')
	turtle.shape("turtle")
	if dir == 25:
		print "f"
		turtle.left(cantidad)
	elif dir == 26:
		print "f"
		turtle.right(cantidad)
	elif dir == 27:
		print "e"
		turtle.forward(cantidad)
	elif dir == 28:
		print "m"
		turtle.backward(cantidad)

#Funcion que recibe la memoria de la direccion y de la cantidad la cual traduce a valor y se manda a
#llamar a la funcion de direccion que hara las operaciones correspondientes a mover.
def mover(operando1, operando2, resultado):
	print "entra mover"
	global contCuadruplos
	global diccionarioConstantes
	dire = 0
	
	print resultado
	if diccionarioConstantes.has_key(str(int(resultado))):
		dire = diccionarioConstantes[str(int(resultado))]

	direccion(int(operando2), int(dire))
	contCuadruplos = contCuadruplos + 1


#Funcion que recibe la direccion de memoria del valor que va a regresar. Mueve el cuadruplo a
#la posicion que se tiene guardada en el cudrRetorno de la memoria de la funcion actual.
#Destruye la memoria de la funcion
def retorno(operando1, operando2, resultado):
	print "entra retorno", operando1, " ", operando2, " ", resultado
	global contCuadruplos
	global listaMemoria
	global diccionarioConstantes
	print len(listaMemoria)
	funcionMem = listaMemoria.pop()
	funcionMain = listaMemoria.pop()
	valor1 = 0
	if diccionarioConstantes.has_key(operando2):
		valor1 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor1  = funcionMem.listaMem[tipoActual][aux1] 
	diccionarioConstantes[str(int(resultado))] = valor1
	print " regresaa", funcionMem.cuadrRetorno, " ", len(listaCuadruplos)
	print "CONTADOR CUADRUPLOS  = ", contCuadruplos
	contCuadruplos = funcionMem.cuadrRetorno
	listaMemoria.append(funcionMain)

#Funcion que recibe el id de la funcion que necesita la nueva memoria. Se crea la memoria de la nueva 
#funcion y se mete a la lista de memorias.	
def generarERA(operando1, operando2, resultado):
	print "entra generarERA"
	global listaMemoria
	global contCuadruplos
	global diccionarioConstantes
	memoriaMain = Memoria(0,{},{},{},{},{},{},{},{},{},{},{},{},{}, {},{},{},{})
	listaMemoria.append(memoriaMain)
	contCuadruplos = contCuadruplos + 1

#Funcion que almacena los valores que se estan mandando como parametros en la memoria de la funcion
#que se esta mandando a llamar
def generaParam(operando1, operando2, resultado):
	print "entra generaParam"
	global contCuadruplos
	global listaMemoria
	global tipoActual

	funcionMem = listaMemoria.pop()
	funcionMain = listaMemoria.pop()

	valor1 = 0
	if diccionarioConstantes.has_key(operando2):
		valor1 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor1  = funcionMain.listaMem[tipoActual][aux1] 
	contCuadruplos = contCuadruplos + 1
	auxResultado = tipodato[int(resultado)/1000](resultado)
	funcionMem.listaMem[tipoActual][auxResultado] = valor1
	listaMemoria.append(funcionMain)
	listaMemoria.append(funcionMem)

#Funcion que recibe el resultado el cual es el primer cuadruplo de la funcion que se mando a llamar.
def generaGOSUB(operando1, operando2, resultado):
	print "entra generaGOSUB"
	global contCuadruplos
	global listaMemoria
	memoria  = listaMemoria.pop()
	print "CONTADOR CUADRUPLOS  = ", contCuadruplos
	memoria.cuadrRetorno = contCuadruplos + 1
	listaMemoria.append(memoria)
	contCuadruplos = int(resultado)

#Funcion que recibe operando 1 y los valores contra los cuales va verificar que el indice al cual 
#se quiere acceder este dentro del rango de la vairable dimensionada
def generaVER(operando1, operando2, resultado):
	print "entra generaVER"
	print operando1
	print operando2
	print resultado
	global contCuadruplos
	global diccionarioConstantes
	global listaMemoria
	funcionMain = listaMemoria.pop()

	#Optiene el valor correspondiente a su direccion de memoria y en caso de ser una memoria temporal
	#de apuntador saca su valor correspondiente a una direccion y accede al valor de esta direccion.
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
		print "Entre constante1", valor1
	else:
		aux1 = tipodato[int(operando1)/1000](operando1)
		valor1  = funcionMain.listaMem[tipoActual][aux1] 

	if diccionarioConstantes.has_key(str(int(resultado))):
		valor2 = diccionarioConstantes[str(int(resultado))]
		print "Entre constante2",valor2, str(int(resultado))
	else:
		aux1 = tipodato[int(resultado)/1000](resultado)
		valor2  = funcionMain.listaMem[tipoActual][aux1] 

	if float(valor1) < float(valor2) and float(valor1) >= 0.0:
		contCuadruplos = contCuadruplos + 1 
	else:
		print "Error en indice de arreglo"
		sys.exit()
	listaMemoria.append(funcionMain)

#Diccionario que maneja el acceso a las funciones de operaciones de los cuadruplos. Siendo la llave
#el identificador del operador y el valor la llamada a funcion.
options = {
	'1' : suma,
	'2' : resta, 
	'3' : multiplicacion,
	'4' : division,
	'5' : asignacion, 
	'6' : comparacionMayor,
	'7' : comparacionMenor,
	'9': comparacionMenorIgual,
	'8' : comparacionMayorIgual,
	'10' : comparacionIgual,
	'11' : comparacionDiferente,
	'12' : comparacionOR,
	'13' : comparacionAND,
	'16' : gotoFalso,
	'17' : goto,
	'18' : imprimir, 
	'19' : dibujar,
	'24' : mover,
	'29' : retorno,
	'30' : generarERA,
	'31' : generaParam,
	'32' : generaGOSUB,
	'33' : generaVER,	
}
#Se carga el archivo de maquiVirtual.txt el cual es generado por el yacc, que contiene la informacion
#de las funciones declaradas, asi como los valores de las variables constantes y los cuadruplos.
archivo = open("maquiVirtual.txt")
linea = archivo.readline()
#crea la lista de funciones con la informacion que recibe del archivo de texto.
while linea != "$$\n":
	lineaAux = linea.split(' ')
	objeto = funcionVM(lineaAux[0], lineaAux[1], lineaAux[2], lineaAux[3], lineaAux[4], lineaAux[5], lineaAux[6],lineaAux[7],lineaAux[8], lineaAux[9],lineaAux[10], lineaAux[11], lineaAux[12], lineaAux[13],lineaAux[14], lineaAux[15], lineaAux[16], lineaAux[17], lineaAux[18], lineaAux[19])
	listaFunc.append(objeto)
	linea = archivo.readline()
	
linea = archivo.readline()
#crea el diccionario de constantes con la direccion de memoria y el valo correspondiente.
while linea != '$$\n':
	lineaAux = linea.split(' ')
	diccionarioConstantes[lineaAux[0]] = lineaAux[1]
	linea = archivo.readline()

linea = archivo.readline()
#crea la lista de cuadruplos con los cruaduplos encontrados en el archivo de texto.
while linea != '$$\n':
	lineaAux = linea.split(' ')
	if(len(lineaAux)) == 4: 
		cuadr = Cuadruplo(lineaAux[0], lineaAux[1], lineaAux[2],lineaAux[3])
	elif (len(lineaAux)) == 5:
		cuadr = Cuadruplo(lineaAux[0], lineaAux[1], lineaAux[2]+lineaAux[3], lineaAux[4])

	listaCuadruplos.append(cuadr)
	linea = archivo.readline()
archivo.close()

#Crea la memoria del main y la mete a la lista de memorias
memoriaMain = Memoria(0,{},{},{},{},{},{},{},{},{},{},{},{}, {},{},{},{},{})
listaMemoria.append(memoriaMain)

#Comienza a leer los cuadruplos
while contCuadruplos < len(listaCuadruplos):
	options[listaCuadruplos[contCuadruplos].operador](listaCuadruplos[contCuadruplos].operando1, listaCuadruplos[contCuadruplos].operando2, listaCuadruplos[contCuadruplos].temporal)
exitonclick()