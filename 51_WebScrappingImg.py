import bs4
import requests

page = requests.get('https://www.escueladirecta.com/')

soup = bs4.BeautifulSoup(page.text,'lxml')

imagenes  = soup.select('.course-box-image')[0]   #esa madre se puede poner para traersolo uno 
#src almacena el link de la imagen, entonces lo especificamos en el corchete para que lo extraigo

imagenes  = soup.select('.course-box-image')[0]['src']  #solo obtendremos el link y no todo el desmadre
print(imagenes)

#for i in imagenes:
#    print(i , "\n")
#
#print(f"la cantida de imagenes es de: {len(imagenes)}")

#ya que tenemos la imagen la podemos extraer 

imagen_1 = requests.get(imagenes)
#print(imagen_1.content)     # <-- Regresa la imagen pero en binario (.....o\xbf\x16\xdfR\x9b6\x.....)

#por ello tenemos que transformarlo en imagen de la siguiente manera 

#creamos un new archivo 

with open("E:\python\ImageExtraida.jpg", 'wb' ) as f:
    f.write(imagen_1.content)