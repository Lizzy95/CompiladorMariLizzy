import ply.yacc as yacc
from TFunc import TFunc
from TVar import TVar
from CuboSemantico import cuboSemantico
from diccionarioMemoria import diccionarioMemoria
from Cuadruplo import Cuadruplo
# Get the token map from the lexer.  This is required.
from lex import tokens

listaFunciones = []
listaCuadruplos = []
funcionActual = ""
tipoActual = 0
operando1 = ""
operando2 = ""
tipofuncMem = '1'
pilaOperadores = []
pilaOperandos = []
diccConstantes = {}
diccionarioVarGlobal = {}
pilaOperandosDirMem = []
pilaSaltos = []
pilaSaltosFunc = []
operadorActual = 0
contParam = 0
llamada = ""
resultado = -1
DEBUG = True
cuadr = Cuadruplo(17, -1, -1, -1)
listaCuadruplos.append(cuadr)
# BNF
def p_programa(p):
	'''programa : vars funcion INICIO funcAgregarInicio bloque  FIN liberarVar
	  			| vars funcion INICIO FIN '''	
	global pilaOperandos
	global pilaOperadores
	global pilaOperandosDirMem
	global pilaSaltosFunc
	global listaCuadruplos
	print("SE TERMINO EL PROGRAMA PATIO CON EXITO!")
	escribeArchivo()
	#print(pilaOperandos, "la ", pilaOperandosDirMem, "de ", pilaOperadores)
	pass


def p_funcAgregarInicio(p):
	'''funcAgregarInicio : '''
	global funcionActual
	global listaFunciones
	global tipofuncMem
	tipofuncMem = '2'
	funcionActual = p[-1]
	objetoFuncion = TFunc(funcionActual, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {}, {})
	listaFunciones.append(objetoFuncion) 
	print("Se agrego la funcion a la tabla")

def p_bloque(p):
	'''bloque : "{" vars guardarCuadruplo estatuto "}"
			  | "{" vars guardarCuadruplo "}"
			  | "{" "}"'''
	print("BLOQUE")
	pass

def p_vars(p):
	'''vars : tipo ID guardarIDs ";" masTipos
		| tipo ID guardarIDs arreglo  ";" masTipos
		| tipo listaIDS ";" masTipos
		| empty'''
	print("VARS: Estructura basica")
	pass

def p_masTipos(p):
	'''masTipos : vars 
				| empty '''
	pass

def p_listaIDS(p):
	''' listaIDS : ID guardarIDs masIDS '''
	pass

def p_masIDS(p):
	'''masIDS : "," ID guardarIDs
			   | empty '''
	pass

def p_arreglo(p):
	''' arreglo : "[" CTI "]" matriz '''
	pass

def p_matriz(p):
	''' matriz : "[" CTI "]" 
			   | empty '''
	pass

def p_funcion(p): 
	''' funcion : FUNC tipo ID  funcAgregar restoFuncion  funcion2
				| empty '''
	print "Entre a funcion"
	pass

def p_funcion2(p): 
	''' funcion2 : funcion
				| empty '''
	print "Entre a funcion2"
	pass

def p_restoFuncion(p):
	''' restoFuncion : "(" param ")" bloquefunc'''
	pass

def p_funcAgregar(p):
	'''funcAgregar :  '''
	print "Entre a funcAgregar"
	global funcionActual
	global listaFunciones
	global tipoActual
	global tipofuncMem
	tipofuncMem = '2'
	funcionActual = p[-1]
	objetoFuncion = TFunc(p[-1], tipoActual, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {}, {})
	#checar si ya existe una funcion
	posicion = busquedaLista()
	if posicion != -1:
		print "FUNCION PREVIAMENTE DECLARADA"
	else:
		print "Entre al else FuncAgregar"
		listaFunciones.append(objetoFuncion)

def p_param(p):
	''' param : tipo  ID guardarIDParam maspaID 
		 		| empty'''
	pass
	
def p_guardarIDParam(p):
	''' guardarIDParam : '''
	global funcionActual
	global listaFunciones
	global tipoActual
	global diccionarioMemoria
	#checar si ya existe una variable
	if (busquedaVar(p[-1]) != -1 ):
		print "SE DECLARO UNA VARIABLE PREVIAMENTE DECLARADA"
	else:
		posicion = busquedaLista()
		var = diccionarioMemoria[tipofuncMem]
		valormem = var[str(tipoActual)]
		agregarVar = TVar(p[-1], tipoActual, valormem)
		diccionarioMemoria[tipofuncMem][str(tipoActual)] = valormem + 1
		listaFunciones[posicion].arrParam.append(agregarVar)
		print "Se guardo el parametro en la tabla de parametros ", tipoActual

