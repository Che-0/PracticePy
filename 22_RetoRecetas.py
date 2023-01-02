from pathlib import Path
from os import system
from os import remove
import os
import sys

def ruta_abs():
    ruta ='C:\\Users\\Che\\Recetas'
    e =  os.path.abspath(ruta)
    return e

def listar(x):
    d = os.listdir(x)
    print("Tienes ", len(d), " recetas")
    print(d)
    return d    # <---- direccion de las carpetas 

def recetas(g):
    print(os.listdir(g))
    return os.listdir(g)

#def lectura(r):

def menu():
    print("""
Que quieres hacer ?
    [1]-leer receta 
    [2]-crear receta 
    [3]-crear categoria
    [4]-eliminar receta
    [5]-eliminar categorias
    [6]-finalizar programa
    """)
    j = int(input("Introduce el numero: "))
    opcion(j)

def opcion(h):
    system('cls')
    if h == 1:
        print("Que categoria quieres? \n") #+ recetas())
        x = recetas(ruta_abs())
        o = input("Escribe el nombre de la categoria: ")
        if o  in x:
            ruta = Path('C:/Users/Che/Recetas') / o
            #os.chdir('C:\\Users\\Che\\Recetas\\ ' + o)
            print("\nElige la receta que quieras leer ( en base a el numero de receta)\n")
            #print(ruta)
            print(os.listdir(ruta))
            e = input("Introduce la receta: ")
            leer = open(ruta / e,'r')
            print(leer.read())
            leer.close()
        
    elif h == 2:
        system('cls')
        x = recetas(ruta_abs())
        o = input("Escribe el nombre de la categoria: ")
        if o  in x:
            ruta = Path('C:/Users/Che/Recetas') / o
            os.chdir(ruta)
            nueva_receta = input("Ingresa el nombre que quieres que tenga la nueva receta: ")
            nueva_receta += ".txt"
            print(nueva_receta)
            #xto = input("Ingresa la receta: ")
            nuevo_archivo = open(nueva_receta,'w')
            nuevo_archivo.write(input("escribeeeee: "))
            nuevo_archivo.close
            print("receta creada")
    
    elif h == 3:
        system('cls')
        owo = input("Escribe el nombre del nuevo directorio: ")
        ruta = Path('C:/Users/Che/Recetas') 
        os.chdir(ruta)
        os.mkdir(owo)

    elif h == 4:
        system('cls')
        print("Que categoria quieres? \n") #+ recetas())
        x = recetas(ruta_abs())
        o = input("Escribe el nombre de la categoria: ")
        if o  in x:
            ruta = Path('C:/Users/Che/Recetas') / o
            #os.chdir('C:\\Users\\Che\\Recetas\\ ' + o)
            print("\nElige la receta que quieras eliminar ( en base a el numero de receta)\n")
            #print(ruta)
            print(os.listdir(ruta))
            e = input("Introduce la receta: ")
            os.chdir(ruta)

            os.remove(e)
    
    elif h == 5:
        sys("cls")
        recetas(ruta_abs())
        ruta = Path('C:/Users/Che/Recetas')
        os.chdir(ruta)
        print(os.getcwd())
        e = input("Escribe el nombre de la categoria a eliminar: ")
        os.rmdir(e)
    
    elif h == 6:
        pass

def bucle():
    while True:
        menu()
        x = input("Quieres volver al menu? \n s/n:")
        if x == 's':
            continue
        elif x =='n':
            break

def bienvenida():
   
    print("Hola las recetas estan en el directorio " + ruta_abs())

    # ------------------#  Cantidad de recetas 
    x = listar(ruta_abs())
    bucle()

bienvenida()