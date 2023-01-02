# Proyecto de bissciom
import numpy as np
import sympy as sym
from tabulate import tabulate
import matplotlib.pyplot as plt
from pylab import *
import tkinter

def listarfx(ls):
    lasx = []
    lasfx = []
    for a in ls:
        #b = a[0]
        c = a[1] 
        #lasx.extend(b)
        lasfx.append(c)
    return lasfx

def puntomedio(a, b):
    pm = ((a+b) / 2) 
    return pm

def formulafx(a):
    j = ecuacion.subs(x, a)
    return j

def sustitucion(a):
    r = a**4+3*a**3-2
    return r

def multiplicacion(a, b):
    d = a*b
    return d

def errorp(a, b):
    d = (a-b)/a
    return d

x = sym.Symbol('x')
ecuacion = input("ingresa la ecuacion: ") #x**4+3*x**3-2
ecuacion = eval(ecuacion)

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
print(coordenadas)

print("Tu grafica es: ")
#fs,xs= plt()
grid()
plot(coordenadas,"o-")
xlabel("Eje X")
ylabel("Eje Y")
title("Puntos fx")
plt.show()

print("---"*6, "Intervalos", "---"*6)   #considera el primer valor como xa y el ultimo como xb
xa = z[0][0]
print("xa: ", xa)
xb = z.pop()
xb =xb.pop(0)
print("xb: ", xb)

xr = puntomedio(xa, xb)
print("punto medio: ", xr)

fxa = sustitucion(xa)
print(fxa)
fxr = sustitucion(xr)
print(fxr)

fxar = multiplicacion(fxa, fxr)
print(fxar)

if fxar > 0:
    xa = xr

elif fxar < 0:
    xb = xr

print(xa)
print(xb)


#fxrvieja = fxr
#xr = puntomedio(xa, xb)
#print("punto medio: ", xr)
#fxr = sustitucion(xr)
#fxar = multiplicacion(fxr, fxrvieja)
#print("xa es : ", xa)
#print("xb es : ", xb)

#if fxar > 0:
#    xa = xr
#elif fxar < 0:
#    xb = xr

iter = int(input("Ingresa el numero de iteraciones: "))

while iter >= 0 :

    fxrvieja = fxr
    xr = puntomedio(xa, xb)
    print("punto medio: ", xr)
    fxr = sustitucion(xr)
    fxar = multiplicacion(fxr, fxrvieja)
    print("xa es : ", xa)
    print("xb es : ", xb)
    print(fxar)
    if fxar > 0:
        xa = xr
    elif fxar < 0:      
        xb = xr
    
    iter -= 1

print("xa es : ", xa)
print("xb es : ",xb)
print(fxr)
print(fxar)