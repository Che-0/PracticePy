from tkinter import *
import time

import numpy as np
root = Tk()
root.title("Programas")
root.geometry("950x550") 

frame1 = Frame()
frame1.pack(fill = "x")
frame1.config(bg= "pink")
frame1.config(width="100", height="40")

#variables que almacenan la fecha y hora
funciondia = time.strftime('%d-%m-%y')
funciontiempo = time.strftime('%H:%M:%S')

tiempo = Label(frame1,text=(f"Hora: {funciontiempo}   Fecha: {funciondia} "),font=10)
tiempo.pack(padx=0,pady=10)
tiempo.config(bg="pink")

frame2 = Frame(bg="pink")
frame2.config(width=60,height=40)
frame2.pack(padx=30,pady=40)  


#nueva ventana 
def comando1():
    ventana = Toplevel()
    ventana.title("Matrices")
    ventana.geometry("950x550")

    label1 = Label(ventana,text="combinacion de dos matrices triangulares",bg="lightpink")
    label1.grid(row = 0, columnspan=10 ,padx=60,ipadx=10,ipady=10)

    label2 = Label(ventana,text="Ingresa las filas que tiene la matriz",justify=LEFT)
    label2.grid(row=2,column=0,padx=10,pady=5)

    text1 = Entry(ventana) # filas
    text1.grid(row=2,column=1)

    label3 = Label(ventana,text="Ingresa la cantidad de columnas",justify=LEFT)
    label3.grid(row=3,column=0,padx=10,pady=5)

    text2 = Entry(ventana) #columnas
    text2.grid(row=3,column=1)

    def accion2():
        """Desactiva los botones y la celda de texto despues de 
        ser utilizados
        """
        text1.config(state=DISABLED)
        boton2.config(state=DISABLED)
        boton3.config(state=NORMAL)
    
    
    def accion3():
        """Desactiva el campo de texto dos y su correspondiente boton 

        """

        def accion4():
            c = int(contador.get()) #señala en que posicion de la matriz va 
            if c ==longitud:        #longitud de filas
                print("completado")

            elif c != longitud:   
                i = int(text3.get())
                matrizA.append(i)
                print(matrizA)
                c+=1
                contador.insert(0,c)
                


        text2.config(state=DISABLED)
        boton3.config(state=DISABLED)

        i = int(text1.get())
        longitud = i
        j = int(text2.get())
    
        label4 = Label(ventana,text="Ingresa los valores de la matriz",justify=LEFT)
        label4.grid(row= 8, column= 0,padx=10)
      
        text3 = Entry(ventana)
        text3.grid(row=9,column=1,padx=10)

        matrizA=[]
        contador = Entry(ventana)

        boton4 = Button(ventana,text="Insertar",bg="green",fg="white",command=accion4)
        boton4.grid(row=9,column=2,padx=10)
            
                

    boton2 = Button(ventana,text="✓",bg="green",fg="white",cursor="hand2",command=accion2)
    boton2.grid(row=2,column=2,padx=10,pady= 5, ipadx=5,ipady=2)

    boton3 = Button(ventana,text="✓",bg="green",fg="white",cursor="hand2",command=accion3,state=DISABLED)
    boton3.grid(row=3,column=2,padx=10,pady= 10, ipadx=5,ipady=2)

    
boton1 = Button(frame2,text="Matrices",bg="pink",command=comando1) #Nombre del boton 
boton1.config(cursor="hand2")
boton1.pack()

frame3 = Frame()
frame3.pack(expand= True ,anchor=S,side=RIGHT,fill= "x")
frame3.config(bg="pink")
frame3.config(width="100", height="40")

root.mainloop()