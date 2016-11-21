#!/usr/bin/python
from turtle import *
import ply.yacc as yacc
import yacc
from Tkinter import *
import Tkinter,tkFileDialog
import os
nombrearchivo = ""
archivo2 = ""
root = Tk()
root.wm_title("LiMa")
root.geometry("600x700")
root.configure(bg = '#ffc0cb')

#Funcion para compilar el programa
def compilar():
	#os.system('python yacc.py')
	global nombrearchivo
	print  nombrearchivo
	yacc.run(archivo2)
#Funcion que guarda lo ingresado en el area de texto en el archivo de texto que indique el usuario.
def guardar():
	global nombrearchivo
	global archivo2
	file = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
	nombrearchivo = file.name
	(f1, archivo2) = os.path.split(nombrearchivo)
	print archivo2
	texto = T.get("1.0",'end-1c')
	with open(archivo2, "w") as f:	
		f.writelines(texto)
#Funcion mediante la cual se ejecuta la Maquina virtual
def ejecutar():
	os.system('python MaquinaVirtual.py')
#Funcion que borra la pantalla de texto del programa 
def borrarpantallatexto():
	T.delete(1.0,END)
#Funcion que carga el programa de un archivo de texto proporcionada por el usuario
def cargar():
	global archivo2
	nombrearchivo = tkFileDialog.askopenfile()
	(f1, archivo2) = os.path.split(nombrearchivo.name)
	print archivo2
	if nombrearchivo:
		T.delete(1.0,END)
		with open(nombrearchivo.name) as archivoabierto:
			for linea in archivoabierto:
				T.insert(END, linea)
#Crea el boton de cargar programa y se asocia a la funcion de cargar.
cargarprograma = Button(root, text = "Cargar programa", command = cargar)
cargarprograma.pack()
#Crea el boton de guardar programa y se asocia a la funcion de guardar.
guardarprograma = Button(root, text = "Guardar programa", command = guardar)
guardarprograma.pack()
#Crea el boton de correr programa y se asocia a la funcion de compilar.
correrprograma = Button(root, text = "Compilar programa", command = compilar)
correrprograma.pack()
#Crea el boton de ejecutar programa y se asocia a la funcion de ejecutar.
ejecutarprograma = Button(root, text = "Ejecutar programa", command = ejecutar)
ejecutarprograma.pack()
#Crea el boton de borrar pantalla y se asicia a la funcion de borrarpantallatexto
borrarpantalla = Button(root, text = "Borrar texto de pantalla", command = borrarpantallatexto)
borrarpantalla.pack()

S = Scrollbar(root)
T = Text(root, height = 33, width = 100, bg = '#c5c3d6')
T.pack()

root.mainloop()