def busquedaLista():
	cont = 0
	global listaFunciones
	global funcionActual
	for elemento in listaFunciones:
		if elemento.nombre == funcionActual : 
			return cont
		cont += 1
	return -1

def busquedaFunc(funcionLlamar):
	cont = 0
	global listaFunciones
	for elemento in listaFunciones:
		if elemento.nombre == funcionLlamar : 
			return cont
		cont += 1
	return -1

def busquedaVar(varActual):
	global listaFunciones
	global funcionActual
	#imprimirLista()
	cont = 0
	for elemento in listaFunciones:
		if funcionActual == elemento.nombre:
			for elemento2 in elemento.arrVar:
				if(varActual == elemento2.nombre):
					return cont
				else:
					cont += 1


	return -1

def busquedaVarGlobal(var):
	global diccionarioVarGlobal
	if diccionarioVarGlobal.has_key(var):
		return -1

#def imprimirLista():
#	print"imprime elementos"
#	for elemento in listaFunciones:
#		print elemento.nombre

def p_guardarIDs(p):
	''' guardarIDs : '''
	global funcionActual
	global listaFunciones
	global tipoActual
	global tipofuncMem
	global diccionarioMemoria
	if(tipofuncMem == '1'):
		if busquedaVarGlobal(p[-1]) == -1:
			"SE DECLARO UNA VARIABLE PREVIAMENTE DECLARADA"
		else:
			var = diccionarioMemoria[tipofuncMem]
			valormem = var[str(tipoActual)]
			diccionarioMemoria[tipofuncMem][str(tipoActual)] = valormem + 1
			diccionarioVarGlobal[valormem] = p[-1]
			print "Se guardo la variable global en el diccionario ", tipoActual
	#checar si ya existe una variable
	else:
		if (busquedaVar(p[-1]) != -1 ):
			print "SE DECLARO UNA VARIABLE PREVIAMENTE DECLARADA"
		else:
			posicion = busquedaLista()
			var = diccionarioMemoria[tipofuncMem]
			valormem = var[str(tipoActual)]
			agregarVar = TVar(p[-1], tipoActual, valormem)
			diccionarioMemoria[tipofuncMem][str(tipoActual)] = valormem + 1 
			listaFunciones[posicion].arrVar.append(agregarVar)
			print "Se guardo la variable en la tabla ", tipoActual

def p_maspaID(p):
	''' maspaID : "," param
				| empty '''
	pass

def p_bloquefunc(p): 
	''' bloquefunc : "{" vars guardarCuadruplo estatuto regresa "}" liberarVar 
				   | "{" vars guardarCuadruplo regresa "}" liberarVar
				   | "{" guardarCuadruplo escritura regresa "}" liberarVar
				   | "{" "}" '''
	pass

def p_liberarVar(p):
	''' liberarVar : '''
	global diccionarioMemoria
	global listaFunciones
	global listaCuadruplos
	
	posicion = busquedaLista()

	cuadr = Cuadruplo(29, -1, -1, -1)
	listaCuadruplos.append(cuadr)


	loc = diccionarioMemoria['2']
	auxLoc = loc['1'] - 8001
	auxCua = loc['2'] - 9001
	auxRect = loc['3'] - 10001
	auxCir = loc['4'] - 11001
	auxLin = loc['5'] - 12001
	auxEstr = loc['6'] - 13001
	auxDec = loc['7'] - 14001
	auxBool = loc['8'] - 15001

	listaFunciones[posicion].varEnt = auxLoc
	listaFunciones[posicion].varDec = auxDec
	listaFunciones[posicion].varCuadrado = auxCua
	listaFunciones[posicion].varRect = auxRect
	listaFunciones[posicion].varCirc = auxCir
	listaFunciones[posicion].varLin = auxLin
	listaFunciones[posicion].varEstr = auxEstr
	listaFunciones[posicion].varBool = auxBool

	loc['1'] = 8001
	loc['2'] = 9001
	loc['3'] = 10001
	loc['4'] = 11001
	loc['5'] =  12001
	loc['6'] =  13001
	loc['7'] =  14001
	loc['8'] =  15001

	temp = diccionarioMemoria['3'] 
	auxLoc = temp['1'] - 16001
	auxCua = temp['2'] - 17001
	auxRect = temp['3'] - 18001
	auxCir = temp['4'] - 19001
	auxLin = temp['5'] - 20001
	auxEstr = temp['6'] - 21001
	auxDec = temp['7'] - 22001
	auxBool = temp['8'] - 23001

	listaFunciones[posicion].varEntTemp = auxLoc
	listaFunciones[posicion].varDecTemp = auxDec
	listaFunciones[posicion].varCuadradoTemp = auxCua
	listaFunciones[posicion].varRectTemp = auxRect
	listaFunciones[posicion].varCircTemp = auxCir
	listaFunciones[posicion].varLinTemp = auxLin
	listaFunciones[posicion].varEstrTemp = auxEstr
	listaFunciones[posicion].varBoolTemp = auxBool

	temp['1'] =  16001
	temp['2'] = 17001
	temp['3'] = 18001
	temp['4'] = 19001
	temp['5'] =  20001
	temp['6'] =  21001
	temp['7'] =  22001
	temp['8'] =  23001

	cte = diccionarioMemoria['4'] 
	cte['1'] =  24001
	cte['2'] = 25001
	cte['3'] = 26001
	cte['4'] = 27001
	cte['5'] =  28001
	cte['6'] =  29001
	cte['7'] =  30001
	cte['8'] =  31001
	
	pass

