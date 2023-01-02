import numpy as np  #libreria para generar matrices con listas

i = int(input ("cuántas filas tiene la matriz: "))
fil = i
j = int(input ("cuántas columnas tiene: "))
col = j
#Genera una matriz de i * j, llena de 0s
matrizA= np.zeros((i, j))

rangof = list(range(i)) #rango filas
rangoc = list ( range(j)) #rango columnas

#iteramos en cada posicion para almacenar un valor
for a  in rangof:
	for b in rangoc:
		matrizA [a][b] = int(input(f"Ingresa el valor de la posición {a} {b}: ") )

coordenadas = [] #lista para guardar coordenada de valores de array != a 0
valores = [] # lista para guardar el valor != de 0

for i in rangof:
	for j in rangoc:
		if matrizA[i][j] != 0:
			crd = [i,j] #tupla de coordenadas
			coordenadas.append(crd)
			valores.append(matrizA[i][j]) #valor de esa posicion

matrizB = np.array(valores)
print("la matriz reducida de A es:") #matriz reducida de A
print(matrizB)
print(valores)
print(coordenadas)
op = input("Quieres ver la matriz original?\ns/n: ")
op = op.lower()
if op == "s":
    print(matrizA)