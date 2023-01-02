from os import system

def funcion1(list):

    lista4 = []
    n = len(list)
    for xs in list:
        l = f"{xs}X^{n}"
        n -= 1 
        lista4.append(l)

    return lista4   

def valorA(list):
    s = list[0]

    return s

def valorI(list):
    d = list.pop()
    return d

def invertir(lst):
   return [i for i in list]

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

    c = invertir(factoresx)
    y = invertir(factoresy)

    factoresx.extend(c)
    factoresy.extend(y)
   
    return factoresx,factoresy

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
        #print(uwu)
    return raiz    

n = int (input ("de que grado es la función: "))

c = n     #cont
lista1 = []  #guarda

while (c != 0):
	z = int(input(f"ingresa el valor de X{c}: " ))
	lista1.append(z)
	c -=1
indep = int(input("Ingresa el valor independiente: "))

system("cls")

g = funcion1(lista1)
g = " ".join(g)
ecuacion = f" {g} {indep}"
print(ecuacion)

lista1.append(indep)
print(lista1)

a = valorA(lista1)
b = valorI(lista1)

fac = factores(a,b)
print(f"los factores de {a} son {fac[0]}")
print(f"los factores de {b} son {fac[1]}")

primera = sintetica(fac[0],lista1)
segunda = sintetica(fac[1],lista1)

print(f"las raices de {ecuacion} son")
print(f"x : {segunda}")
print(f"x : {primera}")