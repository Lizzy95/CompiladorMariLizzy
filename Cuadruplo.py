#Clase que maneja como atributos los componentes de un cruadruplo. Los objetos se usan en archivos 
#YACC y MaquinaVirtual para el procesamiento del programa en ejecución
class Cuadruplo:
	def __init__(self, operador, operando1, operando2, temporal ):
		self.operando1 = operando1
		self.operando2 = operando2
		self.operador = operador
		self.temporal = temporal