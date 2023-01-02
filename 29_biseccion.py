# Proyecto de bissciom
import numpy as np
import sympy as sym
from tabulate import tabulate
import tkinter
import matplotlib.pyplot as plt
from pylab import *
import tkinter

def listarfx(ls):
    lasfx = []
    for a in ls:
        c = a[1] 
        lasfx.append(c)
    return lasfx

def puntomedio(a, b):
    pm = ((a+b) / 2) 
    return pm

def formulafx(a):
    j = ecuacion.subs(x, a)
    return j

def sustitucion(a):
    x = sym.Symbol('x')
    o = ecuacion.subs(x,a)
    return o

def multiplicacion(a, b):
    d = a*b
    return d

def errorp(a, b):
    d = ((a-b)/a) * 100
    return d

x = sym.Symbol('x')
ecuacion = input("ingresa la ecuacion: ")
ecuacion = eval(ecuacion)
print(ecuacion)

lmmenor = float(input("Ingresa el limite menordel rango : "))
lmmayor = float(input("ingresa el limite superior del rango: "))
incrementos = float(input("Introduce el numero de incrementos: "))
lista_rangos = np.arange(lmmenor, lmmayor+.5, incrementos)

z = []
for n in lista_rangos:
    k = ecuacion.subs(x, n)
    k = round(k, 4)
    z.append([n, k])

print(tabulate(z, headers=["x", "f(x)"]))

coordenadas= listarfx(z)

print("Tu grafica es: ")
grid()
plot(coordenadas,"o-")
xlabel("Eje X")
ylabel("Eje Y")
title("Puntos f(x)")
plt.show()

print("---"*6, "Intervalos", "---"*6)
xa = z[0][0]
xb = z.pop()
xb =xb.pop(0)
xr = puntomedio(xa, xb)
fxa = sustitucion(xa)
print(xa)
print(fxa)
fxr = sustitucion(xr)
fxar = multiplicacion(fxa, fxr)

if fxar > 0:
    xa = xr
elif fxar < 0:
    xb = xr

print("El punto se puede encontrar en un promedio de 10 iteraciones o menos")
iter = int(input("Ingresa el numero de iteraciones: "))
while iter >= 0 :

    fxrvieja = fxr
    xr = puntomedio(xa, xb)
    fxr = sustitucion(xr)
    fxar = multiplicacion(fxr, fxrvieja)
    
    if fxar > 0:
        xa = xr
    elif fxar < 0:      
        xb = xr

    iter -= 1

    

print(f"xa vale:  {xa}")
print(f"xb vale : {xb}")
p = puntomedio(xa,xb)
print(f"su punto medio esta en: {p}")
errorporcentual = errorp(p,xr)
print(f"su error porcentual es de {errorporcentual}")


vals = [formulafx(xa),formulafx(p),formulafx(xb)]

#----------Grafica el punto medio--------
print("Grafico: ")
title("Punto medio f(x)")
plot(vals,"o-")
xlabel("Eje X")
ylabel("Eje Y")
grid()
plt.show()

print("fin del programa")
input("tab para finalizar .....\n")