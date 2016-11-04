from funcionVM import funcionVM
from Cuadruplo import Cuadruplo
options = {
	1 : suma,
	2 : resta, 
	3 : multiplicacion,
	4 : division,
	5 : asignacion, 
	6 : comparacionMenor
	7 : comparacionMayor
	8 : comparacionMenorIgual
	9 : comparacionMayorIgual
	10 : comparacionIgual
	11 : comparacionDiferente
	12 : comparacionOR
	13 : comparacionAND
	16 : gotoFalso
	17 : goto 
	18 : leer
	19 : dibujar
	24 : mover
	25 : izquierda
	26 : derecha
	27 : arriba
	28 : abajo
	29 : retorno
	30 : generarERA
	31 : generaParam
	32 : generaGOSUB
}
archivo = open("maquiVirtual.txt")
listaFunc = []
listaCuadruplos = []
diccionarioConstantes = {}
linea = archivo.readline()

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
	elemento[0]	
print len(listaCuadruplos)