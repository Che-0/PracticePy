
import numpy as np  #libreria para generar matrices con listas

i = int(input ("cuántas filas tiene la matriz: "))
j = int(input ("cuántas columnas tiene: "))

#Genera una matriz de i * j, llena de 0s
matrizA= np.zeros((i, j))

rangof = list(range(i)) #filas
rangoc = list ( range(j)) #columna 

#iteramos en cada posicion para almacenar un valor
for a  in rangof:
	for b in rangoc:
		matrizA [a][b] = int(input(f"Ingresa el valor de la posición {a} {b}: ") )

coordenadas = []
valores = []

for i in rangof:
	for j in rangoc:
		if matrizA[i][j] != 0:
			crd = i,j
			coordenadas.append(crd)
			valores.append(matrizA[i][j])
print(coordenadas)
print(valores)

matrizB = np.array(valores)
print("la matriz B es ") #matriz reducida de A
print(matrizB)

matrizC = np.zeros((3,4))   #filas y columnas
print(matrizC)

for val in valores:
	for rang in coordenadas:
		matrizC[rang[0]][rang[1]] = val

print("la matriz original es:")
print(matrizC)