def p_guardarCuadruplo(p): 
	'''guardarCuadruplo :  '''
	global listaFunciones
	global listaCuadruplos
	global funcionActual
	act = len(listaCuadruplos)
	if funcionActual == 'inicio':
		listaCuadruplos[0].temporal = act
	posicion = busquedaLista()
	listaFunciones[posicion].cuadruploInicial = act
	pass

def p_regresa(p):
	''' regresa : RETURN ID '''
	pass

def p_estatuto(p):
	'''estatuto : asignacion estatutoAux
				| escritura estatutoAux
				| condicion estatutoAux
				| lectura estatutoAux
				| whiles estatutoAux
				| funcs estatutoAux '''
	pass

def p_estatutoAux(p):
	''' estatutoAux : estatuto
					| empty'''
	pass

def p_checaNumParam(p):
	''' checaNumParam : ")"'''
	global contParam
	global listaFunciones
	pos = busquedaFunc(llamada)
	numParam  = len(listaFunciones[pos].arrParam)
	if contParam + 1 != numParam:	
		print "El numero de parametros es incorrecto"
	pass

def p_generaGOSUB(p):
	'''generaGOSUB : '''
	global listaCuadruplos
	global llamada
	cuadr = Cuadruplo(32,-1,-1,llamada)
	listaCuadruplos.append(cuadr)
	print "Se guardo GOSUB", llamada
	pass

def p_funcs(p):
	''' funcs : ID verProc generarERA auxExp  checaNumParam generaGOSUB
			  | ID '''
	pass

def p_verProc(p):
	''' verProc : '''
	global llamada
	if busquedaFunc(p[-1]) == -1 :
		print "ESTA FUNCION NO ESTA DECLARADA"
	else:
		llamada = p[-1]
	pass

def p_generarEra(p):
	''' generarERA : "(" '''
	global listaCuadruplos
	global listaFunciones
	global contParam
	global llamada
	contParam = 0
	pos = busquedaLista()
	arrParametros = listaFunciones[pos].arrParam
	longitud = len (arrParametros)
	cuadr = Cuadruplo(30, -1, -1, llamada)
	listaCuadruplos.append(cuadr)
	print "Se guardo ERA ", llamada
	pass

def p_auxExp(p):
	''' auxExp : listaExp llegaComa
				| listaExp  '''
	pass

def p_llegaComa(p):
	''' llegaComa : "," '''
	global contParam
	contParam = contParam + 1
	pass

def p_verificarTiposFunc(p):
	''' verificarTiposFunc : '''
	global pilaOperandos
	global pilaOperandosDirMem
	global listaFunciones
	global contParam
	global listaCuadruplos
	pos = busquedaFunc(llamada)
	arrParametros = listaFunciones[pos].arrParam
	auxParam = arrParametros[contParam].tipo
	auxPila = pilaOperandos.pop()
	mem = pilaOperandosDirMem.pop()
	if(auxParam != auxPila):
		print "TIPO DE PARAMETRO INCORRECTO"
	else: 
		cuadr = Cuadruplo(31, -1, mem, contParam)
		listaCuadruplos.append(cuadr)
	pass

def p_listaExp(p):
	'''listaExp : exp verificarTiposFunc masExps'''
	pass

def p_masExps(p):
	''' masExps : llegaComa listaExp
				|'''
	pass

def p_asignacion(p):
	''' asignacion : ID guardarIDPila opcionAsignacion valorAsig ";" checarOperadorIgual
				 | ID ";" '''
	pass

def p_guardarIDPila(p): 
	''' guardarIDPila : '''
	global pilaOperandos
	global listaCuadruplos
	global pilaOperandosDirMem
	posicion = busquedaLista()
	print "guardarIDPila", p[-1]
	posicion2 = busquedaVar(p[-1])
	if posicion2 != -1:
		memoria = listaFunciones[posicion].arrVar[posicion2]
		pilaOperandos.append(memoria.tipo)
		pilaOperandosDirMem.append(memoria.direcmem)
	else:
		print "NO SE PUEDE HACER UNA ASIGNACION A UNA VARIABLE QUE NO EXISTA"

	pass

