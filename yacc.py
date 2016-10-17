import ply.yacc as yacc
from TFunc import TFunc
from TVar import TVar
from CuboSemantico import cuboSemantico
from diccionarioMemoria import diccionarioMemoria
# Get the token map from the lexer.  This is required.
from lex import tokens

listaFunciones = []
funcionActual = ""
tipoActual = 0
operando1 = ""
operando2 = ""
tipofuncMem = '1'
pilaOperadores = []
pilaOperandos = []
operadorActual = 0
resultado = -1
DEBUG = True

# BNF


def p_programa(p):
	'''programa : INICIO funcAgregarInicio bloque  FIN 
	  			| INICIO FIN
	  			| funcion programa '''
	print diccionarioMemoria['3']
	print("SE TERMINO EL PROGRAMA PATIO CON EXITO!")
	pass

def p_funcAgregarInicio(p):
	'''funcAgregarInicio : '''
	global funcionActual
	global listaFunciones
	global tipofuncMem
	tipofuncMem = '2'
	funcionActual = p[-1]
	objetoFuncion = TFunc(funcionActual, 0, {})
	listaFunciones.append(objetoFuncion)
	print("Se agrego la funcion a la tabla")



def p_bloque(p):
	'''bloque : "{" vars estatuto "}"
			  | "{" vars "}"
			  | "{" "}"'''
	print("BLOQUE")
	pass

def p_vars(p):
	'''vars : tipo ID guardarIDs ";" masTipos
		| tipo ID guardarIDs arreglo  ";" masTipos
		| tipo listaIDS ";" masTipos'''
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
	''' funcion : FUNC tipo ID  funcAgregar "(" param ")" bloquefunc '''
	pass

def p_funcAgregar(p):
	'''funcAgregar : '''
	global funcionActual
	global listaFunciones
	global tipoActual
	global tipofuncMem
	tipofuncMem = '2'
	funcionActual = p[-1]
	objetoFuncion = TFunc(p[-1], tipoActual, {})
	#checar si ya existe una funcion
	posicion = busquedaLista()
	if posicion != -1:
		print "FUNCION PREVIAMENTE DECLARADA"
	else:
		listaFunciones.append(objetoFuncion)

def p_param(p):
	''' param : tipo listapaID '''
	pass
	
def p_listapaID(p):
	''' listapaID : ID guardarIDs maspaID maspaTip '''
	pass

def busquedaLista():
	cont = 0
	global listaFunciones
	global funcionActual
	for elemento in listaFunciones:
		if elemento.nombre == funcionActual : 
			return cont
		cont += cont
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
					cont += cont
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
	#checar si ya existe una variable
	print("mi diccionario: ", diccionarioMemoria['2'])
	if (busquedaVar(p[-1]) != -1 ):
		print "SE DECLARO UNA VARIABLE PREVIAMENTE DECLARADA"
	else:
		posicion = busquedaLista()
		print("funcmen: ", tipofuncMem)
		var = diccionarioMemoria[tipofuncMem]
		valormem = var[str(tipoActual)]
		agregarVar = TVar(p[-1], tipoActual, valormem)
		var[str(tipoActual)] = valormem + 1
		listaFunciones[posicion].arrVar.append(agregarVar)
		print "Se guardo la variable en la tabla ", tipoActual


def p_maspaID(p):
	''' maspaID : "," ID guardarIDs
				| empty '''
	pass

def p_maspaTip(p):
	''' maspaTip : vars
				 | empty '''
	pass

