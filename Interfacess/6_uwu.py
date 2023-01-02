from cProfile import label
from cgitb import text
from tkinter import * 
from datetime import datetime
import time
from tkinter import font

import sympy as sym
import numpy as np

from tabulate import tabulate
# Proyecto de bissciom


def obtener_hora_actual():  # obtiene la hora 
    return datetime.now().strftime("%H:%M:%S")

root = Tk()
root.title("Biseccion")
root.geometry("950x550") 

frame1 = Frame()
frame1.pack(fill = "x")
frame1.config(bg= "pink")
frame1.config(width="100", height="40")



funciondia = time.strftime('%d-%m-%y')
funciontiempo = time.strftime('%H:%M:%S')

tiempo = Label(frame1,text=(f"Hora: {funciontiempo}   Fecha: {funciondia} "),font=10)
tiempo.pack(padx=0,pady=10)
tiempo.config(bg="pink")


def accionBoton1():

    ventana = Toplevel()
    ventana.title("Programa 1")
    ventana.geometry("950x550")

    label3 = Label(ventana,text="Ingresa la ecuacion: ",bg="pink",font=10)
    label3.grid(row=0,column=0,padx=10,pady=10,ipadx=10,ipady=10)

    label4 = Entry(ventana,bg="pink",font=10)
    label4.grid(row = 0, column=1,ipadx=10,ipady=10)

    def accionBoton4():
        x= sym.Symbol('x')
        la = str(label4.get())
        ecuacion = eval(la)
        label6.delete(0,"end")
        label6.insert(0,ecuacion)

    boton4 = Button(ventana,text="Insertar",bg="Green",fg="white",command=accionBoton4,cursor="hand2")
    boton4.grid(row=0,column=3,padx=10,ipady=10)

    label5 = Label(ventana,text="tu ecuacion es: ",font=10)
    label5.grid(row=2, column=0,padx=10,ipady=10)

    label6 = Entry(ventana,font=10)
    label6.grid(row = 2, column=1,ipadx=10,ipady=10)

    label7 = Label(ventana,text="Ingresa el limite menor: ",font=10)
    label7.grid(row=3, column=0,padx=10,ipady=10)
    
    label8 = Entry(ventana,font=10)
    label8.grid(row = 3, column=1,ipadx=10,ipady=10)

    label9 = Label(ventana,text="Ingresa el limite mayor: ",font=10)
    label9.grid(row=4, column=0,padx=10,ipady=10)
    
    label20 = Entry(ventana,font=10)
    label20.grid(row = 4, column=1,ipadx=10,ipady=10)

    label21 = Label(ventana,text="Ingresa el intervalo: ",font=10)
    label21.grid(row=5, column=0,padx=10,ipady=10)

    label22 = Entry(ventana,font=10)
    label22.grid(row = 5, column=1,ipadx=10,ipady=10)

    
    #----------------------------------------------------#
    #convierto a floats los strings de los input y lo almaceno en una variable con su name correspondiente
    x = sym.Symbol('x')
    la = str(label4.get())
    ecuacion = eval(la)
    lmmenor = float(label7.get())
    lmmayor = float(label20.get())
    incrementos = float(label22.get())
    lista_rangos = np.arange(lmmenor, lmmayor+.5, incrementos)
    z = []
    for n in lista_rangos:
        k = ecuacion.subs(x, n)
        k = round(k, 4)
        z.append([n, k])
    label25 = Label(ventana,text =tabulate(z, headers=["  x  ", " f(x) "]),bg="pink",font=2)
    label25.grid(row=6,column=0,padx=15,pady=15)
    

    #-----------------------------------------------------------#

button1 = Button(root,text="Biseccion",bg="pink",font=10,command =accionBoton1)
button1.config(cursor="hand2")
button1.pack(ipadx=10,ipady=10,expand=True) #tamaño del boton

frame2 = Frame()
#frame2.pack(expand= True, fill= "x" ,anchor=S,side=LEFT)
frame2.pack(expand= True ,anchor=S,side=RIGHT,fill= "x")
frame2.config(bg="pink")
frame2.config(width="100", height="40")

button2 = Button(root,text="<-",bg="green",font=10)
button2.config(cursor= "hand2")
button2.pack(ipadx=5,ipady=5,anchor=W,side=LEFT)


button3 = Button(root,text="Datos",bg="purple",font=10)
button3.config(cursor= "hand2")
button3.pack(padx = 10, ipadx=5,ipady=5,anchor=W,side=LEFT)

root.mainloop()