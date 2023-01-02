from os import system

#da formato para imprimir la ecacion en String
def imprimir(list):

    lista4 = []
    n = len(list)
    for xs in list:
        l = f"{xs}X^{n}"
        n -= 1 
        lista4.append(l)
    return lista4   

#Obtiene el primer valor de la lita
def valorA(list):
    s = list[0]
    return s

#Obtiene el ultimo valor de la lista
def valorI(list):
    d = list.pop()
    return d

#Genera dos listas de los factores de x y v y los retorna
def factores(x,v):
    factoresx = []
    factoresy = []
     
    d = list(range(1,x+1))
    for dprim in d:
        if x % dprim == 0:
            factoresx.append(dprim)
        else:
            continue

    h = list(range(1,v+1))
    for hprim in h:
        if v % hprim == 0:
            factoresy.append(hprim)
        else:
            continue

    return factoresx,factoresy 

#metodo de division sintetica que retorna solo los valores
# de x cuyas raices dan 0 en forma de una lista
def sintetica(list1,list2):
    
    final = valorI(list2)
    
    raiz = []
    for x in list1:
        uwu = 0
        for y in list2:    
            h = y + uwu
            uwu = x * h
            h = y + uwu
            if uwu + final == 0:
                raiz.append(x)
    return raiz    

# Genera una lista con los valores negativos de una lista proporcionada
# y lo retorna
def reve(list):
	g = []
	for i in list:
		tr = -1 * i
		g.append(tr)
	return g

n = int (input ("de que grado es la función: "))

c = n     #cont
lista1 = []  #guarda

while (c != 0):
	z = int(input(f"ingresa el valor de X{c}: " ))
	lista1.append(z)
	c -=1
indep = int(input("Ingresa el valor independiente: "))

system("cls")

g = imprimir(lista1)
g = " ".join(g)
ecuacion = f" {g} {indep}"
print(f"la ecuacion es: {ecuacion}")

lista1.append(indep)

a =abs( valorA(lista1))
b =abs(valorI(lista1))

fac = factores(a,b)
negativosx = reve(fac[0])
negativosy = reve(fac[1])

fac[0].extend(negativosx)
fac[1].extend(negativosy)
print(f"los factores de {a} son {fac[0]}")
print(f"los factores de {b} son {fac[1]}")

primera = sintetica(fac[0],lista1)
segunda = sintetica(fac[1],lista1)

print(f"las raices de {ecuacion} son")
print(f"x : {primera}")
print(f"x : {segunda}")