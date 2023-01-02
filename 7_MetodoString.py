#okey
#how refert wen i say "metodos de string"
#well i refer a lot metods used in vars strings
#watch this

texto = "Este es el texto de manuel"

resultado = texto[2].upper()

#pero con este desmade podemos hacer mayusculas las que queramos
#seria algo like

#resultados = texto[2].upper()


print (resultado)


texto2 = "Gatos hijos de puta"

resultados2 = texto2.lower()
print(resultados2)

resultados2 = resultados2.split()
print(resultados2)

#tambien puedes poner como argumente en split una letre
#y esa letra se tomara para cortar split(a)
# ['g', 'tos hijos de put', '']

a = "la"
b = "re"
c = "mil puta"
e = " ".join([a,b,c])
print(e)
