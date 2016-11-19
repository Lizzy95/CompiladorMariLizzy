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
# Code to add widgets will go here...
def compilar():
	#os.system('python yacc.py')
	global nombrearchivo
	print  nombrearchivo
	yacc.run(archivo2)

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
	yacc.run(archivo2)

def ejecutar():
	os.system('python MaquinaVirtual.py')

def borrarpantallatexto():
	T.delete(1.0,END)
	
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

cargarprograma = Button(root, text = "Cargar programa", command = cargar)
cargarprograma.pack()

guardarprograma = Button(root, text = "Guardar programa", command = guardar)
guardarprograma.pack()

correrprograma = Button(root, text = "Compilar programa", command = compilar)
correrprograma.pack()

ejecutarprograma = Button(root, text = "Ejecutar programa", command = ejecutar)
ejecutarprograma.pack()

borrarpantalla = Button(root, text = "Borrar texto de pantalla", command = borrarpantallatexto)
borrarpantalla.pack()

S = Scrollbar(root)
T = Text(root, height = 33, width = 100, bg = '#c5c3d6')
T.pack()

root.mainloop()