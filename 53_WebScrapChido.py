import bs4
import requests

#crear url sin numero de pagina
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

#lista de tituloa con 4 o 5 estrellas
titulos_reating_alto = []

#iterar paginas
for pagina in range (1,51):
    
    #sopa de cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccion de los datos de los libros
    libros = sopa.select('.product_pod')

    #iterar libros
    for libro in libros:
        #chequear qur tengan 4 o mas estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            #guardamos titulo en var 
            titulo_libro = libro.select('a')[1]['title']
            #agregar a la lista
            titulos_reating_alto.append(titulo_libro)


#ver libros

for t in titulos_reating_alto:
    print(t)