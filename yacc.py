import ply.yacc as yacc
from TFunc import TFunc
from TVar import TVar
from CuboSemantico import cuboSemantico
from diccionarioMemoria import diccionarioMemoria
from Cuadruplo import Cuadruplo
import sys
# Get the token map from the lexer.  This is required.
from lex import tokens

#variables globales para el manejo de funciones, cuadruplos y validaciones
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
colArreglo = 0
renArreglo = 0
renglon = 0
columna = 0
DEBUG = True
idActual = ""
cuadr = Cuadruplo(17, -1, -1, -1)
listaCuadruplos.append(cuadr)
# BNF
#Sintaxis que inicia el programa
def p_programa(p):
	'''programa : vars funcion INICIO funcAgregarInicio bloque  FIN liberarVar
	  			| vars funcion INICIO FIN '''	
	print("SE TERMINO EL PROGRAMA CON EXITO!")
	escribeArchivo()
	pass

#Regla para guardar en diccionario de funciones la funcion de inicio
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
#Bloque del main del programa, inicio-fin
def p_bloque(p):
	'''bloque : "{" vars guardarCuadruplo estatuto "}"
			  | "{" vars guardarCuadruplo "}"
			  | "{" "}"'''
	print("BLOQUE")
	pass
#Sintaxis de declaracion de variables
def p_vars(p):
	'''vars : tipo listaIDS ";" masTipos
		| tipo ID guardarIDs  arreglo  ";" masTipos
		| empty'''
	print("VARS: Estructura basica")
	pass
#Permite la declaracion de diferentes tipos de datos
def p_masTipos(p):
	'''masTipos : vars 
				| empty '''
	pass
# permite tener mas de un id del mismo tipo
def p_listaIDS(p):
	''' listaIDS : ID guardarIDs masIDS '''
	pass
#Regla que permite tener diferentes IDs
def p_masIDS(p):
	'''masIDS :  "," ID guardarIDs masIDS2
			   | empty '''
	pass

def p_masIDS2(p):
	'''masIDS2 :  "," ID guardarIDs masIDS
			   | empty '''
	pass
#Sintaxis para declaracion de arreglos
def p_arreglo(p):
	''' arreglo : "[" expresion  guardarExpArr  '''
	global pilaOperandos
	global pilaOperandosDirMem
	global listaFunciones
	pos = busquedaLista()
	pos1 = busquedaVar(p[-2])
	print "Entre  a arreglo"
	if len(pilaOperandosDirMem) > 0:
		pilaOperandosDirMem.pop()
	pass
#Funcion que guarda el id y valores de un arreglo, manda a llamar la opcion de poner matriz
def p_guardarExpArr(p):
	''' guardarExpArr :  "]" matriz '''
	global pilaOperandos
	global pilaOperandosDirMem
	global listaFunciones
	global diccionarioMemoria
	global tipoActual
	global tipofuncMem
	print "Entre a guardar exp arreglo"
	if(len(pilaOperandosDirMem) != 1) and (len(pilaOperandosDirMem) > 0):
		operando1 = pilaOperandosDirMem.pop()
		res = pilaOperandosDirMem.pop()
		pos = busquedaLista()
		pos2 = busquedaVarDir(res)

		aux = diccConstantes[operando1]
		diccionarioMemoria[tipofuncMem][str(tipoActual)] = diccionarioMemoria[tipofuncMem][str(tipoActual)] + aux

		var = listaFunciones[pos].arrVar[pos2]
		var.col = 0
		var.ren = operando1
		pilaOperandos.pop()
	pass
#Sintaxis para la declaracion de matrices
def p_matriz(p):
	''' matriz : "[" expresion guardarExpMat
			   | empty '''
	pass
#Sintaxis para guardar los renglones y columnas de la matriz a su id correspondiente.
def p_guardarExpMat(p):
	''' guardarExpMat :  "]" '''
	global pilaOperandos
	global pilaOperandosDirMem
	global listaFunciones
	print "Entre guardar exp Matriz"
	operando2 = pilaOperandosDirMem.pop()
	operando1 = pilaOperandosDirMem.pop()
	res = pilaOperandosDirMem.pop()
	pos = busquedaLista()
	pos2 = busquedaVarDir(res)
	
	aux = diccConstantes[operando2]
	aux2 = diccConstantes[operando1]
	aux1 = aux * aux2

	diccionarioMemoria[tipofuncMem][str(tipoActual)] = diccionarioMemoria[tipofuncMem][str(tipoActual)] + aux1

	var = listaFunciones[pos].arrVar[pos2]
	var.col = operando2
	var.ren = operando1
	pilaOperandos.pop()
	pilaOperandos.pop()
	
	pass
#Sintaxis para la creacion de funciones
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
#Funcion que contiene los elementos de la declaracion de una funcion
def p_restoFuncion(p):
	''' restoFuncion : "(" param ")" bloquefunc'''
	pass
#Regla para agregar las funciones al diccionario de funciones
def p_funcAgregar(p):
	'''funcAgregar :  '''
	print "Entre a funcAgregar"
	global funcionActual
	global listaFunciones
	global tipoActual
	global tipofuncMem
	global diccionarioVarGlobal
	tipofuncMem = '2'
	funcionActual = p[-1]
	objetoFuncion = TFunc(p[-1], tipoActual, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {}, {})
	#checar si ya existe una funcion
	posicion = busquedaLista()
	if posicion != -1:
		print "FUNCION PREVIAMENTE DECLARADA"
		sys.exit()
	else:
		print "Entre al else FuncAgregar"
		listaFunciones.append(objetoFuncion)
		var = diccionarioMemoria['1']
		valormem = var[str(tipoActual)]
		diccionarioMemoria['1'][str(tipoActual)] = valormem + 1
		diccionarioVarGlobal[p[-1]] = valormem

