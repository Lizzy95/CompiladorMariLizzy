#Clase que crea el cubo semantico para verificar las operaciones, asi mismo contine el identificador 
#que le corresponde a cada operador

#1 +
#2 -
#3 *
#4 /
#5 =
#6 >
#7 <
#8 >=
#9 <=
#10 ==
#11 !=
#12 |
#13 &&
#14 (
#15 )
#16 GOTOF
#17 GOTO 
#19 DIBUJAR
#20 AMARILLO
#21 VERDE
#22 ROJO
#23 AZUL
#24 MUEVE
#25 IZQUIERDA
#26 DERECHA
#27 ARRIBA
#28 ABAJO
#29 RETORNO
#30 ERA
#31 PARAM
#32 GOSUB
#33 VER
#34 rosa
#35 morado

#enteros
cuboSemantico = [[[-1 for k in range(14)] for j in range(9)] for i in range(9)]


#entero
cuboSemantico[1][1][1]= 1
cuboSemantico[1][1][2]= 1
cuboSemantico[1][1][3]= 1
cuboSemantico[1][1][4]= 1
cuboSemantico[1][1][5]= 1
cuboSemantico[1][1][6]= 8
cuboSemantico[1][1][7]= 8
cuboSemantico[1][1][8]= 8
cuboSemantico[1][1][9]= 8
cuboSemantico[1][1][10]= 8
cuboSemantico[1][1][11]= 8

cuboSemantico[1][7][1]= 7
cuboSemantico[1][7][2]= 7
cuboSemantico[1][7][3]= 7
cuboSemantico[1][7][5]= 7
cuboSemantico[1][7][6]= 8
cuboSemantico[1][7][7]= 8
cuboSemantico[1][7][8]= 8
cuboSemantico[1][7][9]= 8
cuboSemantico[1][7][10]= 8
cuboSemantico[1][7][11]= 8

#decimal
cuboSemantico[7][7][1]= 7
cuboSemantico[7][7][2]= 7
cuboSemantico[7][7][3]= 7
cuboSemantico[7][7][4]= 7
cuboSemantico[7][7][5]= 7
cuboSemantico[7][7][6]= 8
cuboSemantico[7][7][7]= 8
cuboSemantico[7][7][8]= 8
cuboSemantico[7][7][9]= 8
cuboSemantico[7][7][10]= 8
cuboSemantico[7][7][11]= 8

cuboSemantico[7][1][1]= 7
cuboSemantico[7][1][2]= 7
cuboSemantico[7][1][3]= 7
cuboSemantico[7][1][5]= 7
cuboSemantico[7][1][6]= 8
cuboSemantico[7][1][7]= 8
cuboSemantico[7][1][8]= 8
cuboSemantico[7][1][9]= 8
cuboSemantico[7][1][10]= 8
cuboSemantico[7][1][11]= 8

#bool
cuboSemantico[8][8][5]= 8
cuboSemantico[8][8][6]= 8
cuboSemantico[8][8][7]= 8
cuboSemantico[8][8][8]= 8
cuboSemantico[8][8][9]= 8
cuboSemantico[8][8][10]= 8
cuboSemantico[8][8][11]= 8
cuboSemantico[8][8][12]= 8
cuboSemantico[8][8][13]= 8