def p_bloquefunc(p): 
	''' bloquefunc : "{" vars estatuto regresa "}" 
				   | "{" vars regresa "}" 
				   | "{" escritura regresa "}" 
				   | "{" "}" '''
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
				| fors estatutoAux '''
	pass
def p_estatutoAux(p):
	''' estatutoAux : estatuto
					| empty'''
	pass

def p_asignacion(p):
	''' asignacion : ID opcionAsignacion valorAsig ";"
				 | ID ";" '''
	pass

def p_opcionAsignacion(p):
	''' opcionAsignacion : "[" CTI "]"
						| "[" CTI "]" "[" CTI "]"
						| empty '''
	pass
def p_valorAsig(p):
	''' valorAsig : "=" exp
				  | empty'''
	pass

def p_lectura(p):
	''' lectura : LEER ID opcionesLectura ";" '''
	pass

def p_opcionesLectura(p):
	''' opcionesLectura : "[" CTI "]"
						| "[" CTI "]" "[" CTI "]"
						| empty '''
	pass

def p_escritura(p):
	''' escritura : DIBUJAR "(" ID pos color ")" ";"
				  |  mueve '''
	pass

def p_color(p):
	''' color : AMARILLO
			  | VERDE
			  | ROJO
			  | AZUL '''
	pass

def p_condicion(p):
	''' condicion : IF "(" expresion ")" bloque
				  | IF "(" expresion ")" bloque ELSE bloque '''
	pass

def p_expresion(p):
	'''expresion :  exp ">" exp 
				 | exp "<" exp 
				 | exp MENORIGUAL exp 
				 | exp MAYORIGUAL exp 
				 | exp IGUALIGUAL exp 
				 | exp DIFERENTE exp 
				 | exp COOR exp 
				 | exp COAND exp 
				 | exp '''
	pass

def p_exp(p):
	'''exp : termino checaroperador4 '''
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
			var[str(resultado)] = valormem + 1
			listaFunciones[posicion].arrVar.append(agregarVar)
			print("Resultado: ", resultado)
			#meter a pila el temporal 
			if resultado == -1:
				print "ERROR: Operacion invalida, tipos no compatibles"
			else:
				print("SE CHECO EL CUADRUPLO Y ES CORRECTO", operando2, operando1, operadorActual)
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
			var[str(resultado)] = valormem + 1
			listaFunciones[posicion].arrVar.append(agregarVar)
			print("resultado checaroperador5", resultado)
			#meter a pila el temporal 
			if resultado == -1:
				print "ERROR: Operacion invalida, tipos no compatibles"
			else:
				print("SE CHECO EL CUADRUPLO Y ES CORRECTO", operando2, operando1, operadorActual)
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

def p_for(p):
	'''fors : FOR fondoFalso asignacion expresion ";" asignacion finFondoFalso bloque '''
	pass

def p_pos(p):
	''' pos : "(" varcte "," varcte ")" '''
	pass

def p_whiles(p):
	''' whiles : WHILE "(" expresion ")" bloque '''
	pass

def p_varcte(p):
	''' varcte : recibe_ID 
			   | recibe_CTF 
			   | recibe_CTI 
			   | recibe_CTS 
			   | recibe_TRUE 
			   | recibe_FALSE '''
	pass

def p_recibe_ID(p):
	''' recibe_ID : ID '''
	print("VARCTE: ", p[1])
	pos = busquedaLista()
	print("Guardar: ", p[1])
	pos2 = busquedaVar(p[-1])
	if(pos2 != -1 ):
		var = listaFunciones[pos].arrVar[pos2].tipo
		pilaOperandos.append(var)
	else:
		print "ERROR: NO SE ENCUENTRA EL ID QUE QUIERES USAR"
	pass

def p_recibe_CTF(p):
	''' recibe_CTF : CTF '''
	print("VARCTE: ", p[1])
	pilaOperandos.append(7)
	pass

def p_recibe_CTI(p):
	''' recibe_CTI : CTI '''
	print("VARCTE: ", p[1])
	pilaOperandos.append(1)
	pass

def p_recibe_CTS(p):
	''' recibe_CTS : CTS '''
	print("VARCTE: ", p[1])
	pass

def p_recibe_TRUE(p):
	''' recibe_TRUE : TRUE '''
	print("VARCTE: ", p[1])
	pilaOperandos.append(8)
	pass

def p_recibe_FALSE(p):
	''' recibe_FALSE : FALSE '''
	print("VARCTE: ", p[1])
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
	''' mueve : MUEVE  opcionMue '''
	pass

def p_opcionMue(p):
	''' opcionMue : IZQUIERDA ID CTI ";" 
			   | DERECHA ID CTI ";" 
			   | ARRIBA ID CTI ";"
			   | ABAJO ID CTI ";"'''
	pass

def p_empty(p):
    'empty : '
    print("SALTO DE LINEA")
    pass

def p_error(p):
    print("Syntax error")
    
import ply.yacc as yacc
parser = yacc.yacc()
#yacc.yacc()
file = open("prueba.txt", "r")
yacc.parse(file.read())
file.close()
