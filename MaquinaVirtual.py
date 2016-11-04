from funcionVM import funcionVM
from Cuadruplo import Cuadruplo
from Memoria import Memoria
listaFunc = []
listaCuadruplos = []
tipoActual = "" 
diccionarioConstantes = {}
listaMemoria = []
contCuadruplos = 0

def varEntero(variable):
	global tipoActual
	tipoActual = "arrEntero"
	return variable - 8001
def varCuadrado(variable):
	global tipoActual
	tipoActual = "arrCuadrado"
	return variable - 9001
def varRectangulo(variable):
	global tipoActual
	tipoActual = "arrRectangulo"
	return variable - 10001
def varCirculo(variable):
	global tipoActual
	tipoActual = "arrCirculo"
	return variable - 11001
def varLinea(variable):
	global tipoActual
	tipoActual = "arrLinea"
	return variable - 12001
def varEstrella(variable):
	global tipoActual
	tipoActual = "arrEstrella"
	return variable - 13001
def varDecimal(variable):
	global tipoActual
	tipoActual = "arrDecimal"
	return variable - 13001
def varBool(variable):
	global tipoActual
	tipoActual = "arrBool"
	return variable - 14001
def varEntTemp(variable):
	global tipoActual
	tipoActual = "arrEnteroTemp"
	return variable - 15001
def varCuadTemp(variable):
	global tipoActual
	tipoActual = "arrCuadradoTemp"
	return variable - 16001
def varRectTemp(variable):
	global tipoActual
	tipoActual = "arrRectanguloTemp"
	return variable - 17001
def varCircTemp(variable):
	global tipoActual
	tipoActual = "arrCirculoTemp"
	return variable - 18001
def varLineaTemp(variable):
	global tipoActual
	tipoActual = "arrLineaTemp"
	return variable - 19001
def varEstrTemp(variable):
	global tipoActual
	tipoActual = "arrEstrellaTemp"
	return variable - 20001
def varDecTemp(variable):
	global tipoActual
	tipoActual = "arrDecimalemp"
	return variable - 21001
def varBoolTemp(variable):
	global tipoActual
	tipoActual = "arrBoolTemp"
	return variable - 22001

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
}
def suma(operando1, operando2, resultado):
	global pilaMemoria
	global diccionarioConstantes
	print "entra suma"
	global contCuadruplos
	global tipoActual
	contCuadruplos = contCuadruplos + 1
	valor1 = 0
	valor2 = 0
	memoria = listaMemoria.pop()
	print operando1
	if diccionarioConstantes.has_key(operando1):
		print "entra if 1"
		valor1 = diccionarioConstantes[operando1]
	else:
		print "entra else 1"
		aux1 = tipodato[int(operando1)/1000]
		valor1  = memoria.tipoActual[aux1] 
	print operando2
	if diccionarioConstantes.has_key(operando2):
		print "entra if 2"
		valor2 = diccionarioConstantes[operando2]
	else:
		print "entra else 2"
		aux1 = tipodato[int(operando2)/1000]
		valor2 = memoria.tipoActual[aux1] 

 	auxResultado = tipodato[int(resultado)/1000]
 	print "enta adu", tipoActual
	memoria.tipoActual[aux1] = valor1 + valor2
	listaMemoria.append(memoria)
	print memoria.tipoActual[aux1] 





def resta(operando1, operando2, resultado):
	print "entra resta"

def multiplicacion(operando1, operando2, resultado):
	print "entra multiplicacion"

def division(operando1, operando2, resultado):
	print "entra division"

def asignacion(operando1, operando2, resultado):
	print "entra asignacion"

def goto(operando1, operando2, resultado):
	print "entra goto"

def comparacionMenor(operando1, operando2, resultado):
	print "entra comparacionMenor"
def comparacionMayor(operando1, operando2, resultado):
	print "entra comparacionMayor"
def comparacionMenorIgual(operando1, operando2, resultado):
	print "entra comparacionMenorIgual"
def comparacionMayorIgual(operando1, operando2, resultado):
	print "entra comparacionMayorIgual"
def comparacionIgual(operando1, operando2, resultado):
	print "entra comparacionIgual"
def comparacionDiferente(operando1, operando2, resultado):
	print "entra comparacionDiferente"
def comparacionOR(operando1, operando2, resultado):
	print "entra comparacionOR"
def comparacionAND(operando1, operando2, resultado):
	print "entra comparacionAND"
def gotoFalso(operando1, operando2, resultado):
	global contCuadruplos
	contCuadruplos = contCuadruplos + 1
	print "entra gotoFalsor"
def goto(operando1, operando2, resultado):
	global contCuadruplos
	contCuadruplos = contCuadruplos + 1
	print "entra goto"
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
	print "entra retorno"
def abajo(operando1, operando2, resultado):
	print "entra abajo"
def generarERA(operando1, operando2, resultado):
	print "entra generarERA"
def generaParam(operando1, operando2, resultado):
	print "entra generaParam"

def generaGOSUB(operando1, operando2, resultado):
	print "entra generaGOSUB"




options = {
	'1' : suma,
	'2' : resta, 
	'3' : multiplicacion,
	'4' : division,
	'5' : asignacion, 
	'6' : comparacionMenor,
	'7' : comparacionMayor,
	'8': comparacionMenorIgual,
	'9' : comparacionMayorIgual,
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

memoriaMain = Memoria({},{},{},{},{},{},{},{},{},{},{},{},{}, {},{},{}	,0)
listaMemoria.append(memoriaMain)

while contCuadruplos <= len(listaCuadruplos):
	options[listaCuadruplos[contCuadruplos].operador](listaCuadruplos[contCuadruplos].operando1, listaCuadruplos[contCuadruplos].operando2, listaCuadruplos[contCuadruplos].temporal)



