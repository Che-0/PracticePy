from tkinter import*
import time
import numpy as np
#funcion para obtener el dia
def fecha():
    dia = time.strftime('%d-%m-%y')
    hora = time.strftime('%H:%M:%S')
    x = " " *10
    return "Fecha: " + dia + x + "Hora: " + hora

def programa1():

    #desactiva el boton
    def desactivar(x):
        x.config(state = DISABLED)

    #funcion boton2
    #Pasa los strings a enteros
    def enteros():
        desactivar(insertar)
        i = int(filas.get())  #filas
        newi = i
        j = int(columnas.get()) #columnas
        newj = j
        print(type(i))
        print(type(j))

        matrizA= np.zeros((i, j))
        rangof = list(range(i))
        rangoc = list ( range(j))

        #indica que posicion (solo como texto)
        textoinsertat = Entry(ventana2,width=40)
        textoinsertat.place(x=10,y=110)

        

        #Entrada de datos del usuario para lo posicion i j
        #valores = Entry(ventana2)
        #valores.place(x=10,y=143)

        #Boton para guardar datos en el array MatrizA
        #guarDato =Button(ventana2,bg="green",text="✔",fg="white",height=1,cursor="hand2",command=cambiar)
        #guarDato.place(x=150,y=140)



    #Nueva ventana
    ventana2 = Toplevel()
    ventana2.title("Matrices Triangulares")
    ventana2.geometry("800x500")
    ventana2.resizable(0,0)  #Pagina con tamaño definido 

    #Titulo
    barra2 = Frame(ventana2,bg="pink",width=800,height=30)
    barra2.place(x = 0)
    titulo2 = Label(barra2,bg="pink",text="PROGRAMA MATRICES TRIANGULARES")
    titulo2.place(x=300)

    #etiqueta filas 
    Label(ventana2,text="Ingresa el numero de filas que tiene tu matriz ").place(x=10,y=40)
    #Entrada de dato de filas
    filas = Entry(ventana2,width=4)
    filas.place(x=300,y=44)

    #etiqueta columnas
    Label(ventana2,text="Ingresa el numero de columnas que tiene tu matriz ").place(x=10,y=80)
    #Entrada de dato de columnas
    columnas = Entry(ventana2,width=4)
    columnas.place(x=300,y=84)

    #contenedor de boton
    frameboton1 = Frame(ventana2,bg="green")
    frameboton1.place(x = 350,y=60)
    #Boton para inserar datos de filas y columnas
    insertar = Button(frameboton1,bg="green",fg="white",text="Insertar",height=1,cursor="hand2", command=enteros)
    insertar.pack()

    
#Page Geometry
root = Tk()
root.geometry("800x500") 
root.title("Programas")
root.resizable(0,0)  #Pagina con tamaño definido 

#Frame 1  Barra de hora y fecha
barra = Frame(root,bg="pink",width=800,height=30)
barra.place(x = 0)

#Titulo "PROGRAMAS"
titulo = Label(barra,bg="pink",text="PROGRAMAS")
titulo.place(x=360)

#label 1 Hora y fecha
fecha = Label(barra,text=f"{fecha()}",bg="pink")
fecha.place(x=600,y=0)

#Contenedor Boton1
frame2 = Frame(root,bg="pink")
frame2.place(x = 360, y=150)
boton1 = Button(frame2,text="matriz 1",bg="pink",cursor="hand2",command=programa1)
boton1.pack()

root.mainloop()