def p_checarOperadorIgual(p):
	'''checarOperadorIgual :  '''
	global pilaOperadores
	signo = pilaOperadores.pop()
	if(signo == 5):
		operando2 = pilaOperandos.pop()
		operando1 = pilaOperandos.pop()
		resultado = cuboSemantico[operando1][operando2][signo]
		if(resultado == -1):
			print "Error con signo = "
		else: 
			print("SE CHECO EL CUADRUPLO ASIGNACION Y ES CORRECTO ", operando1, operando2, signo)
			operando2C = pilaOperandosDirMem.pop()
			operando1C = pilaOperandosDirMem.pop()
			cuadr = Cuadruplo(signo, operando2C, -1, operando1C)

			listaCuadruplos.append(cuadr)
	pass

def p_opcionAsignacion(p):
	''' opcionAsignacion : "[" CTI "]"
						| "[" CTI "]" "[" CTI "]"
						| empty '''
	pass

def p_valorAsig(p):
	''' valorAsig : "="  exp
				  | empty'''
	
	global pilaOperadores

	if p[1] == "=":
		pilaOperadores.append(5)

	pass

def p_guardarToken(p):
	'''guardarToken :  '''
	global pilaOperadores
	if p[-1] == "leer":
		pilaOperadores.append(18)
	elif p[-1] == "dibujar":
		pilaOperadores.append(19)
	elif p[-1] == "mueve":
		pilaOperadores.append(24)	
	pass

def p_checarLectura(p):
	''' checarLectura : '''
	global pilaOperadores
	global pilaOperandos
	global listaCuadruplos
	signo = pilaOperadores.pop()
	if signo == 18: 
		 operando1C = pilaOperandos.pop()
		 memoria = pilaOperandosDirMem.pop()
		 cuadr = Cuadruplo(signo, memoria,-1,-1)
		 listaCuadruplos.append(cuadr)
		 print "SE GUARDO EL CUADRUPLO DE LECTURA"
	pass

def p_lectura(p):
	''' lectura : LEER guardarToken ID guardarIDPila  checarLectura opcionesLectura ";" '''
	pass

def p_opcionesLectura(p):
	''' opcionesLectura : "[" CTI "]"
						| "[" CTI "]" "[" CTI "]"
						| empty '''
	pass

def p_guardarParametros(p):
	''' guardarParametros : ID guardarIDPila pos color checarDibujar '''	
	pass

def p_checarDibujar(p):
	''' checarDibujar : '''
	global pilaOperadores
	global pilaOperandos
	global listaCuadruplos
	signo = pilaOperadores.pop()
	if signo == 19:
		col = pilaOperandos.pop()
		posy = pilaOperandosDirMem.pop()
		posx = pilaOperandosDirMem.pop()
		ids = pilaOperandosDirMem.pop()
		cuadr = Cuadruplo(signo, ids, [posx,posy], col)
		listaCuadruplos.append(cuadr)
		pilaOperandos.pop()
		pilaOperandos.pop()
		pilaOperandos.pop()
		print "SE GUARDO EL CUADRUPLO DE DIBUJAR"

def p_escritura(p):
	''' escritura : DIBUJAR guardarToken "("  guardarParametros ")" ";"
				  |  mueve '''
	pass

def p_color(p):
	''' color : AMARILLO
			  | VERDE
			  | ROJO
			  | AZUL '''
	if p[-1] == "amarillo":
		pilaOperandos.append(20)
	elif p[-1] == "verde":
		pilaOperandos.append(21)
	elif p[-1] == "rojo":
		pilaOperandos.append(22)
	elif p[-1] == "azul":
		pilaOperandos.append(23)
	pass

def p_condicion(p):
	''' condicion : IF "(" expresion ")" checarIF finPilaSaltos
				  | IF "(" expresion ")" checarIF checarElse  finPilaSaltos'''
	pass

def p_bloqueCond(p):
	'''bloqueCond : "{" estatuto regresaCond "}" 
				  |  "{" regresaCond "}" 
				  | "{"  "}" '''
	print("BLOQUE CONDICIONALES")
	pass

def p_regresaCond(p):
	''' regresaCond :  RETURN ID
					| empty'''
	pass

def p_checarIF(p):
	'''checarIF : bloqueCond '''
	print "Entre a checar IF"
	global pilaOperandos
	global pilaSaltos
	global pilaOperadores
	aux = pilaOperandos.pop()
	if aux != 8: 
		print "Error semantico en condicion IF"
	else:
		lenCuadruplos = len(listaCuadruplos)
		pilaSaltos.append(lenCuadruplos)
		cuadr = Cuadruplo(16,-1,-1,0)
		print "Guarde cuadruplo IF"
		listaCuadruplos.append(cuadr)
		print pilaOperandos
		print pilaOperadores

	pass

