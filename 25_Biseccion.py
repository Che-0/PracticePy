import numpy as np   #<--- permite valores flotantes para crear un rango 

# Formulas que se utilizaran

# Xr = (Xa + Xb) / 2

# f(Xa)*(Xr)

#Ep = ((Xr(actual) * Xr(anterior)) /2) * 100

def ingresar():
    n = int(input("de que grado es la función: "))

    c = n 
    lista1 = []

    while (c != 0):
        z = int(input(f"ingresa el valor de X{c}: "))
        lista1.append(z)
        c -= 1
    
    return lista1

def rango():
    print("Rango en el que quieres los valores de x y f(x) ")
    inicial = float(input("Ingresa el valor inicial: "))
    final   = float(input("Ingresa el limite: "))
    incremento = float(input("Ingresa los incrementos: "))
    lista_rangos = np.arange(inicial,final+.5,incremento)

    return lista_rangos

def convertirfloats(ls):
    
    uwu = []
    
    for c in ls:
        f = float(c)
        uwu.append(f)
    return uwu
    

def owo(d,f):
    r =[]
    for s in d:
        r.append(s*f)
    return r

def sumalista(list):
    for h in list:
        sumatotal += h
    return sumatotal

def ecuacion(rango,valores,i):
    contador = len(valores)
    potencia = len(valores)

    valoresflot = convertirfloats(valores)

    fx = []

    for n in rango:
        e = owo(n,valores)
        for resultado in e:
            nuevo = resultado**potencia
            fin = sumalista(nuevo) -i
            fx.append(fin)
            potencia -=1
        
    return fx

x = ingresar()
print(x)

indep = int(input("Ingresa el valor independiente: "))

d = rango()
print(d)

tabulado = ecuacion(d,x,indep)
print(tabulado)