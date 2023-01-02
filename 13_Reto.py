from random import shuffle

#Un programa que te haga escoger entre 4 palitos
#El que tenga el menor tamaño pierde 


#lista inicial

palitos = ["-","--","---","----"]

#mezcla palitos

def mezcla(list):
    shuffle(list)
    return list
    

#pedirle intento

def probar_suerte():
    intento = " "
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero del 1 al 4")
        
    return int(intento)

inten = probar_suerte()
print(inten)
