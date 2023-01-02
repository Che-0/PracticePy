import random 
import time
from statistics import mean

lista = [random.randint(0,100) for x in range(100)]

print (f"La lista de numeros es: \n {lista}")

rango= list(range (len(lista)))

iteraciones = 0
cambios = 0
intercambio = True
start = time.time()
while intercambio:
	for i in rango:
		for j in rango:
				if lista[i] < lista[j]:
					aux = lista[i]
					lista[i] = lista[j]
					lista[j] = aux
					intercambio = True
					cambios += 1

				elif lista[i] == lista[j]:
					aux = lista[i]
					lista[i] = lista[j]
					lista[j] = aux
					intercambio = True

		#if lista[-1]>lista[-2]:
		#	intercambio = False
		#else:
		#	iteraciones += 1
		#iteraciones += 1

end = time.time() 
print (lista)

media = mean(lista)

print(f"Tiempo de ejecución: {end - start}\n")
print(f"numero de iteraciones: {iteraciones}")
print(f"numero de cambios: {cambios}")
print(f"La mediana aritmetica es: {media}")