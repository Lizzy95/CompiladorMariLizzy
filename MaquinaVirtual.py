from funcionVM import funcionVM
from Cuadruplo import Cuadruplo
from Memoria import Memoria
import sys
listaFunc = []
listaCuadruplos = []
tipoActual = 0 
diccionarioConstantes = {}
diccionarioGlobal = {}
listaMemoria = []
contCuadruplos = 0

def varEntero(variable):
	global tipoActual
	tipoActual = 0
	return int(variable) - 8001
def varCuadrado(variable):
	global tipoActual
	tipoActual = 1
	return int(variable) - 9001
def varRectangulo(variable):
	global tipoActual
	tipoActual = 2
	return int(variable) - 10001
def varCirculo(variable):
	global tipoActual
	tipoActual = 3
	return int(variable) - 11001
def varLinea(variable):
	global tipoActual
	tipoActual = 4
	return int(variable) - 12001
def varEstrella(variable):
	global tipoActual
	tipoActual = 5
	return int(variable) - 13001
def varDecimal(variable):
	global tipoActual
	tipoActual = 6
	return int(variable) - 14001
def varBool(variable):
	global tipoActual
	tipoActual = 7
	return int(variable) - 15001
def varEntTemp(variable):
	global tipoActual
	tipoActual = 8
	return int(variable) - 16001
def varCuadTemp(variable):
	global tipoActual
	tipoActual = 9
	return variable - 17001
def varRectTemp(variable):
	global tipoActual
	tipoActual = 10
	return int(variable) - 18001
def varCircTemp(variable):
	global tipoActual
	tipoActual = 11
	return variable - 19001
def varLineaTemp(variable):
	global tipoActual
	tipoActual = 12
	return int(variable) - 20001
def varEstrTemp(variable):
	global tipoActual
	tipoActual = 13
	return int(variable) - 21001
def varDecTemp(variable):
	global tipoActual
	tipoActual = 14
	return int(variable) - 22001
def varBoolTemp(variable):
	global tipoActual
	tipoActual = 15
	return int(variable) - 23001
def varApuntTemp(variable):
	global tipoActual
	tipoActual = 16
	return int(variable) - 24001

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

	if listaCuadruplos[contCuadruplos - 2].operador == '30':
		memoria = listaMemoria.pop()
	elif listaCuadruplos[contCuadruplos].operador == '31':
		print memoria.listaMem
		print auxMem.listaMem
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
	if tipoActual == 16:
		print "entraaa"
		memoria.listaMem[tipoActual][auxResultado] = int(valor1) + int(operando2)
	else:
		print "entrssss"
		if diccionarioConstantes.has_key(operando2):
			print"entra if"
			valor2 = diccionarioConstantes[operando2]
		else:
			print "enf"
			aux2 = tipodato[int(operando2)/1000](operando2)
			if tipoActual == 16:
				valor2 = memoria.listaMem[tipoActual][aux2]
				operando2 = valor2
				aux2 = tipodato[int(operando2)/1000](operando2)
				valor2  = memoria.listaMem[tipoActual][aux2]
			else:
				valor2  = memoria.listaMem[tipoActual][aux2] 
	 	auxResultado = tipodato[int(resultado)/1000](resultado)
	 	if '.' in str(valor1) or '.' in str(valor2):
	 		memoria.listaMem[tipoActual][auxResultado] = float(valor1) + float(valor2)
	 	else:
			memoria.listaMem[tipoActual][auxResultado] = int(valor1) + int(valor2)
	listaMemoria.append(memoria)
	print "la suma es", memoria.listaMem[tipoActual][auxResultado]

