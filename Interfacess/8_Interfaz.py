
from tkinter import *
import time

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

    #aqui se programa lo que tiene que hacer esta pagina


boton1 = Button(frame2,text="Matrices",bg="pink",command=comando1) #Nombre del boton 
boton1.config(cursor="hand2")
boton1.pack()

frame3 = Frame()
frame3.pack(expand= True ,anchor=S,side=RIGHT,fill= "x")
frame3.config(bg="pink")
frame3.config(width="100", height="40")

root.mainloop()