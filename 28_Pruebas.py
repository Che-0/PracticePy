import numpy as np  #libreria para generar matrices con listas

i = int(input ("cuántas filas tiene la matriz: "))
j = int(input ("cuántas columnas tiene: "))

#Genera una matriz de i * j, llena de 0s
matrizA= np.zeros((i, j))

#Rango de 0 a i
longitud = list(range (i)) 

#iteramos en cada posicion para almacenar un valor
for a  in longitud:
	for b in longitud:
		matrizA [a][b] = int(input(f"Ingresa el valor de la posición {a} {b}: ") )
	
print ("matriz 2")
filasAB = i   #valores para generar la matriz AB
longitudAB = list(range(i))
longitudAB2= list(range (1,i))
columnasAB= j+1  #Valores para generar la matriz AB con una columna mas

matrizB = np.zeros((i, j))
longitud = list(range (i))

#iteramos en cada posicion para almacenar un valor
for c  in longitud:
	for d in longitud:
		matrizB [c][d] = int(input(f"Ingresa el valor de la posición {c} {d}: ") )
	
matrizC = []      
#Generamos la matriz invertida de B y la almacenamos en C    
for i in longitud:
	columna = matrizB [:,i]
	matrizC.append(columna)

matrizC = np.array(matrizC)  #convertimos la lista de tipo array a matriz con su formato 

#print (matrizA) #matriz uno
#print (matrizB) #matriz dos
#print (matrizC) #matriz invertida de B

matrizAB = np.zeros((filasAB,columnasAB))
matrizAB = np.array(matrizAB)
print(matrizAB)

#Agrega los elementos de la primera matriz 
for f in longitudAB:
	for g in longitudAB:
		if matrizA[f][g] != 0:
			matrizAB[f][g] = matrizA[f][g]

#Agrega los elementos de la segunda matriz
for f in longitudAB:
	for g in longitudAB:
		if matrizC[f][g] !=0:
			matrizAB[f][g+1]=matrizC[f][g]

print("La combinacion de las matrices es: ")
print(matrizAB)