def resta(operando1, operando2, resultado):
	global pilaMemoria
	global diccionarioConstantes
	print "entra resta", operando1, " ", operando2, " ", resultado
	global contCuadruplos
	global tipoActual
	global listaMemoria
	global listaCuadruplos
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	auxMem = listaMemoria.pop()
	if listaCuadruplos[contCuadruplos - 2].operador == '30':
		memoria = listaMemoria.pop()
	elif listaCuadruplos[contCuadruplos].operador == '31':
		print memoria.listaMem
		print auxMem.listaMem
	else:
		memoria = auxMem

	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		aux1 = tipodato[int(operando1)/1000](operando1)
		valor1  = memoria.listaMem[tipoActual][aux1]  
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
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
	print"----------", auxMem.listaMem
	if listaCuadruplos[contCuadruplos - 2].operador == '30':
		print "entraaa"
		memoria = listaMemoria.pop()
	elif listaCuadruplos[contCuadruplos].operador == '31':
		print memoria.listaMem
		print auxMem.listaMem
	else:
		# print "entraaa21"
		# auxier = listaMemoria.pop()
		memoria = auxMem
		# listaMemoria.append(auxier)

	print "Operando 1 = ", operando1 , " Operando 2 = ", operando2
	print diccionarioConstantes
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		aux1 = tipodato[int(operando1)/1000](operando1)
		valor1  = memoria.listaMem[tipoActual][aux1]  
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		print "aux1 = ", aux1
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	print "valor1: ", valor1, "valor2: ",valor2
 	if '.' in str(valor1) or '.' in str(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = float(valor1) * float(valor2)
 	else:
		memoria.listaMem[tipoActual][auxResultado] = int(valor1) * int(valor2)
	listaMemoria.append(memoria)
	print "la multiplicacion es", memoria.listaMem[tipoActual][auxResultado]
	

def division(operando1, operando2, resultado):
	global pilaMemoria
	global diccionarioConstantes
	print "entra division"
	global contCuadruplos
	global tipoActual
	global listaMemoria
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	auxMem = listaMemoria.pop()
	if listaCuadruplos[contCuadruplos - 2].operador == '30':
		memoria = listaMemoria.pop()
	elif listaCuadruplos[contCuadruplos].operador == '31':
		print memoria.listaMem
		print auxMem.listaMem
	else:
		memoria = auxMem
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		aux1 = tipodato[int(operando1)/1000](operando1)
		print "operando1", operando1
		print "operando2", operando2
		print "aux1 = ", aux1
		valor1  = memoria.listaMem[tipoActual][aux1]  
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		print "aux1 = ", aux1
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	print valor1, " ", valor2
 	if '.' in str(valor1) or '.' in str(valor2):
 		try:
 			memoria.listaMem[tipoActual][auxResultado] = float(valor1) / float(valor2)
			print "la division es", memoria.listaMem[tipoActual][auxResultado]
 		except ZeroDivisionError:
 			memoria.listaMem[tipoActual][auxResultado] = 0
 			print "Error en la division"
 			sys.exit()
 	else:
 		try:
			memoria.listaMem[tipoActual][auxResultado] = int(valor1) / int(valor2)
			print "la division es", memoria.listaMem[tipoActual][auxResultado]
		except ZeroDivisionError:
			memoria.listaMem[tipoActual][auxResultado] = 0
 			print "Error en la division"
 			sys.exit()
	listaMemoria.append(memoria)

def asignacion(operando1, operando2, resultado):
	print "entra asignacion", operando2, " ", operando1, " ", resultado
	global contCuadruplos
	global pilaMemoria
	global diccionarioConstantes
	global tipoActual
	global listaMemoria
	memoria = listaMemoria.pop()
	valor1 = 0

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
				print ":",operando1, aux1, tipoActual, memoria.listaMem[tipoActual]
				valor1  = memoria.listaMem[tipoActual][aux1] 
		else:
			aux1 = tipodato[int(operando1)/1000](operando1)
			print operando1, aux1, tipoActual, memoria.listaMem
			valor1  = memoria.listaMem[tipoActual][aux1] 

	contCuadruplos = contCuadruplos + 1
	print "CONTADOR CUADRUPLOS  = ", contCuadruplos
	print int(resultado)
	auxp = int(resultado)

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


def goto(operando1, operando2, resultado):
	global contCuadruplos
	global listaCuadruplos
	print "entra goto \n"
	print resultado
	if listaCuadruplos[int(resultado)].operador == 17:
		print "----- entraaaa "
	contCuadruplos =  int(resultado)
	#listaCuadruplos.pop()
	#else:
		#contCuadruplos = int(resultado)


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

	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	if float(valor1) < float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		auxResultado = tipodato[int(resultado)/1000](resultado)
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion menor  es", memoria.listaMem[tipoActual][auxResultado]

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

	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) > float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion mayor  es", memoria.listaMem[tipoActual][auxResultado]

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

	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	print "valor 1: ",valor1
 	print "valor 2: ",valor2
 	if float(valor1) <= float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion menor igual  es", memoria.listaMem[tipoActual][auxResultado]

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

	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) >= float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion mayor igual  es", memoria.listaMem[tipoActual][auxResultado]
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

	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) == float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion igual igual  es", memoria.listaMem[tipoActual][auxResultado]

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

	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) != float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion diferente es", memoria.listaMem[tipoActual][auxResultado]
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
	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) or float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion OR es", memoria.listaMem[tipoActual][auxResultado]
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

	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()
	if diccionarioConstantes.has_key(operando2):
		valor2 = diccionarioConstantes[operando2]
	else:
		aux1 = tipodato[int(operando2)/1000](operando2)
		valor2 = memoria.listaMem[tipoActual][aux1] 
 	auxResultado = tipodato[int(resultado)/1000](resultado)
 	
 	if float(valor1) and float(valor2):
 		memoria.listaMem[tipoActual][auxResultado] = 1
 	else:
 		memoria.listaMem[tipoActual][auxResultado] = 0

	listaMemoria.append(memoria)
	print "la comparacion AND es", memoria.listaMem[tipoActual][auxResultado]