def p_checarElse(p):
	'''checarElse : ELSE bloqueCond  '''
	print "Entre a checar else"
	global pilaSaltos
	global listaCuadruplos
	#meter cuadruplo de go to a la pila
	cuadr = Cuadruplo(17,-1,-1,0)
	listaCuadruplos.append(cuadr)
	#rellena el goto falso
	lenCuadruplos = len(listaCuadruplos)
	salto = pilaSaltos.pop()
	listaCuadruplos[salto].temporal = lenCuadruplos
	pilaSaltos.append(lenCuadruplos - 1)
	pass

def p_finPilaSaltos(p):
	'''finPilaSaltos : '''
	print "Entre fin pila saltos"
	salto = pilaSaltos.pop()
	lenCuadruplos = len(listaCuadruplos)
	listaCuadruplos[salto].temporal = lenCuadruplos - 1
	pass

def p_expresion(p):
	'''expresion :  exp operacionLogica checaoperador6
				 | exp '''
	pass

def p_push_logica(p):
	'''push_logica : 	  ">" 
						| "<" 
				 		| MENORIGUAL  
				 		| MAYORIGUAL 
				 	   	| IGUALIGUAL  
				 		| DIFERENTE 
						| COOR
						| COAND  '''
	global pilaOperadores
	print ("Operador logico: ", p[1])
	if p[1] == ">":
		pilaOperadores.append(6)
	elif p[1] == "<":
		pilaOperadores.append(7)
	elif p[1] == "<=":
		pilaOperadores.append(9)
	elif p[1] == ">=":
		pilaOperadores.append(8)
	elif p[1] == "==":
		pilaOperadores.append(10)
	elif p[1] == "!=":
		pilaOperadores.append(11)
	elif p[1] == "OR":
		pilaOperadores.append(12)
	elif p[1] == "&&":
		pilaOperadores.append(13)
	pass

def p_operacionLogica(p):
	'''operacionLogica : push_logica exp
						 | '''
	pass

def p_checaoperador6(p):
	'''checaoperador6 : '''
	global pilaOperadores
	global pilaOperandos
	global diccionarioMemoria
	opr = len(pilaOperadores)
	print "Entra checaroperador 6"
	print ("PilaOperadores: ", pilaOperadores)
	if(opr != 0):
		if((pilaOperadores[opr-1] == 6) | (pilaOperadores[opr-1] == 7) | (pilaOperadores[opr-1] == 8) | (pilaOperadores[opr-1] == 9) | (pilaOperadores[opr-1] == 10) | (pilaOperadores[opr-1] == 11) | (pilaOperadores[opr-1] == 12) | (pilaOperadores[opr-1] == 13) ):
			operando2 = pilaOperandos.pop()
			operando1 = pilaOperandos.pop()
			operadorActual = pilaOperadores.pop()
			resultado = cuboSemantico[operando1][operando2][operadorActual]
			posicion = busquedaLista()
			var = diccionarioMemoria['3']
			valormem = var[str(resultado)]
			agregarVar = TVar('temp', resultado, valormem)
			diccionarioMemoria['3'][str(resultado)] = valormem + 1
			listaFunciones[posicion].arrVar.append(agregarVar)
			pilaOperandosDirMem.append(valormem)
			print("Resultado: ", resultado)
			#meter a pila el temporal 
			if resultado == -1:
				print "ERROR: Operacion invalida, tipos no compatibles"
			else:
				print("SE CHECO EL CUADRUPLO Y ES CORRECTO", operando2, operando1, operadorActual)
				resultadoT = valormem
				operando2C = pilaOperandosDirMem.pop()
				operando1C = pilaOperandosDirMem.pop()
				cuadr = Cuadruplo(operadorActual, operando1C,operando2C,resultadoT)
				listaCuadruplos.append(cuadr)
				pilaOperandos.append(resultado)
	pass

def p_exp(p):
	'''exp : termino  checaroperador4'''
	print("Entra exp. ", p[1])

	pass

def p_fondoFalso(p):
	'''fondoFalso : "(" '''
	print "PARENTESIS ( "
	global pilaOperadores
	pilaOperadores.append(14)
	pass

def p_finFondoFalso(p):
	'''finFondoFalso : ")" ''' 
	print "PARENTESIS ) "
	global pilaOperadores
	print("Entra Fondo Folso: ", pilaOperadores.pop())
	pass

# def p_operacion(p):
# 	'''operacion : termino checaroperador4
# 		   		 | termino checaroperador4 signo '''
# 	print "entre a operacion"
# 	pass

