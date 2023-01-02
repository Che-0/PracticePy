from sys import builtin_module_names
from tkinter import *
from pathlib import Path
import os
os.chdir(Path("E:\python\Interfacess"))

root = Tk()

root.title("Huevos")


#En el primer argumento se pone si quieres que se pueda
#alterar el ancho y en el segundo el largo
#tambien funciona con 0 y 1
# 0 = False     1 = True
root.resizable(1,1)

#cambiar la imagen del programa
#actua con la direccion de la imagen
#de preferencia que este en el mismo directorio
# la imagen tiene que tener formato .ico
# Transformarla en linea 

#poner una imagen en la esquina
root.iconbitmap("e.ico")

#root.geometry("750x450") --- nel
#root.config(bg="white")

miFrame = Frame()
#El freame debe de estar enpaquetado en la raiz

miFrame.pack(side="left",anchor="n")
miFrame.config(bg ="red")
miFrame.config(width="650", height="350")

root.mainloop()