def gotoFalso(operando1, operando2, resultado):
	global contCuadruplos
	global diccionarioConstantes
	global listaMem
	memoria = listaMemoria.pop()
	valor1 = 0


	if diccionarioConstantes.has_key(operando1):
		valor1 = diccionarioConstantes[operando1]
	else:
		try:
			aux1 = tipodato[int(operando1)/1000](operando1)
			valor1  = memoria.listaMem[tipoActual][aux1] 
		except KeyError:
			print "Variable no tiene valor asignado"
			sys.exit()

	print "Valor 1 = ", valor1
	if valor1 == 0:
		contCuadruplos = int(resultado)
	else:
		contCuadruplos = contCuadruplos + 1
	listaMemoria.append(memoria)
	print "entra gotoFalsor", resultado," ", operando2
def leer(operando1, operando2, resultado):
	print "entra leer"
def dibujar(operando1, operando2, resultado):
	print "entra dibujar"
def mover(operando1, operando2, resultado):
	print "entra mover"
def izquierda(operando1, operando2, resultado):
	print "entra izquierda"
def derecha(operando1, operando2, resultado):
	print "entra derecha"
def arriba(operando1, operando2, resultado):
	print "entra arriba"
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

def abajo(operando1, operando2, resultado):
	print "entra abajo"
	
def generarERA(operando1, operando2, resultado):
	print "entra generarERA"
	global listaMemoria
	global contCuadruplos
	global diccionarioConstantes
	print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", contCuadruplos	
	memoriaMain = Memoria(0,{},{},{},{},{},{},{},{},{},{},{},{}, {},{},{},{})
	#diccionarioConstantes[str(int(resultado))] = 1
	listaMemoria.append(memoriaMain)
	contCuadruplos = contCuadruplos + 1


def generaParam(operando1, operando2, resultado):
	print "entra generaParam"
	global contCuadruplos
	global listaMemoria
	global tipoActual

	funcionMem = listaMemoria.pop()
	funcionMain = listaMemoria.pop()

	# print "Operando 1  = ", operando1
	# print "Operando2 = ", operando2
	# print "Resultado = ",resultado
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

def generaGOSUB(operando1, operando2, resultado):
	print "entra generaGOSUB"
	global contCuadruplos
	global listaMemoria
	memoria  = listaMemoria.pop()
	print "CONTADOR CUADRUPLOS  = ", contCuadruplos
	memoria.cuadrRetorno = contCuadruplos + 1
	listaMemoria.append(memoria)
	contCuadruplos = int(resultado)

def generaVER(operando1, operando2, resultado):
	print "entra generaVER"
	print operando1
	print operando2
	print resultado
	global contCuadruplos
	global diccionarioConstantes
	global listaMemoria
	funcionMain = listaMemoria.pop()
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
	'18' : leer,
	'19' : dibujar,
	'24' : mover,
	'25' : izquierda,
	'26' : derecha,
	'27' : arriba,
	'28' : abajo,
	'29' : retorno,
	'30' : generarERA,
	'31' : generaParam,
	'32' : generaGOSUB,
	'33' : generaVER,
	
}
archivo = open("maquiVirtual.txt")
linea = archivo.readline()
while linea != "$$\n":
	lineaAux = linea.split(' ')
	objeto = funcionVM(lineaAux[0], lineaAux[1], lineaAux[2], lineaAux[3], lineaAux[4], lineaAux[5], lineaAux[6],lineaAux[7],lineaAux[8], lineaAux[9],lineaAux[10], lineaAux[11], lineaAux[12], lineaAux[13],lineaAux[14], lineaAux[15], lineaAux[16], lineaAux[17], lineaAux[18], lineaAux[19])
	listaFunc.append(objeto)
	linea = archivo.readline()
	
linea = archivo.readline()

while linea != '$$\n':
	lineaAux = linea.split(' ')
	diccionarioConstantes[lineaAux[0]] = lineaAux[1]
	linea = archivo.readline()

linea = archivo.readline()

while linea != '$$\n':
	lineaAux = linea.split(' ')
	cuadr = Cuadruplo(lineaAux[0], lineaAux[1], lineaAux[2],lineaAux[3])
	listaCuadruplos.append(cuadr)
	linea = archivo.readline()
archivo.close()

memoriaMain = Memoria(0,{},{},{},{},{},{},{},{},{},{},{},{}, {},{},{},{},{})
listaMemoria.append(memoriaMain)

while contCuadruplos < len(listaCuadruplos):
	options[listaCuadruplos[contCuadruplos].operador](listaCuadruplos[contCuadruplos].operando1, listaCuadruplos[contCuadruplos].operando2, listaCuadruplos[contCuadruplos].temporal)