def p_checaroperador4(p):
	'''checaroperador4 : signo
					   | '''
	global pilaOperadores
	global pilaOperandos
	global diccionarioMemoria
	opr = len(pilaOperadores)
	print "Entra checaroperador4"
	print ("PilaOperadores: ", pilaOperadores)
	if(opr != 0):
		if((pilaOperadores[opr-1] == 1) | (pilaOperadores[opr-1] == 2)):

			operando2 = pilaOperandos.pop()
			operando1 = pilaOperandos.pop()
			operadorActual = pilaOperadores.pop()
			resultado = cuboSemantico[operando1][operando2][operadorActual]
			posicion = busquedaLista()
			var = diccionarioMemoria['3']
			valormem = var[str(resultado)]
			agregarVar = TVar('temp', resultado, valormem)
			diccionarioMemoria['3'][str(resultado)] = valormem + 1
			listaFunciones[posicion].arrVar.append(agregarVar)
			pilaOperandosDirMem.append(valormem)
			print("Resultado: ", resultado)
			#meter a pila el temporal 
			if resultado == -1:
				print "ERROR: Operacion invalida, tipos no compatibles"
			else:
				print("SE CHECO EL CUADRUPLO Y ES CORRECTO", operando2, operando1, operadorActual)
				print pilaOperandosDirMem
				resultadoT = pilaOperandosDirMem.pop()
				operando2C = pilaOperandosDirMem.pop()
				operando1C = pilaOperandosDirMem.pop()
				pilaOperandosDirMem.append(resultadoT)
				cuadr = Cuadruplo(operadorActual, operando1C,operando2C,resultadoT)
				listaCuadruplos.append(cuadr)
				pilaOperandos.append(resultado)
	pass

def p_signo(p):
	'''signo : push_pm exp
			 | '''

def p_push_pm(p):
	'''push_pm : "+" 
			| "-" '''
	print("OPERADOR: ", p[1])
	global pilaOperadores
	if p[1] == "+":
		pilaOperadores.append(1)
	else:
		pilaOperadores.append(2)
	pass 

def p_termino(p):
	'''termino : factor checaroperador5'''
	print ("Entre Termino ", p[1])
	pass

def p_checaroperador5(p):
	'''checaroperador5 : masop
					   | '''
	global pilaOperadores
	global pilaOperandos
	global diccionarioMemoria
	opr = len(pilaOperadores)
	print "Entre a checaroperador5"
	print ("PilaOperadores: ", pilaOperadores)	
	if(opr != 0):
		print("pila operadores",pilaOperadores[opr-1] )
		if((pilaOperadores[opr-1] == 3) | (pilaOperadores[opr-1] == 4)):
			operando2 = pilaOperandos.pop()
			operando1 = pilaOperandos.pop()
			operadorActual = pilaOperadores.pop()
			resultado = cuboSemantico[operando1][operando2][operadorActual]
			posicion = busquedaLista()
			var = diccionarioMemoria['3']
			valormem = var[str(resultado)]
			agregarVar = TVar('temp', resultado, valormem)
			diccionarioMemoria['3'][str(resultado)] = valormem + 1
			listaFunciones[posicion].arrVar.append(agregarVar)
			pilaOperandosDirMem.append(valormem)
			print("resultado checaroperador5", resultado)
			#meter a pila el temporal 
			if resultado == -1:
				print "ERROR: Operacion invalida, tipos no compatibles"
			else:
				print("SE CHECO EL CUADRUPLO Y ES CORRECTO", operando2, operando1, operadorActual)
				resultadoT = valormem
				operando2C = pilaOperandosDirMem.pop()
				operando1C = pilaOperandosDirMem.pop()
				cuadr = Cuadruplo(operadorActual, operando1C,operando2C,resultadoT)
				listaCuadruplos.append(cuadr)
				pilaOperandos.append(resultado)
	pass

def p_masop(p):
	'''masop : push_td termino
			| '''

def p_push_td(p):
	'''push_td : "*"
 			   | "/"'''
 	global pilaOperadores
 	print("OPERADOR: ", p[1])
	if p[1] == "*":
		pilaOperadores.append(3)
	else:
		pilaOperadores.append(4)
 	pass

def p_factor(p):
	'''factor : fondoFalso expresion finFondoFalso
			  | varcte '''
	print "Entre a Factor"
	pass

def p_pos(p):
	''' pos : "(" varcte "," varcte ")" '''
	pass

def p_whiles(p):
	''' whiles : WHILE checarWhile "(" expresion ")" checarContenido bloqueCond finPilaSaltosWhile '''
	pass

def p_checarWhile(p):
	''' checarWhile : '''
	global pilaSaltos
	global listaCuadruplos
	lenCuadruplos = len(listaCuadruplos)
	pilaSaltos.append(lenCuadruplos)
	print "Se guardo el salto. " , len(pilaSaltos)
	pass