#Funcion que maneja los parametros de una funcion
def p_param(p):
	''' param : tipo  ID guardarIDParam maspaID 
		 		| empty'''
	pass
#Regla para guardar los parametros y verificar que se puedan usar
def p_guardarIDParam(p):
	''' guardarIDParam : '''
	global funcionActual
	global listaFunciones
	global tipoActual
	global diccionarioMemoria
	#checar si ya existe una variable
	if (busquedaVar(p[-1]) != -1 ):
		print "SE DECLARO UNA VARIABLE PREVIAMENTE DECLARADA"
		sys.exit()
	else:
		posicion = busquedaLista()
		var = diccionarioMemoria[tipofuncMem]
		valormem = var[str(tipoActual)]
		agregarVar = TVar(p[-1], tipoActual, valormem,0,0)
		diccionarioMemoria[tipofuncMem][str(tipoActual)] = valormem + 1
		listaFunciones[posicion].arrParam.append(agregarVar)
		print "Se guardo el parametro en la tabla de parametros ", tipoActual
#Funcion para buscar la funcion actual en lista de funciones
def busquedaLista():
	cont = 0
	global listaFunciones
	global funcionActual
	for elemento in listaFunciones:
		if elemento.nombre == funcionActual : 
			return cont
		cont += 1
	return -1
#Funcion para buscar una funcion en especifico 
def busquedaFunc(funcionLlamar):
	cont = 0
	global listaFunciones
	for elemento in listaFunciones:
		if elemento.nombre == funcionLlamar : 
			return cont
		cont += 1
	return -1
#Funcion para buscar una variable en la tabla de variables de la funcion 
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

#Funcion para buscar una variable en la tabla de variables de la funcion 
def busquedaVarDir(varActual):
	global listaFunciones
	global funcionActual
	cont = 0
	for elemento in listaFunciones:
		if funcionActual == elemento.nombre:
			for elemento2 in elemento.arrVar:
				if(varActual == elemento2.direcmem):
					return cont
				else:
					cont += 1
	return -1

#Funcion para buscar una variable en la tabla de parametros de la funcion 
def busquedaVarParam(varActual):
	global listaFunciones
	global funcionActual
	cont = 0
	for elemento in listaFunciones:
		if funcionActual == elemento.nombre:
			for elemento2 in elemento.arrParam:
				if(varActual == elemento2.nombre):
					return cont
				else:
					cont += 1
	return -1

#Funcion para buscar si hay uan variable global previamente declarada y si no regresa -1 para poder declararla
def busquedaVarGlobal(var):
	global diccionarioVarGlobal
	if diccionarioVarGlobal.has_key(var):
		return -1
#Funcion que recibe el ID y la declara en su tabla correspondiente asignandole un valor de memoria.
#Asimismo guarda su direccion en la pilaOperandosDirMem
def p_guardarIDs(p):
	''' guardarIDs : '''
	global funcionActual
	global listaFunciones
	global tipoActual
	global tipofuncMem
	global diccionarioMemoria
	global pilaOperandosDirMem
	if(tipofuncMem == '1'):
		if busquedaVarGlobal(p[-1]) == -1:
			"SE DECLARO UNA VARIABLE PREVIAMENTE DECLARADA"
			sys.exit()
		else:
			var = diccionarioMemoria[tipofuncMem]
			valormem = var[str(tipoActual)]
			diccionarioMemoria[tipofuncMem][str(tipoActual)] = valormem + 1
			diccionarioVarGlobal[p[-1]] = valormem
			print "Se guardo la variable global en el diccionario ", tipoActual
	#checar si ya existe una variable
	else:
		if (busquedaVar(p[-1]) != -1 ):
			print "SE DECLARO UNA VARIABLE PREVIAMENTE DECLARADA"
			sys.exit()
		else:
			posicion = busquedaLista()
			var = diccionarioMemoria[tipofuncMem]
			valormem = var[str(tipoActual)]
			agregarVar = TVar(p[-1], tipoActual, valormem,0,0)
			diccionarioMemoria[tipofuncMem][str(tipoActual)] = valormem + 1 
			listaFunciones[posicion].arrVar.append(agregarVar)
			pilaOperandosDirMem.append(valormem)
			print "Se guardo la variable en la tabla ", tipoActual, p[-1]

def p_maspaID(p):
	''' maspaID : "," param
				| empty '''
	pass
#Sintaxis de bloque de una funcuion 
def p_bloquefunc(p): 
	''' bloquefunc : "{" vars guardarCuadruplo estatuto regresa "}" liberarVar 
				   | "{" vars guardarCuadruplo regresa "}" liberarVar
				   | "{" guardarCuadruplo escritura regresa "}" liberarVar
				   | "{" "}" '''
	pass
#Regla para liberar la tabla de variables de una funcion 
def p_liberarVar(p):
	''' liberarVar : '''
	global diccionarioMemoria
	global listaFunciones
	global listaCuadruplos
	global funcionActual
	global pilaOperandos
	global pilaOperandosDirMem
	global pilaOperadores
	global diccionarioVarGlobal
	posicion = busquedaLista()
	pilaOperandosDirMem = []
	pilaOperandos = []
	pilaOperadores = []
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
	pass
#Regla para actualizar los gotos de una funcion
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
#Sintaxis para el retorno de una variable
def p_regresa(p):
	''' regresa : RETURN expresion generarCuadRetorno'''
	pass
