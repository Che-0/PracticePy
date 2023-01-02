from site import venv
from tkinter import *


def sumar():
    n1 = txt1.get()
    n2 = txt2.get()
    r = n1 + n2 
    txt3.delete(0,"end")
    txt3.insert(0,r)


root = Tk()
root.title("Suma de dos numeros")
root.geometry("900x500")

label1 = Label(root,text="primer numero: ",bg = "yellow")
label1.place(x =10 , y= 10, width=100, height=40)
txt1 = Entry(root,bg="pink")
txt1.place(x = 120, y = 10, width=100, height=40)

label2 = Label(root,text="Segundo numero: ",bg="pink")
label2.place(x = 10, y = 60, width=100, height=40)
txt2 = Entry(root,bg="pink")
txt2.place(x = 120, y = 60, width=100, height=40)

boton1 = Button(root,bg="pink",text="Sumar",command=sumar())
boton1.place(x = 240, y = 60, width=100, height=40)

label3 = Label(root,text = "resultado: ", bg ="red")
label3.place(x= 10 , y = 110,  width=100, height=40)
txt3 = Entry(root,bg="green")
txt3.place(x = 120, y = 110, width=100, height=40)




root.mainloop()