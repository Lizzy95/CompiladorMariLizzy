#Esta clase se encarga de manejar la memoria de ejecucion, la cual esta compuesta de diferentes #arreglos correspondientes a
#las variables entero, cuadrado, rectangulo, circulo, linea, estrella, decimal, bool y sus #temporales. Asi como tambien el 
#arreglo de variables temporales de apuntadores. 
#Esta clase agrupa cada uno de estos arreglos en una lista la cual es la memoria.
#
class Memoria:
	def __init__(self, cuadrRetorno, arrEntero, arrCuadrado, arrRectangulo, arrCirculo, arrLinea, arrEstrella, arrDecimal, arrBool, arrEnteroTemp, arrCuadradoTemp, arrRectanguloTemp, arrCirculoTemp, arrLineaTemp, arrEstrellaTemp, arrDecimalTemp, arrBoolTemp,arrApuntTemp):
		self.arrEntero = []
		self.arrCuadrado = []
		self.arrRectangulo = []
		self.arrCirculo = []
		self.arrLinea = []
		self.arrEstrella = []
		self.arrDecimal = []
		self.arrBool = []
		self.arrEnteroTemp = []
		self.arrCuadradoTemp = []
		self.arrRectanguloTemp = []
		self.arrCirculoTemp = []
		self.arrLineaTemp = []
		self.arrEstrellaTemp = []
		self.arrDecimalTemp = []
		self.arrBoolTemp = []
		self.arrApuntTemp = []
		self.cuadrRetorno = cuadrRetorno
		self.listaMem = [arrEntero, arrCuadrado,arrRectangulo, arrCirculo, arrLinea, arrEstrella, arrDecimal, arrBool, arrEnteroTemp, arrCuadradoTemp,arrRectanguloTemp,arrCirculoTemp, arrLineaTemp,arrEstrellaTemp, arrDecimalTemp, arrBoolTemp, arrApuntTemp]
