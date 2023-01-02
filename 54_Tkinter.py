
from tkinter import*

#Inciar tkinter 
root = Tk()

#tamaño de ventana 
root.geometry("1020x630+0+0")  #los ultimos ceros son para indicar en la posicion en la que van a aparecen 

#evitar maximiza
root.resizable(0,0)

#TITULO de la ventana
root.title("Huevos sistema de facturacion")

#color de fondo de la ventana
root.config(bg='pink')


panel_superior = Frame(root,bd=1, relief=FLAT, bg="purple" )
panel_superior.pack(side=TOP )

#etiqueta titulo 
etiqueta_titulo = Label(panel_superior,text="Sistema de facturacion",fg="white",bg="purple",width=25,font=("Dosis",58))
etiqueta_titulo.grid(row=0,column=0)
 
 #panel izquierco
panel_izquierdo = Frame(root, bd= 1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)


#panel de costos
panel_costos = Frame(panel_izquierdo, bd=1 , relief=FLAT)
panel_costos.pack(side=BOTTOM)


#panel comidas 
panel_comidas = LabelFrame(panel_izquierdo, text="comida",font=('Dosis',19),bd=1,relief=FLAT,fg="azure4")
panel_comidas.pack(side=LEFT)

#panel bebidas 
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas",font=('Dosis',19),bd=1,relief=FLAT,fg="azure4")
panel_bebidas.pack(side=LEFT)

#panelpostres
panel_postres= LabelFrame(panel_izquierdo, text="Postres",font=('Dosis',19),bd=1,relief=FLAT,fg="azure4")
panel_postres.pack(side=LEFT)


#panel derecha 
panel_derecha = Frame(root,bd=1,relief=FLAT)
panel_derecha.pack(side = RIGHT) 

#panel calculadora 
panel_calculador = Frame(panel_derecha, bd = 1, relief=FLAT,bg="pink")
panel_calculador.pack()


#panelrecibo 
panel_recibo = Frame(panel_derecha, bd = 1, relief=FLAT,bg="pink")
panel_recibo.pack()

#panel botones
panel_botones= Frame(panel_derecha, bd = 1, relief=FLAT,bg="pink")
panel_botones.pack()

#lista de productos

lista_comidas = ["caldo","mole","arroz","manzana","pera","cordero","salmon","merluza","kebab","pizza"]
lista_bebida =  ["agua","pisto","tony","oso","gine","amper","volt","vive100","te","chocolate"]
lista_postres = ["helado","mimi","fruta","pan","dulces","flan","naaranja","postre1","postrew2","postre3"]

#generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []

contador=0

for comida in lista_comidas:
    
    #crear check button 
    variables_comida.append('')
    variables_comida[contador] = IntVar
    comida = Checkbutton(panel_comidas,text=comida.title(),font=('Dosis',19,'bold'),onvalue=1,offvalue=0,variable= variables_comida[contador])

    comida.grid(row=contador, column=0, sticky=W)
    
    #crear los cuadros de entrada 
    cuadros_comida.append('')
    texto_comida.append('')
    cuadros_comida[contador] = Entry(panel_comidas,font=("Dosis",18,"bold"),bd=1,width=6,state=DISABLED,textvariable=texto_comida[contador] )

    cuadros_comida[contador].grid(row=contador,column =1)

#generar items bebida
variables_bebida = []
contador=0

for bebida in lista_bebida:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar
    bebida= Checkbutton(panel_bebidas,text=bebida.title(),font=('Dosis',19,'bold'),onvalue=1,offvalue=0,variable= variables_bebida[contador])

    bebida.grid(row=contador, column=0, sticky=W)
    contador+=1

#generar items postres
variables_postres = []
contador=0

for postres in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar
    postres= Checkbutton(panel_postres,text=postres.title(),font=('Dosis',19,'bold'),onvalue=1,offvalue=0,variable= variables_postres[contador])

    postres.grid(row=contador, column=0, sticky=W)
    contador+=1


root.mainloop()


#las putas interfaces en tkinder me dan asco 
#re puta mierda
