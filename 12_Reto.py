from asyncio.base_futures import _FINISHED
from random import randint

#un juego en el que tienes 8 intentos para 
#adivinar el numero (1,100)

#pide el name del jugador y la chingada
# si es superior o menor al rango ("eres un pendejo")
# si es menor al n
#si es mayor
#es el correcto 
#intentos

x = input("Hola, introduce tu nombre: ")

print(f" {x} este es un juego de adivinanzas")
print("Tienes que adivinar un numero del 1 al 100 pero solo tendras 8 intentos, adelante")

y = randint(1,101)
print(y)

intentos = 8

uwu = 8

while intentos != 0 :

    z = int(input("introduce el nunero: "))

    if z < 0 or z > 100:
        print("fuera de rango")
        intentos -= 1

    elif z > y:
        print("El numero es menor")
        intentos -= 1

    elif z < y:
        print("El numero es mayor")
        intentos -=1

    elif z == y:
        print("Felicidades, es el numero correcto")
        print(f"lo lograste en {uwu - intentos + 1} intentos")
        break

    elif intentos == 0:
        print("perdiste")
        
if intentos == 0:
    print("tus intentos se terminaron , perdiste")

else:
    print("fin")