#Funcion la cual genera el cuadruplo de retorno de una funcion, guardandola en la lista de cuadruplos.
def p_generarCuadRetorno(p):
	''' generarCuadRetorno : '''
	global listaCuadruplos
	global diccionarioVarGlobal
	global pilaOperadores
	global pilaOperandosDirMem
	global funcionActual
	global listaFunciones
	global pilaOperandos
	posicion = busquedaLista()
	posicion2 = busquedaVar(p[-1])
	if posicion2 != -1:
		memoria = listaFunciones[posicion].arrVar[posicion2]
		pilaOperandos.append(memoria.tipo)
		pilaOperandosDirMem.append(memoria.direcmem)
	if funcionActual != 'inicio':
		aux = pilaOperandosDirMem.pop()
		cuadr = Cuadruplo(29, -1, aux, diccionarioVarGlobal[funcionActual])
		listaCuadruplos.append(cuadr)
		pilaOperandos.pop()
#Sintaxis para estatutos
def p_estatuto(p):
	'''estatuto : asignacion estatutoAux
				| escritura estatutoAux
				| condicion estatutoAux
				| whiles estatutoAux
				| funcs estatutoAux '''
	pass

def p_estatutoAux(p):
	''' estatutoAux : estatuto
					| empty'''
	pass
#Regla para verificar que el numero de parametros sea el mismo
def p_checaNumParam(p):
	''' checaNumParam : finFondoFalso'''
	global contParam
	global listaFunciones
	global llamada
	pos = busquedaFunc(llamada)
	numParam  = len(listaFunciones[pos].arrParam)
	if contParam + 1 != numParam:	
		print "El numero de parametros es incorrecto"
		sys.exit()
	pass
#Regla para generar los GoSub de las llamadas a una funcion
def p_generaGOSUB(p):
	'''generaGOSUB : '''
	global listaCuadruplos
	global llamada
	global diccionarioVarGlobal
	global listaFunciones

	print "Se guardo GOSUB", llamada
	pos = busquedaFunc(llamada)
	aux1 = listaFunciones[pos].cuadruploInicial

	cuadr = Cuadruplo(32,-1,-1,aux1)
	listaCuadruplos.append(cuadr)
	var = diccionarioMemoria['3']
	mem = var[str(listaFunciones[pos].tipo)]
	pos2 = diccionarioVarGlobal[llamada]
	cuadr = Cuadruplo(5,pos2,-1,mem)
	diccionarioMemoria['3'][listaFunciones[pos].tipo] = mem + 1
	listaCuadruplos.append(cuadr)
	pass
#Sintaxis de llamada a una funcion 
def p_funcs(p):
	''' funcs : ID guardarIDFunc verProc generarERA auxExp  checaNumParam generaGOSUB '''
	pass
#Funcion que guarda en pilaOperandosDirMem la direccion de memoria del ID de la funcion asi como su 
#tipo en pilaOperandos.
def p_guardarIDFunc(p):
	''' guardarIDFunc : '''
	global pilaOperandos
	global listaFunciones
	global diccionarioMemoria
	pos = busquedaFunc(p[-1])
	aux = listaFunciones[pos].tipo
	pilaOperandos.append(aux)
	print diccionarioVarGlobal
	aux1 = p[-1]
	pilaOperandosDirMem.append(diccionarioVarGlobal[p[-1]])

#Funcion que verifica si una funcion esta declarada o no
def p_verProc(p):
	''' verProc : '''
	global llamada
	if busquedaFunc(p[-2]) == -1 :
		print "ESTA FUNCION NO ESTA DECLARADA"
		sys.exit()
	else:
		llamada = p[-2]
	pass
#Regla para generar Era
def p_generarEra(p):
	''' generarERA : fondoFalso '''
	global listaCuadruplos
	global listaFunciones
	global contParam
	global llamada
	contParam = 0
	pos = busquedaLista()
	arrParametros = listaFunciones[pos].arrParam
	longitud = len (arrParametros)
	r = diccionarioVarGlobal[llamada]
	cuadr = Cuadruplo(30, -1, -1,r )
	listaCuadruplos.append(cuadr)
	print "Se guardo ERA ", llamada
	pass

def p_auxExp(p):
	''' auxExp : listaExp llegaComa
				| listaExp  '''
	pass
#Regla auxiliar para recibir la , de mas expresiones y contar los parametros
def p_llegaComa(p):
	''' llegaComa : "," '''
	global contParam
	contParam = contParam + 1
	pass
#Regla para verificar funciones
def p_verificarTiposFunc(p):
	''' verificarTiposFunc : '''
	global pilaOperandos
	global pilaOperandosDirMem
	global listaFunciones
	global contParam
	global listaCuadruplos
	global arrParametros
	global llamada
	pos = busquedaFunc(llamada)
	arrParametros = listaFunciones[pos].arrParam
	auxParam = arrParametros[contParam].tipo
	auxPila = pilaOperandos.pop()
	mem = pilaOperandosDirMem.pop()
	if(auxParam != auxPila):
		print "TIPO DE PARAMETRO INCORRECTO"
		sys.exit()
	else: 
		aux = arrParametros[contParam].direcmem
		cuadr = Cuadruplo(31, -1, mem,aux)
		listaCuadruplos.append(cuadr)
	pass

def p_listaExp(p):
	'''listaExp : exp verificarTiposFunc masExps'''
	pass

def p_masExps(p):
	''' masExps : llegaComa listaExp
				|'''
	pass
