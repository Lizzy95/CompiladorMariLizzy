from funcionVM import funcionVM
from Cuadruplo import Cuadruplo

listaFunc = []
listaCuadruplos = []
diccionarioConstantes = {}
linea = archivo.readline()

tipodato = {
	0 : varEntero,
	1 : varCuadrado,
	2 : varRectangulo,
	3 : varCirculo,
	4 : varLinea,
	5 : varEstrella,
	6 : varDecimal,
	7 : varBool,
	8 : varEntTemp,
	9 : varCuadTemp,
	10 : varRectTemp,
	11 : varCircTemp,
	12 : varLineaTemp,
	13 : varEstrTemp,
	14 : varDecTemp,
	15 : varBoolTemp,
}

def suma(operando1, operando2, resultado):
	print "entra suma"

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
def gotoFalso(operando1, operando2, resultado):
	print "entra gotoFalsor"
def goto(operando1, operando2, resultado):
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
def generarERA(operando1, operando2, resultado):
	print "entra generarERA"
def generarParam(operando1, operando2, resultado):
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

while linea != "$$\n":
	lineaAux = linea.split(' ')
	objeto = funcionVM(lineaAux[0], lineaAux[1], lineaAux[2], lineaAux[3], lineaAux[4], lineaAux[5], lineaAux[6],lineaAux[7],lineaAux[8], lineaAux[9],lineaAux[10], lineaAux[11], lineaAux[12], lineaAux[13])
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

for elemento in listaCuadruplos:
	print elemento.operador
	options[elemento.operador](elemento.operando1, elemento.operando2, elemento.temporal)