def p_checarContenido(p):
	''' checarContenido : '''
	global pilaSaltos
	global listaCuadruplos
	global pilaOperandos
	aux = pilaOperandos.pop()
	if aux != 8:
		print "Error semantico en while"
	else:
		resultado = aux
		#GOTO FALSO RESULTADO _____
		cuadr = Cuadruplo(16,-1, resultado ,0)
		listaCuadruplos.append(cuadr)
		pilaSaltos.append(len(listaCuadruplos) - 1)
		print "Se guardo GOTO FALSO WHILE: ", cuadr.operador, cuadr.temporal
	pass

def p_finPilaSaltosWhile(p):
	'''finPilaSaltosWhile : '''
	global pilaSaltos
	global listaCuadruplos
	saltos = pilaSaltos.pop()
	cuadr = Cuadruplo(17,-1,-1,saltos)
	listaCuadruplos.append(cuadr)
	lenCuadruplos = len(listaCuadruplos)
	listaCuadruplos[saltos].temporal = lenCuadruplos
	print "Se guardo GOTO RETORNO: ", cuadr.operador, cuadr.temporal
	pass

def p_varcte(p):
	''' varcte : recibe_ID 
			   | recibe_CTF 
			   | recibe_CTI  
			   | recibe_TRUE 
			   | recibe_FALSE '''
	pass

def p_recibe_ID(p):
	''' recibe_ID : ID '''
	print("VARCTE: ", p[1])
	pos = busquedaLista()
	print("Guardar: ", p[1])
	pos2 = busquedaVar(p[1])
	if(pos2 != -1 ):
		var = listaFunciones[pos].arrVar[pos2].tipo
		direc = listaFunciones[pos].arrVar[pos2].direcmem
		pilaOperandosDirMem.append(direc)
		pilaOperandos.append(var)
	else:
		print "ERROR: NO SE ENCUENTRA EL ID QUE QUIERES USAR"
	pass

def p_recibe_CTF(p):
	''' recibe_CTF : CTF '''
	print("VARCTE: ", p[1])
	global diccionarioMemoria
	global diccConstantes
	posicion = busquedaLista()
	var = diccionarioMemoria['4']
	valormem = var[str(7)]
	agregarVar = TVar(p[1],7, valormem)
	diccionarioMemoria['4'][str(7)] = valormem + 1
	listaFunciones[posicion].arrVar.append(agregarVar)
	diccConstantes[valormem] = p[1]
	pilaOperandosDirMem.append(valormem)
	pilaOperandos.append(7)
	pass

def p_recibe_CTI(p):
	''' recibe_CTI : CTI '''
	print("VARCTE: ", p[1])
	global diccionarioMemoria
	global diccConstantes
	posicion = busquedaLista()
	var = diccionarioMemoria['4']
	valormem = var[str(1)]
	agregarVar = TVar(p[1],1, valormem)
	diccionarioMemoria['4'][str(1)] = valormem + 1
	listaFunciones[posicion].arrVar.append(agregarVar)
	diccConstantes[valormem] = p[1]
	pilaOperandosDirMem.append(valormem)
	pilaOperandos.append(1)
	pass

def p_recibe_TRUE(p):
	''' recibe_TRUE : TRUE '''
	print("VARCTE: ", p[1])
 	global diccionarioMemoria
	posicion = busquedaLista()
	var = diccionarioMemoria['4']
	valormem = var[str(8)]
	agregarVar = TVar(p[1],8, valormem)
	diccionarioMemoria['4'][str(8)] = valormem + 1
	listaFunciones[posicion].arrVar.append(agregarVar)
	pilaOperandosDirMem.append(valormem)
	pilaOperandos.append(8)
	pass

def p_recibe_FALSE(p):
	''' recibe_FALSE : FALSE '''
	print("VARCTE: ", p[1])
	global diccionarioMemoria
	posicion = busquedaLista()
	var = diccionarioMemoria['4']
	valormem = var[str(8)]
	agregarVar = TVar(p[1],8, valormem)
	diccionarioMemoria['3'][str(8)] = valormem + 1
	listaFunciones[posicion].arrVar.append(agregarVar)
	pilaOperandosDirMem.append(valormem)
	pilaOperandos.append(8)
	pass