#Regla de sintaxis que maneja la asignacion, indicando que atributos debe de tener.
def p_asignacion(p):
	''' asignacion : ID guardarIDPila opcionAsignacion valorAsig expresion ";" checarOperadorIgual
				 '''
	pass
#Regla con la cual se guarda el ID en la pilaOperandosDirMem que se usa en un estatuto para poder
# utilizarlo en cada operacion que se indique.
def p_guardarIDPila(p): 
	''' guardarIDPila : '''
	global pilaOperandos
	global listaCuadruplos
	global pilaOperandosDirMem
	global renArreglo
	global idActual
	global colArreglo
	posicion = busquedaLista()
	print "guardarIDPila", p[-1]
	posicion2 = busquedaVar(p[-1])
	if posicion2 != -1:
		memoria = listaFunciones[posicion].arrVar[posicion2]
		pilaOperandos.append(memoria.tipo)
		pilaOperandosDirMem.append(memoria.direcmem)
		colArreglo = memoria.col
		renArreglo = memoria.ren
		idActual = p[-1]
	else:
		print "NO SE PUEDE HACER UNA ASIGNACION A UNA VARIABLE QUE NO EXISTA"
		sys.exit()

	pass
#Verfica que se pueda hacer una asignacion, es decir que los operandos sean compatibles
def p_checarOperadorIgual(p):
	'''checarOperadorIgual :  '''
	global pilaOperadores
	global listaCuadruplos
	global pilaOperandos

	signo = pilaOperadores.pop()
	if(signo == 5):
		operando2 = pilaOperandos.pop()
		operando1 = pilaOperandos.pop()
		resultado = cuboSemantico[operando1][operando2][signo]
		if(resultado == -1):
			print "Error con signo = "
			sys.exit()
		else: 
			print("SE CHECO EL CUADRUPLO ASIGNACION Y ES CORRECTO ", operando1, operando2, signo)
			operando2C = pilaOperandosDirMem.pop()
			operando1C = pilaOperandosDirMem.pop()
			cuadr = Cuadruplo(signo, operando2C, -1, operando1C)
			listaCuadruplos.append(cuadr)
	pass
#Regla para poder hacer una asignacion a una variable dimensionada
def p_opcionAsignacion(p):
	''' opcionAsignacion : checaDim fondoFalsoC expresion opcionmatriz 
 						| empty '''
 	pass

def p_fondoFalsoC(p):
	'''fondoFalsoC : "[" '''
	print "PARENTESIS [ "
	global pilaOperadores
	pilaOperadores.append(14)
	pass

def p_finfondoFalsoC(p):
	'''finfondoFalsoC : "]" '''
	print "PARENTESIS ] "
	global pilaOperadores
	pilaOperadores.pop
	pass
#Regla para poder manejar las variables dimensionadas
def p_opcionmatriz(p):
	'''opcionmatriz : finfondoFalsoC fondoFalsoC expresion generaCuadruploMatriz
					| generaCuadruploMatriz
					| empty '''
	pass
#Funcion que checa si una funcion es dimensionada o no 
def p_checaDim(p):
	''' checaDim : '''
	global pilaOperandosDirMem
	global pilaOperandos
	global listaFunciones
	global idActual
	pos = busquedaLista()
	if busquedaVar(idActual) != -1:
		pos2 = busquedaVar(idActual)
	elif busquedaVarGlobal(idActual) != -1:
		pos2 = busquedaVarGlobal(idActual)
	elif busquedaVarParam(idActual) != -1:
		pos2 = busquedaVarGlobal(idActual)
	else:
		print "No se encontro la variable dimensionada"
		sys.exit()

	var = listaFunciones[pos].arrVar[pos2]
	if var.ren != 0 or var.col != 0:
		pilaOperandos.pop()
		pilaOperandosDirMem.pop()
	pass
#Genera los cuadruplos necesarios para las variables dimensionadas
def p_generaCuadruploMatriz(p):
	''' generaCuadruploMatriz : "]" '''
	global listaCuadruplos
	global listaFunciones
	global pilaOperadores
	global pilaOperandosDirMem
	global colArreglo
	global idActual
	pilaOperadores.pop()
	print "Entre generaCuadruploMatriz", pilaOperandosDirMem
	pos = busquedaLista()
	func = listaFunciones[pos].arrVar
	longi = len(func)
	if colArreglo != 0:
		#genera cuadruplos para matrices
		pilaOperadores.pop()
		operando1 = pilaOperandos.pop()
		operandoMem1 = pilaOperandosDirMem.pop()
		operando2 = pilaOperandos.pop()
		operandoMem2 = pilaOperandosDirMem.pop()
		#cuadruplo verificar
		cuadr = Cuadruplo(33,operandoMem2, 0, renArreglo)
		print "renArreglo ", renArreglo
		listaCuadruplos.append(cuadr)
		#direccion base para cuadruplos
		if busquedaVar(idActual) != -1:
			aux = busquedaVar(idActual)
		elif busquedaVarGlobal(idActual) != -1:
			aux = busquedaVarGlobal(idActual)
		elif busquedaVarParam(idActual) != -1:
			aux = busquedaVarGlobal(idActual)
		else:
			print "No se encontro la variable dimensionada"
			sys.exit()
		dirBase = func[aux].direcmem

		var = diccionarioMemoria['3']
		mem = var[str(operando1)]
		cuadr = Cuadruplo(3, operandoMem2, operandoMem1, mem)
		listaCuadruplos.append(cuadr)
		cuadr2 = Cuadruplo(33,operandoMem1, 0, colArreglo)
		listaCuadruplos.append(cuadr2)
		cuadr1 = Cuadruplo(1, mem, operandoMem1, mem+1)
		diccionarioMemoria['3'][listaFunciones[pos].tipo] = mem + 2
		listaCuadruplos.append(cuadr1)
		print "colArreglo = ", colArreglo
		var1 = diccionarioMemoria['3']
		mem1 = var['9']
		cuadr = Cuadruplo(1, mem+1,dirBase, mem1)
		listaCuadruplos.append(cuadr)
		pilaOperandosDirMem.append(mem1)
		pilaOperandos.append(operando1)
		diccionarioMemoria['3']['9'] = mem1 + 1
	else:
		#genera cuadruplos para los arreglos
		operando1 = pilaOperandos.pop()
		operandoMem1 = pilaOperandosDirMem.pop()
		
		print "renArreglo = ", renArreglo, pilaOperandosDirMem

		cuadr = Cuadruplo(33,operandoMem1, 0, renArreglo)
		listaCuadruplos.append(cuadr)

		if busquedaVar(idActual) != -1:
			aux = busquedaVar(idActual)
		elif busquedaVarGlobal(idActual) != -1:
			aux = busquedaVarGlobal(idActual)
		elif busquedaVarParam(idActual) != -1:
			aux = busquedaVarGlobal(idActual)
		else:
			print "No se encontro la variable dimensionada"
			sys.exit()
		dirBase = func[aux].direcmem
		
		var = diccionarioMemoria['3']
		mem = var['9']
		cuadr = Cuadruplo(1, operandoMem1,dirBase, mem)
		listaCuadruplos.append(cuadr)
		pilaOperandosDirMem.append(mem)
		pilaOperandos.append(operando1)
		diccionarioMemoria['3']['9'] = mem + 1
	pass
