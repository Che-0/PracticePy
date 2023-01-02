from cProfile import label
from tkinter import *
import time

import sympy as sym
import numpy as np
from tabulate import tabulate

root = Tk()
root.title("Programas")
root.geometry("950x550") 
#root.iconbitmap("gato.ico")
#img = PhotoImage(file="wife.gif")


frame1 = Frame()
frame1.pack(fill = "x")
frame1.config(bg= "pink")
frame1.config(width="100", height="40")

funciondia = time.strftime('%d-%m-%y')
funciontiempo = time.strftime('%H:%M:%S')

#margen superior de la ventana principal que muestra la hora y fecha
tiempo = Label(frame1,text=(f"Hora: {funciontiempo}   Fecha: {funciondia} "),font=10)
tiempo.pack(padx=0,pady=10)
tiempo.config(bg="pink")

#margen inferior
frame2 = Frame(bg="pink")
frame2.config(width=60,height=40)
frame2.pack(padx=30,pady=40)


  
def accion1():
    """" 
    Genera una nueva ventana que contiene el programa con los metodos y funciones de
    biseccion
    """

    def accionborrar():
        """Borra los datos de las primeras labels
        Puesto a que no estan en la funcion de accion2, entonces se tuvo que hacer
        esta funcion y borrarlo al accionar el boton 4, que elimina los datos 
        """
        texto1.delete(0,"end")
        texto2.delete(0,"end")
        texto3.delete(0,"end")
        texto4.delete(0,"end")
        
    ventana = Toplevel()
    ventana.title("Programa 1")
    ventana.geometry("950x550")
   
    titulo = Label(ventana,text="Biseccion",bg="pink")
    titulo.grid(row=0,columnspan=6,ipadx=5,ipady=10,padx=10,pady=20)

    label1 = Label(ventana,text="Introduce la ecuacion: ")
    label1.grid(row=2,column=3,padx=10)

    texto1 = Entry(ventana,bg="white")
    texto1.grid(row=2 ,column=5,padx=20)
    
    def accion2():
        """Esta funcio almacena las funciones del metodo biseccion que se utilizaran durante el
        proceso en este y otros botones.
        Tambien se encarga de generar el tabulado de la funcion dada por el usuario
        """
        def puntomedio(a, b):
            pm = ((a+b) / 2) 
            return pm
        def sustitucion(a):
            x = sym.Symbol('x')
            o = ecuacion.subs(x,a)
            return o
        def multiplicacion(a, b):
            d = a*b
            return d
        def errorp(a, b):
            d = ((a-b)/a) * 100
            return d

        x = sym.Symbol('x')
        r = str(texto1.get())
        ecuacion = eval(r)
        limitemenor = float(texto2.get())
        limitemayor = float(texto3.get())
        intervalos = float(texto4.get())

        lista_rangos = np.arange(limitemenor, limitemayor+.5, intervalos)

        z = []
        for n in lista_rangos:
            k = ecuacion.subs(x, n)
            k = round(k, 4)
            z.append([n, k])
        
        label5 = Label(ventana,text="Tabulado")
        label5.grid(row=9,column=3,padx=30,pady=30)
        label6 = Label(ventana,text=tabulate(z, headers=["x", "f(x)"]),bg="pink")
        label6.grid(row=9,column=5,padx=30)

        def accion3():
            """Esta fiuncion se encarga de recibir el numero de iteraciones 
            y lo utiliza como limite para repetir el proceso de biseccion 
            dando como resultado final xa, xb, punto medio y el indice de error porcentual
            """
            iter = int(texto5.get())
            while iter >= 0 :
                t = fxr
                a = xa
                b = xb
                r = xr
                fxrvieja = t
                r = puntomedio(a, b)
                t = sustitucion(r)
                fxar = multiplicacion(t, fxrvieja)
    
                if fxar > 0:
                    a = r
                elif fxar < 0:      
                    b = r

                iter -= 1

            label9 = Label(ventana,text=f"xa vale: {a}")
            label9.grid(row=7,column=8,padx=5)

            label0 = Label(ventana,text=f"xb vale: {b}")
            label0.grid(row=8,column=8,padx=5)

            p = puntomedio(a,r)

            label11= Label(ventana,text=f"El punto medio es: {p}")
            label11.grid(row=9,column=8,padx=5)

            errorporcentual = errorp(p,r)

            label12= Label(ventana,text=f"El error porcentual es de: {errorporcentual}")
            label12.grid(row=10,column=8,padx=5)

            def accion4():
                """Destruye todas las etiquetas que contengan informacion de la funcion 
                que se haya realizado para poder volver a calcular otra funcion
                """
                accionborrar()
                texto5.destroy()
                boton3.destroy()
                label6.destroy()
                label5.destroy()
                label7.destroy()
                label8.destroy()
                label9.destroy()
                label0.destroy()
                label11.destroy()
                label12.destroy()
                boton4.destroy()
            boton4 = Button(ventana,text="Borrar datos",bg="red",fg="white",cursor="pirate",command=accion4)
            boton4.grid(row=12,column=11)
            


        xa = z[0][0]
        xb = z.pop()
        xb =xb.pop(0)
        xr = puntomedio(xa, xb)
        fxa = sustitucion(xa)
        
        fxr = sustitucion(xr)
        fxar = multiplicacion(fxa, fxr)

        if fxar > 0:
            xa = xr
        elif fxar < 0:
            xb = xr

        label7 =Label(ventana,text="El punto se puede encontrar en un promedio de 10 iteraciones o menos")
        label7.grid(row=2,column=8,padx=5)
        
        label8 =Label(ventana,text="Ingresa el numero de iteraciones que quieres realizar: ")
        label8.grid(row=4,column=8)

        texto5 = Entry(ventana) #iteraciones 
        texto5.grid(row=5,column=8)            

        boton3 = Button(ventana,text="✔",bg="green",fg="white",cursor="hand2",command=accion3)
        boton3.grid(row=6,column=8,padx=5)



    boton2 = Button(ventana,text="insetar datos",bg="green",fg="white",command=accion2,cursor="hand2")
    boton2.grid(row=7, columnspan=6,padx=30,pady=20)
    
    label2 = Label(ventana,text="Ingresa el limite menor: ")
    label2.grid(row = 4,column=3,padx=30,pady=10)

    texto2 = Entry(ventana,bg="white")   #lmmenor
    texto2.grid(row=4 ,column=5,padx=20)

    label3 = Label(ventana,text="Ingresa el limite mayor: ")
    label3.grid(row = 5,column=3,padx=30,pady=10)

    texto3 = Entry(ventana,bg="white")   #lmmayor
    texto3.grid(row=5 ,column=5,padx=20)

    label4 = Label(ventana,text="Ingresa el intervalo: ")
    label4.grid(row= 6,column=3,padx=30,pady=10)

    texto4 = Entry(ventana,bg="white")  #pasos
    texto4.grid(row=6,column=5,padx=20)

boton1 = Button(frame2,text="biseccion",bg="pink",command=accion1)
boton1.config(cursor="hand2")
boton1.pack()



frame3 = Frame()
frame3.pack(expand= True ,anchor=S,side=RIGHT,fill= "x")
frame3.config(bg="pink")
frame3.config(width="100", height="40")

#labe0 = Label(root,image=img)
#labe0.config(width=50,height=300)
#labe0.pack(side = RIGHT)
#labe0.pack(side=RIGHT,anchor=SE)

root.mainloop()