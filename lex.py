#------------------------------------------------------------
# lex.py
#
# tokenizer
# De esta pagina http://www.juanjoconti.com.ar/2007/11/02/minilisp-un-ejemplo-de-ply/
# se obtuvo el metodo t_newline y t_error
# ------------------------------------------------------------

import ply.lex as lex


# Palabras reservadas
reserved = {
#    'if' : 'IF',
    'inicio': 'INICIO', #0
    'entero' : 'ENTERO', #1 
    'decimal' : 'DECIMAL', #2
    'cuadrado' : 'CUADRADO', #3
    'rectangulo' : 'RECTANGULO', #4
    'circulo' : 'CIRCULO', #5
    'linea' : 'LINEA', #6
    'estrella' : 'ESTRELLA', #7
    'leer' : 'LEER', 
    'else': 'ELSE',
    'dibujar' : 'DIBUJAR',
    'mueve' : 'MUEVE',
    'derecha' : 'DERECHA',
    'izquierda' : 'IZQUIERDA',
    'arriba' : 'ARRIBA',
    'abajo' : 'ABAJO',
    'void' : 'VOID', #8
    'return' : 'RETURN',
    'bool' : 'BOOL', #9
    'func' : 'FUNC',
    'for' : 'FOR',
    'amarillo' : 'AMARILLO',
    'verde' : 'VERDE',
    'rojo' : 'ROJO',
    'azul' : 'AZUL',
    'fin' : 'FIN',

}
#reserved = {'IF', 'ELSE', 'VAR', 'PRINT', 'INT', 'FLOAT', 'PROGRAM'}

# Lista de los nombres de tokens   
tokens = ['IF','ID','WHILE', 'CTI', 'CTF', 'CTS', 'MENORIGUAL', 'MAYORIGUAL', 'IGUALIGUAL', 'DIFERENTE', 'COAND', 'COOR', 'TRUE', 'FALSE',] + list(reserved.values())

#Declaracion de simbolos especiales mediatne literales
literals = ['.', ',', ':', ';', '(', ')', '{', '}', '[', ']', '+', '-', '*', '/', '<', '>', '=']

t_MENORIGUAL = "<="

t_MAYORIGUAL = ">="

t_IGUALIGUAL = "=="

t_DIFERENTE = "!="

t_COOR = "OR"

t_COAND = "&&"

t_TRUE = "TRUE"

t_FALSE = "FALSE"


def t_IF(t):
    r'if'
    t.type = reserved.get(t.value, 'IF')
    return t

def t_WHILE(t):
    r'while'
    t.type = reserved.get(t.value, 'WHILE')
    return t

def t_ID(t):
    r'[a-zA-Z].[a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CTF(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CTI(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CTS(t):
    r'[\"a-zA-Z0-9]+\"'
    t.type = reserved.get(t.value, 'STRING')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# String para ignorar los espacios
t_ignore  = ' \t'

# Manejar errores
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Construye el lexico
lex.lex()

if __name__ == '__main__':
    lex.runmain()