#Regla que maneja el simbolo de =
def p_valorAsig(p):
	''' valorAsig : "="
				  | empty'''
	global pilaOperadores
	if p[1] == "=":
		pilaOperadores.append(5)

	pass
#Regla de sintaxis que guarda los signos de mostrar, dibujar, mueve asignandoles su numero
#numero correspondinete a operador
def p_guardarToken(p):
	'''guardarToken :  '''
	global pilaOperadores
	if p[-1] == "mostrar":
		pilaOperadores.append(18)
	elif p[-1] == "dibujar":
		pilaOperadores.append(19)
	elif p[-1] == "mueve":
		pilaOperadores.append(24)	
	pass

#Genera el cuadruplo de impresion
def p_checarImpresion(p):
	''' checarImpresion : '''
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

#Regla que maneja los atributos que debe de tener un parametro de dibujar
def p_guardarParametros(p):
	''' guardarParametros : ID guardarIDPila pos color checarDibujar '''	
	pass
#Crea el cuadruplo de dibujar, con su operador 19, el id de la figura que se quiere dibujar, las 
#posiciones donde se quiere dibujar y el color.
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
		cuadr = Cuadruplo(signo,ids,(posx,posy),col)
		listaCuadruplos.append(cuadr)
		pilaOperandos.pop()
		pilaOperandos.pop()
	
		print "SE GUARDO EL CUADRUPLO DE DIBUJAR"
#Regla de sintaxis correspondiente a dibujar una figura
def p_escritura(p):
	''' escritura : DIBUJAR guardarToken "("  guardarParametros ")" ";"
				  |  mueve
				  | desplegar '''
	pass
#Regla de sintaxis para mover la tortuja hacia diferentes lugares
def p_desplegar(p):
	''' desplegar : MOSTRAR guardarToken ID guardarIDPila ";" checarImpresion '''
	pass
#Regla de sintaxis que maneja los colores que se ingresen asignandoles su id de operador
def p_color(p):
	''' color : AMARILLO
			  | VERDE
			  | ROJO
			  | AZUL
			  | ROSA
			  | MORADO '''
	if p[1] == "amarillo":
		pilaOperandos.append(20)
	elif p[1] == "verde":
		pilaOperandos.append(21)
	elif p[1] == "rojo":
		pilaOperandos.append(22)
	elif p[1] == "azul":
		pilaOperandos.append(23)
	elif p[1] == "rosa":
		pilaOperandos.append(34)
	elif p[1] == "morado":
		pilaOperandos.append(35)
	pass
#Regla de sintaxis que maneja las condiciones
def p_condicion(p):
	''' condicion : IF "(" expresion ")" checarIF bloqueCond finPilaSaltos
				  | IF "(" expresion ")" checarIF bloqueCond checarElse bloqueCond finPilaSaltos'''
	pass
#Regla de sintaxis correspondiente al bloque de una funcion
def p_bloqueCond(p):
	'''bloqueCond : "{" estatuto regresaCond "}" 
				  |  "{" regresaCond "}" 
				  | "{"  "}" '''
	print("BLOQUE CONDICIONALES")
	pass
#Regla para generar el retorno de una funcion
def p_regresaCond(p):
	''' regresaCond :  RETURN expresion generarCuadRetorno
					| empty'''
	pass
#Regla de sintaxis en la cual se checa el if de una expresion
def p_checarIF(p):
	'''checarIF : '''
	print "Entre a checar IF"
	global pilaOperandos
	global pilaSaltos
	global pilaOperadores
	global pilaOperandosDirMem
	aux = pilaOperandos.pop()
	if aux != 8: 
		print "Error semantico en condicion IF"
		sys.exit()
	else:
		lenCuadruplos = len(listaCuadruplos)
		pilaSaltos.append(lenCuadruplos)
		print pilaOperandos
		temporal = pilaOperandosDirMem.pop()
		cuadr = Cuadruplo(16,temporal,-1,0)
		print "Guarde cuadruplo IF"
		listaCuadruplos.append(cuadr)
		print pilaOperandos
		print pilaOperadores

	pass