def p_tipo(p):
	''' tipo : ENTERO 
			 | DECIMAL 
			 | BOOL
			 | VOID 
			 | CUADRADO 
			 | RECTANGULO 
			 | CIRCULO 
			 | LINEA 
			 | ESTRELLA '''
	global tipoActual
	if(p[1] == "entero"):
		tipoActual = 1
	elif(p[1] == "decimal"):
		tipoActual = 7
	elif(p[1] == "cuadrado"):
		tipoActual = 2
	elif(p[1] == "rectangulo"):
		tipoActual = 2
	elif(p[1] == "circulo"):
		tipoActual = 4
	elif(p[1] == "linea"):
		tipoActual = 5
	elif(p[1] == "estrella"):
		tipoActual = 6
	elif(p[1] == "void"):
		tipoActual = 9
	elif(p[1] == "bool"):
		tipoActual = 8
	pass

def p_mueve(p):
	''' mueve : MUEVE guardarToken opcionMue '''
	pass

def p_opcionMue(p):
	''' opcionMue : direccion ID guardarIDPila recibe_CTI checarMover ";" '''
	pass

def p_direccion(p):
	''' direccion : IZQUIERDA
				| DERECHA
				| ARRIBA
				| ABAJO '''
	if p[1] == "izquierda":
		pilaOperandos.append(25)
	elif p[1] == "derecha":
		pilaOperandos.append(26)
	elif p[1] == "arriba":
		pilaOperandos.append(27)
	elif p[1] == "abajo":
		pilaOperandos.append(28)
	pass

def p_checarMover(p):
	''' checarMover : '''
	global pilaOperadores
	global pilaOperandos
	global listaCuadruplos
	signo = pilaOperadores.pop()
	if signo == 24:
		cant = pilaOperandosDirMem.pop()
		ids = pilaOperandosDirMem.pop()
		dirc = pilaOperandos.pop()
		cuadr = Cuadruplo(signo, ids, dirc, cant)
		listaCuadruplos.append(cuadr)
		pilaOperandos.pop()
		pilaOperandos.pop()
		print "SE GUARDO EL CUADRUPLO DE DIBUJAR"

def p_empty(p):
    'empty : '
    print("SALTO DE LINEA")
    pass

# Funcion para guardar los datos necesarios 
# para la creacion de la maquina virtual
def escribeArchivo():
	archivo = open ('maquiVirtual.txt', 'w')
	global listaFunciones
	global listaCuadruplos
	global diccConstantes
	#Las funciones se guardan de la siguiente forma:
	#nombre tipo varLoca VarTemporales varEnt varDec varCuadrado varRect varCirc varLinea varEstrella varBool inicioCuadruplo cantidadParametros.
	for elemento in listaFunciones:
		archivo.write(elemento.nombre)
		archivo.write(' ')
		archivo.write(str(elemento.tipo))
		archivo.write(' ')
		archivo.write(str(elemento.varEnt))
		archivo.write(' ')
		archivo.write(str(elemento.varDec))
		archivo.write(' ')
		archivo.write(str(elemento.varCuadrado))
		archivo.write(' ')
		archivo.write(str(elemento.varRect))
		archivo.write(' ')
		archivo.write(str(elemento.varCirc))
		archivo.write(' ')
		archivo.write(str(elemento.varLin))
		archivo.write(' ')
		archivo.write(str(elemento.varEstr))
		archivo.write(' ')
		archivo.write(str(elemento.varBool))
		archivo.write(' ')
		archivo.write(str(elemento.varEntTemp))
		archivo.write(' ')
		archivo.write(str(elemento.varDecTemp))
		archivo.write(' ')
		archivo.write(str(elemento.varCuadradoTemp))
		archivo.write(' ')
		archivo.write(str(elemento.varRectTemp))
		archivo.write(' ')
		archivo.write(str(elemento.varCircTemp))
		archivo.write(' ')
		archivo.write(str(elemento.varLinTemp))
		archivo.write(' ')
		archivo.write(str(elemento.varEstrTemp))
		archivo.write(' ')
		archivo.write(str(elemento.varBoolTemp))
		archivo.write(' ')
		archivo.write(str(elemento.cuadruploInicial))
		archivo.write(' ')
		archivo.write(str(len(elemento.arrParam)))
		archivo.write('\n')
	archivo.write('$$\n')
	for elemento in diccConstantes:
		archivo.write(str(elemento))
		archivo.write(' ')
		archivo.write(str(diccConstantes[elemento]))
		archivo.write('\n')
	archivo.write('$$\n')
	for elemento in listaCuadruplos:
		archivo.write(str(elemento.operador))
		archivo.write(' ')
		archivo.write(str(elemento.operando1))
		archivo.write(' ')
		archivo.write(str(elemento.operando2))
		archivo.write(' ')
		archivo.write(str(elemento.temporal))
		archivo.write('\n')
	archivo.write('$$\n')

	archivo.close()

def p_error(p):
    print("Syntax error")
    
import ply.yacc as yacc
parser = yacc.yacc()
#yacc.yacc()
file = open("prueba.txt", "r")
yacc.parse(file.read())
file.close()
