import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

# BNF
def p_programa(p):
	'''programa : INICIO bloque  FIN 
	  			| INICIO FIN
	  			| funcion programa '''
	print("SE TERMINO EL PROGRAMA PATIO CON EXITO!")
	pass

def p_bloque(p):
	'''bloque : "{" vars estatuto "}"
			  | "{" vars "}"
			  | "{" "}"'''
	print("BLOQUE")
	pass

def p_vars(p):
	'''vars : tipo ID ";" masTipos
		| tipo ID arreglo  ";" masTipos
		| tipo listaIDS ";" masTipos'''
	print("VARS: Estructura basica")
	pass


def p_masTipos(p):
	'''masTipos : vars 
				| empty '''
	pass

def p_listaIDS(p):
	''' listaIDS : ID masIDS '''
	pass

def p_masIDS(p):
	'''masIDS : "," ID 
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
	''' funcion : FUNC tipo ID "(" param ")" bloquefunc '''
	pass

def p_param(p):
	''' param : tipo listapaID '''
	pass

def p_listapaID(p):
	''' listapaID : ID maspaID maspaTip '''
	pass

def p_maspaID(p):
	''' maspaID : "," ID
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
				 | exp COAND exp '''
	pass

def p_exp(p):
	''' exp : "(" expresion ")" 
			| "(" varcte  operacion ")" 
			| varcte operacion 
			| varcte
			| empty '''
	pass

def p_operacion(p):
	'''operacion : termino 
		   		 | termino signo '''
	pass

def p_signo(p):
	'''signo : "+" exp 
			| "-" exp '''
	pass

def p_termino(p):
	'''termino : factor 
			   | factor masop '''
	pass

def p_masop(p):
	'''masop : "*" termino 
 			 | "/" termino''' 
 	pass

def p_factor(p):
	'''factor : "(" expresion ")" 
			  | varcte 
	    	  | "+" varcte 
			  | "-" varcte '''
	pass

def p_for(p):
	'''fors : FOR "(" asignacion expresion ";" asignacion ")" bloque '''
	pass

def p_pos(p):
	''' pos : "(" varcte "," varcte ")" '''
	pass

def p_whiles(p):
	''' whiles : WHILE "(" expresion ")" bloque '''
	pass

def p_varcte(p):
	''' varcte : ID 
			   | CTF 
			   | CTI 
			   | CTS 
			   | TRUE 
			   | FALSE '''
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
    print("VACIO")
    pass

def p_error(p):
    print("Syntax error")
    
import ply.yacc as yacc
parser = yacc.yacc()
#yacc.yacc()
file = open("prueba.txt", "r")
yacc.parse(file.read())
file.close()
