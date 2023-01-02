import random 
import time
from statistics import mean

lista = [random.randint(0,10000) for x in range(10000)]

print (f"La lista de numeros es: \n {lista}")

rango = len(lista)-1

contador = 0
cambio = 0
start = time.time()
for i in range(0,rango):
    contador+=1
    for j in range(0,rango):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
            cambio +=1
        elif lista[j] == lista[j+1]:
            continue
end = time.time()
print(lista)
media = mean(lista)

print(f"Tiempo de ejecución: {end - start}\n")
print(f"numero de iteraciones: {contador}")
print(f"numero de cambios: {cambio}")
print(f"La mediana aritmetica es: {media}")