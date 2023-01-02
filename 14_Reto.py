from __future__ import print_function
from msilib.schema import AdvtUISequence
import random
from sqlite3 import enable_shared_cache

lista1 = ["gato","perro","conejo","tortuga","pato"]

def bienvenida():
    print("Hola este es el juego de el ahorcado, tienes 6 vidas para adivinar la palabra")
    print("Te doy una pista, es un animal ")


def seleccionar(d):
    
    return random.choice(d)  

def lineas(g):
    j = []
    for x in g:
        j += '_'
    
    return print(" ".join(j))

#def compara(k,d):



def proceso(t):
    
    print(f"la longitud de la palabra es de {len(t)}")
    lineas(t)

    list2 = []
    for r in t:
        list2 += '_'

    vidas = 6
    while vidas!= 0:
        print("".join(list2))    
        x = str(input("introduce una letra: "))
        
        if x in t:
            list2[t.find(x)] = x
            if "_" not in list2:
                return print(f"Felicidades, GANASTE! , la palabra era {t}") 

        else:
            print("k wey")
            vidas -= 1
    

    else:
        print("PERDEDOR")

def juego():
    bienvenida()
    
    c = seleccionar(lista1)
    print (c)
    #lineas(c)
    proceso(c)

juego()