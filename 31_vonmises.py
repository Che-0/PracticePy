import sympy as sym
from math import e

#permite convertir el string en una funcion evaluable
def convertir(a):

    x = sym.Symbol('x')
    ecuacion = eval(a)
    return ecuacion

#retorna la derivada de x de una funcion
def derivar(a):

    x = sym.Symbol('x')
    derivada = sym.diff(a,x)
    return derivada

def raizAprox(fxi,fxi2,i):
    x1 = i - (fxi/fxi2)
    return x1

def error(xnueva,anterior):
    errorp = xnueva-anterior/xnueva
    return float(errorp)


def evaluar(funcion,derivada,inicia):
    #evaluar f(x) y f'(x) con el valor de i correspondiente
    x = sym.Symbol('x')
    i = 0
    inicial = inicia
    iteracion = 1
    erroresperado =1
    errorporcentual=100
    while errorporcentual > erroresperado and iteracion<11:
        fxi = funcion.subs(x,inicial)    #funcion prinncipal
        fxi2 = derivada.subs(x,inicial)

        xnueva = raizAprox(fxi,fxi2,inicial)

        errorporcentual = error(xnueva,inicial)
        if errorporcentual <1:
            break
        else:
            print(errorporcentual)
            i += 1
            iteracion += 1
    print ("fxi vale :",xnueva)
    print("fxi2 vale: ",inicial+.001)

funcion = input("Ingresa la funcion: ")
valorinicial = float(input("Ingresa el valor inicial: "))

funcion = convertir(funcion)
derivada = derivar(funcion)
evaluar(funcion,derivada,valorinicial)