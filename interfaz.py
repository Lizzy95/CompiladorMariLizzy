#!/usr/bin/python
from turtle import *
import ply.yacc as yacc
from Tkinter import *
import os
root = Tk()
root.geometry("600x700")
root.configure(bg = '#ffc0cb')
# Code to add widgets will go here...
def compilar():
	os.system('python yacc.py')

def guardar():
    text = T.get("1.0",'end-1c')
    with open("prueba.txt", "w") as f:
        f.writelines(text)

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