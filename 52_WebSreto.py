"""
http://books.toscrape.com/index.html
sirve para precticar el scrapping  

Obetener todos los titulos de los libros que tengan 4 o mas estrellas
http://books.toscrape.com/



"""

import bs4
import requests

url_base = "http://books.toscrape.com/catalogue/page-{}.html" # las llaves para aplicar un format

#print(url_base.format('10'))   #pone ese numero en el lugar de las llaves de arriba
#solo voy a obtener lo de 10 paginas

#for n in range(1,11):
#    print(url_base.format(n))
#para ver lo de las estrellas 

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


libros = sopa.select('.product_pod')

ejemplo = libros[0].select('a')[1]["title"]

print(ejemplo)