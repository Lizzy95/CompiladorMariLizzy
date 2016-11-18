#!/usr/bin/python
from turtle import *
import ply.yacc as yacc
import yacc
from Tkinter import *
import Tkinter,tkFileDialog
import os
filename = ""
f2 = ""
root = Tk()
root.wm_title("LiMa")
root.geometry("600x700")
root.configure(bg = '#ffc0cb')
# Code to add widgets will go here...
def compilar():
	#os.system('python yacc.py')
	global filename
	print filename
	yacc.run(f2)

def guardar():
	global filename
	global f2
	file = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
	filename = file.name
	(f1, f2) = os.path.split(filename)
	print f2
	text = T.get("1.0",'end-1c')
	with open(f2, "w") as f:	
		f.writelines(text)
	yacc.run(f2)

def ejecutar():
	os.system('python MaquinaVirtual.py')

def borrarpantallatexto():
	T.delete(1.0,END)
	

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