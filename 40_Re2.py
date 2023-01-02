import re

texto = "llama al 564-525-6588 ya mismo"

#patron = r'\d\d\d-\d\d\d-\d\d\d\d' # r indica que es una cadena especial
patron = r'\d{3}-\d{3}-\d{4}' # r indica que es una cadena especial
#          numeros


busqueda = re.search(patron,texto)
#busqueda = re.findall(patron,texto)

#print(busqueda.group())

# (r^\D',fdf)    es para decir que encontro o no un digito de esos al principio
#r'^Hola 
# r'\D$'   checa al finale del string
# r'^\s'   excluye los caracteres en blanco


#este otro pedo se me ocurriria ocupar en tareas de separar texto
#o un desmadre asi, wacha 


texto2 = "No estamos los jueves por las tardes"

clave = re.findall(r'[^\s]+',texto)
print(clave)
print("".join(clave))


#r'@\w+\.com'