#Regla de sintaxis que genera el cuadruplo correspondiente al goto del if, y rellena el gotofalso
def p_checarElse(p):
	'''checarElse : ELSE '''
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
#Regla para manejar los saltos de gotos
def p_finPilaSaltos(p):
	'''finPilaSaltos : '''
	print "Entre fin pila saltos", pilaSaltos
	salto = pilaSaltos.pop()
	lenCuadruplos = len(listaCuadruplos)
	listaCuadruplos[salto].temporal = lenCuadruplos
	pass
#Regla para manejar las expresiones y operadores logicos
def p_expresion(p):
	'''expresion :  exp operacionLogica checaoperador6
				 | exp '''
	pass
#Manejo de los operadores logicos, asignandoles su numero identificador
def p_push_logica(p):
	'''push_logica : 	  ">" 
						| "<" 
				 		| MENORIGUAL  
				 		| MAYORIGUAL 
				 	   	| IGUALIGUAL  
				 		| DIFERENTE 
						| "|"
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
	elif p[1] == "|":
		pilaOperadores.append(12)
	elif p[1] == "&&":
		pilaOperadores.append(13)
	pass
#Regla auxiliar para manejar las operaciones logicas con mas expresiones
def p_operacionLogica(p):
	'''operacionLogica : push_logica exp
						 | '''
	pass
#Regla que verifica que las operaciones logicas que se esten manejando sean las correctas y se crea 
#el cuadruplo
def p_checaoperador6(p):
	'''checaoperador6 : '''
	global pilaOperadores
	global pilaOperandos
	global diccionarioMemoria
	global pilaOperandosDirMem
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
			print("Resultado: ", resultado)
			#meter a pila el temporal 
			if resultado == -1:
				print "ERROR: Operacion invalida, tipos no compatibles"
				sys.exit()
			else:
				print("SE CHECO EL CUADRUPLO Y ES CORRECTO", operando2, operando1, operadorActual)
				valormem = var[str(resultado)]
				agregarVar = TVar('temp', resultado, valormem,0,0)
				diccionarioMemoria['3'][str(resultado)] = valormem + 1
				listaFunciones[posicion].arrVar.append(agregarVar)
				pilaOperandosDirMem.append(valormem)
				resultadoT = pilaOperandosDirMem.pop()
				operando2C = pilaOperandosDirMem.pop()
				operando1C = pilaOperandosDirMem.pop()
				cuadr = Cuadruplo(operadorActual, operando1C,operando2C,resultadoT)
				listaCuadruplos.append(cuadr)
				pilaOperandos.append(resultado)
				pilaOperandosDirMem.append(resultadoT)
				print "asdasd ", pilaOperandos, " ", resultadoT

	pass
#Regla que maneja los terminos y manda a checar operador de + y -
def p_exp(p):
	'''exp : termino  checaroperador4'''
	global pilaOperandosDirMem
	print pilaOperandosDirMem
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
#Regla de sintaxis para verificar que la operacion que se quiere hacer sea valida y genera el cuadruplo
def p_checaroperador4(p):
	'''checaroperador4 : signo
					   | '''
	global pilaOperadores
	global pilaOperandos
	global diccionarioMemoria
	opr = len(pilaOperadores)
	print "Entra checaroperador4"
	if(opr != 0):
		if((pilaOperadores[opr-1] == 1) | (pilaOperadores[opr-1] == 2)):

			operando2 = pilaOperandos.pop()
			operando1 = pilaOperandos.pop()
			operadorActual = pilaOperadores.pop()
			resultado = cuboSemantico[operando1][operando2][operadorActual]
			posicion = busquedaLista()
			var = diccionarioMemoria['3']
			valormem = var[str(resultado)]
			agregarVar = TVar('temp', resultado, valormem,0,0)
			diccionarioMemoria['3'][str(resultado)] = valormem + 1
			listaFunciones[posicion].arrVar.append(agregarVar)
			pilaOperandosDirMem.append(valormem)
			print("Resultado: ", resultado)
			#meter a pila el temporal 
			if resultado == -1:
				print "ERROR: Operacion invalida, tipos no compatibles"
				sys.exit()
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
#Funcion auxiliar para manejar +- y exp
def p_signo(p):
	'''signo : push_pm exp
			 | '''
#Regla que maneja los operadores +- asigandoles su identificador y metiendolos a la pila de operadores
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
#Regla que maneja factor y checaroperador5 para las operaciones *-
def p_termino(p):
	'''termino : factor checaroperador5'''
	print ("Entre Termino ", p[1])
	pass
#Funcion para verificar que la operacion que se quiere hacer sea valida y genera el cuadruplo
def p_checaroperador5(p):
	'''checaroperador5 : masop
					   | '''
	global pilaOperadores
	global pilaOperandos
	global diccionarioMemoria
	opr = len(pilaOperadores)
	print "Entre a checaroperador5"	
	if(opr != 0):
		print("pila operadores",pilaOperadores[opr-1] )
		if((pilaOperadores[opr-1] == 3) | (pilaOperadores[opr-1] == 4)):
			operando2 = pilaOperandos.pop()
			operando1 = pilaOperandos.pop()
			operadorActual = pilaOperadores.pop()
			resultado = cuboSemantico[operando1][operando2][operadorActual]
			posicion = busquedaLista()
			var = diccionarioMemoria['3']
			print("resultado checaroperador5", resultado)
			#meter a pila el temporal 
			if resultado == -1:
				print "ERROR: Operacion invalida, tipos no compatibles"
				sys.exit()
			else:
				print("SE CHECO EL CUADRUPLO Y ES CORRECTO", operando2, operando1, operadorActual)
				valormem = var[str(resultado)]
				agregarVar = TVar('temp', resultado, valormem,0,0)
				diccionarioMemoria['3'][str(resultado)] = valormem + 1
				listaFunciones[posicion].arrVar.append(agregarVar)
				pilaOperandosDirMem.append(valormem)
				resultadoT = pilaOperandosDirMem.pop()
				operando2C = pilaOperandosDirMem.pop()
				operando1C = pilaOperandosDirMem.pop()
				pilaOperandosDirMem.append(resultadoT)
				cuadr = Cuadruplo(operadorActual, operando1C,operando2C,resultadoT)
				listaCuadruplos.append(cuadr)
				pilaOperandos.append(resultado)
	pass
#Funcion auxiliar para manejar *- y terminos
def p_masop(p):
	'''masop : push_td termino
			| '''
#Funcion que maneja */ asignandoles su operador y metiendolo a la pila
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
#Funcion que maneja expresion y variables constantes en una operacion
def p_factor(p):
	'''factor : fondoFalso expresion finFondoFalso
			  | varcte '''
	print "Entre a Factor"
	pass
#Funcion la cual maneja las posiciones en dibujar
def p_pos(p):
	''' pos : "(" expresion "," expresion ")" '''
	pass
#Regla de sintaxis para los whiles
def p_whiles(p):
	''' whiles : WHILE checarWhile "(" expresion ")" checarContenido bloqueCond finPilaSaltosWhile '''
	pass
#Regla que maneja los saltos de whiles
def p_checarWhile(p):
	''' checarWhile : '''
	global pilaSaltos
	global listaCuadruplos
	lenCuadruplos = len(listaCuadruplos)
	pilaSaltos.append(lenCuadruplos)
	pass
#Regla de sintaxis que verifica que el while este correcto y genera el cuadruplo goto falso
def p_checarContenido(p):
	''' checarContenido : '''
	global pilaSaltos
	global listaCuadruplos
	global pilaOperandos
	aux = pilaOperandos.pop()
	if aux != 8:
		print "Error en while"
		sys.exit()
	else:
		resultado = aux
		temp = pilaOperandosDirMem.pop()
		#GOTO FALSO RESULTADO _____
		cuadr = Cuadruplo(16,temp, -1,0)
		listaCuadruplos.append(cuadr)
		pilaSaltos.append(len(listaCuadruplos) - 1)
		print "Se guardo GOTO FALSO WHILE: ", cuadr.operador, cuadr.temporal
	pass
#Regla que maneja la pila de saltos de while
def p_finPilaSaltosWhile(p):
	'''finPilaSaltosWhile : '''
	global pilaSaltos
	global listaCuadruplos
	saltos = pilaSaltos.pop()
	saltos2 = pilaSaltos.pop()
	cuadr = Cuadruplo(17,-1,-1,saltos2)
	listaCuadruplos.append(cuadr)
	lenCuadruplos = len(listaCuadruplos)
	listaCuadruplos[saltos].temporal = lenCuadruplos
	print "Se guardo GOTO RETORNO: ", cuadr.operador, cuadr.temporal
	pass
#Regla de sintaxis que maneja las variables ingresadas
def p_varcte(p):
	''' varcte : recibe_ID opcionAsignacion
			   | recibe_CTF 
			   | recibe_CTI  
			   | recibe_TRUE 
			   | recibe_FALSE 
			   | funcs
			   '''
	pass
#Regla que maneja los ID que recibe, metiendolos a la pila de operandos y en caso de ser dimensionada 
#asignarle a la variable renArreglo y colArreglo el valor de los renglones y columnas de la variable 
#dimensionada para usarlas en el manejo de acceso de una variable dimensionada
def p_recibe_ID(p):
	''' recibe_ID : ID '''
	global renArreglo
	global colArreglo
	global listaFunciones
	global pilaOperandosDirMem
	global idActual

	print("VARCTE: ", p[1])
	pos = busquedaLista()
	print("Guardar: ", p[1])
	print pilaOperandosDirMem
	pos2 = busquedaVar(p[1])
	pos3 = busquedaVarParam(p[1])
	pos4 = busquedaVarGlobal(p[1])
	
	if(pos2 != -1):
		var = listaFunciones[pos].arrVar[pos2].tipo
		print "renArreglo = ", renArreglo
		if listaFunciones[pos].arrVar[pos2].ren != 0 or listaFunciones[pos].arrVar[pos2].col != 0:
			idActual = p[1]
			renArreglo = listaFunciones[pos].arrVar[pos2].ren
			colArreglo = listaFunciones[pos].arrVar[pos2].col
		direc = listaFunciones[pos].arrVar[pos2].direcmem
		pilaOperandosDirMem.append(direc)
		pilaOperandos.append(var)
	elif(pos3 != -1):
		var = listaFunciones[pos].arrParam[pos3].tipo
		print "colArreglo = ", colArreglo
		renArreglo = listaFunciones[pos].arrParam[pos2].ren
		colArreglo = listaFunciones[pos].arrParam[pos2].col
		if listaFunciones[pos].arrVar[pos2].ren != 0 or listaFunciones[pos].arrVar[pos2].col != 0:
			idActual = p[1]
			renArreglo = listaFunciones[pos].arrVar[pos2].ren
			colArreglo = listaFunciones[pos].arrVar[pos2].col
		direc = listaFunciones[pos].arrParam[pos3].direcmem
		pilaOperandosDirMem.append(direc)
		pilaOperandos.append(var)
	elif(pos4 != -1):
		direc = diccionarioVarGlobal[p[1]]
		pilaOperandosDirMem.append(direc)
	else:
		print "ERROR: NO SE ENCUENTRA EL ID QUE QUIERES USAR"
		sys.exit()
	pass
#Regla de sintaxis que maneja las variables flotantes metiendolas a la pilaOperandosDirMem y asignarle 
#memoria
def p_recibe_CTF(p):
	''' recibe_CTF : CTF '''
	print("VARCTE: ", p[1])
	global diccionarioMemoria
	global diccConstantes
	posicion = busquedaLista()
	var = diccionarioMemoria['4']
	valormem = var[str(7)]
	agregarVar = TVar(p[1],7, valormem,0,0)
	diccionarioMemoria['4'][str(7)] = valormem + 1
	listaFunciones[posicion].arrVar.append(agregarVar)
	diccConstantes[valormem] = p[1]
	pilaOperandosDirMem.append(valormem)
	pilaOperandos.append(7)
	pass
#Regla que maneja las variables constantes y asigna memoria
def p_recibe_CTI(p):
	''' recibe_CTI : CTI 
					| "-" CTI'''
	print("VARCTE: ", p[1])
	global diccionarioMemoria
	global diccConstantes
	global pilaOperandos
	global pilaOperandosDirMem
	print pilaOperadores
	if(p[1] == "-"):
		aux = -p[2]
	else:
		aux = p[1]
	posicion = busquedaLista()
	var = diccionarioMemoria['4']
	valormem = var[str(1)]
	agregarVar = TVar(aux,1, valormem,0,0)
	diccionarioMemoria['4'][str(1)] = valormem + 1
	listaFunciones[posicion].arrVar.append(agregarVar)
	diccConstantes[valormem] = aux
	pilaOperandosDirMem.append(valormem)
	pilaOperandos.append(1)
	print pilaOperandosDirMem
	pass
#Regla que maneja true 
def p_recibe_TRUE(p):
	''' recibe_TRUE : TRUE '''
	print("VARCTE: ", p[1])
 	global diccionarioMemoria
	posicion = busquedaLista()
	var = diccionarioMemoria['4']
	valormem = var[str(8)]
	agregarVar = TVar(p[1],8, valormem,0,0)
	diccionarioMemoria['4'][str(8)] = valormem + 1
	listaFunciones[posicion].arrVar.append(agregarVar)
	diccConstantes[valormem] = p[1]
	pilaOperandosDirMem.append(valormem)
	pilaOperandos.append(8)
	pass
#Regla que maneja false
def p_recibe_FALSE(p):
	''' recibe_FALSE : FALSE '''
	print("VARCTE: ", p[1])
	print("VARCTE: ", p[1])
 	global diccionarioMemoria
	global diccionarioMemoria
	posicion = busquedaLista()
	var = diccionarioMemoria['4']
	valormem = var[str(8)]
	agregarVar = TVar(p[1],8, valormem)
	diccionarioMemoria['4'][str(8)] = valormem + 1
	listaFunciones[posicion].arrVar.append(agregarVar)
	diccConstantes[valormem] = p[1]
	pilaOperandosDirMem.append(valormem)
	pilaOperandos.append(8)
	pass

#Regla que maneja los tipos de datos que se pueden declarar
def p_tipo(p):
	''' tipo : ENTERO 
			 | DECIMAL 
			 | BOOL
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
		tipoActual = 3
	elif(p[1] == "circulo"):
		tipoActual = 4
	elif(p[1] == "linea"):
		tipoActual = 5
	elif(p[1] == "estrella"):
		tipoActual = 6
	elif(p[1] == "bool"):
		tipoActual = 8
	pass
