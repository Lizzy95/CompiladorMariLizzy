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
    'else': 'ELSE',
    'dibujar' : 'DIBUJAR',
    'mueve' : 'MUEVE',
    'derecha' : 'DERECHA',
    'izquierda' : 'IZQUIERDA',
    'mostrar' : 'MOSTRAR',
    'arriba' : 'ARRIBA',
    'abajo' : 'ABAJO',
    'return' : 'RETURN',
    'bool' : 'BOOL', #9
    'func' : 'FUNC',
    'amarillo' : 'AMARILLO',
    'verde' : 'VERDE',
    'rojo' : 'ROJO',
    'azul' : 'AZUL',
    'rosa' : 'ROSA',
    'morado' : 'MORADO',
    'fin' : 'FIN',

}
#reserved = {'IF', 'ELSE', 'VAR', 'PRINT', 'INT', 'FLOAT', 'PROGRAM'}

# Lista de los nombres de tokens   
tokens = ['TRUE','FALSE','IF','ID','WHILE', 'CTI', 'CTF', 'MENORIGUAL', 'MAYORIGUAL', 'IGUALIGUAL', 
'DIFERENTE', 'COAND', 'COOR',] + list(reserved.values())

#Declaracion de simbolos especiales mediatne literales
literals = "+-*/.,:;(){}[]<>=|"

t_MENORIGUAL = "<="

t_MAYORIGUAL = ">="

t_IGUALIGUAL = "=="

t_DIFERENTE = "!="

# t_COOR = "||"

t_COAND = "&&"

# t_TRUE = "TRUE"

# t_FALSE = "FALSE"
#Checa true
def t_TRUE(t):
    r'true'
    t.type = reserved.get(t.value, 'TRUE')
    return t
#Regla que checa el false
def t_FALSE(t):
    r'false'
    t.type = reserved.get(t.value, 'FALSE')
    return t
#Regla que checa el IF
def t_IF(t):
    r'if'
    t.type = reserved.get(t.value, 'IF')
    return t
#Regla que checa el while
def t_WHILE(t):
    r'while'
    t.type = reserved.get(t.value, 'WHILE')
    return t
#Regla que checa el ID
def t_ID(t):
    r'[a-zA-Z].[a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')   
    return t
#Regla que checa las CTF
def t_CTF(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t
#Regla que checa las CTI
def t_CTI(t):
    r'[0-9]+'
    t.value = int(t.value)
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
