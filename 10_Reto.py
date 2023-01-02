#El usuario tiene que ingresar una frase
#Pedir 3 letras
#Decir cuantas hay de c/u

from posixpath import split


x = str(input("Ingresa la frase que tu quieras: "))
x = x.lower()


a,b,c = ((input("escoge la primera letra "), input("escoge la segunda letra ") ,input("escoge la tercera letra ")))

print("ok")

print(f"La cantida de letras {a} es de: ",x.count(a))
print(f"La cantida de letras {b} es de: ",x.count(b))
print(f"La cantida de letras {c} es de: ",x.count(c))

print("tu frase tiene", x.split())
print("basicamente son ", len(x.split()))


print(x[::-1])

print("fin alaverga")
