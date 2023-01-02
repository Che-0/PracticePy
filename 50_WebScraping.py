import bs4
import requests


resultado = requests.get("https://www.escueladirecta.com/")   #pide el sitio web


sopa = bs4.BeautifulSoup(resultado.text,'lxml')   #<---Esta madre organiza el desmadre que entrega resutados

#print(sopa)   <--- Esta madre imprime elcodigo

#print(sopa.select('title'))  #Trae en formato de lista esa o esas etiquetas que se encuentren ahí

print(sopa.select('title')[0].getText())  #asi solo emprime el contenido de la etiqueta y no la etiqueta 


parrafo_especial = sopa.select('p')[3].getText()   #el corchete indica que solo traiga el elemento 3 y no toda la lista
print(parrafo_especial)