#Regla de sintaxis que maneja la opcion de mover a la tortuga.
def p_mueve(p):
	''' mueve : MUEVE guardarToken opcionMue '''
	pass
#Regla auxiliar con los componentes de la regla mover
def p_opcionMue(p):
	''' opcionMue : direccion recibe_CTI checarMover ";" '''
	pass
#Funcion que maneja las direcciones en las que se puede mover asignandoles su operador y 
#metiendolos a la pila
def p_direccion(p):
	''' direccion : IZQUIERDA
				| DERECHA
				| ARRIBA
				| ABAJO '''
	global pilaOperandos
	if p[1] == "izquierda":
		pilaOperandos.append(25)
		print pilaOperandos
	elif p[1] == "derecha":
		pilaOperandos.append(26)
	elif p[1] == "arriba":
		pilaOperandos.append(27)
	elif p[1] == "abajo":
		pilaOperandos.append(28)
	pass
#Funcion que crea el cuadruplo de mover
def p_checarMover(p):
	''' checarMover : '''
	global pilaOperadores
	global pilaOperandos
	global listaCuadruplos
	signo = pilaOperadores.pop()
	if signo == 24:
		pilaOperandos.pop()
		cant = pilaOperandosDirMem.pop()
		dirc = pilaOperandos.pop()
		cuadr = Cuadruplo(signo, 1, dirc, cant)
		listaCuadruplos.append(cuadr)
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

# file = open("prueba3.txt", "r")
# yacc.parse(file.read())
# file.close()
def run(filename):
	print filename
	file = open(filename, "r")
	yacc.parse(file.read())
	file.close()