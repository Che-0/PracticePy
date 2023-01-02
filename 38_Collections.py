from collections import Counter
from collections import defaultdict #<- para que cuando no encuentre algo no de error y diga nada 
from collections import  namedtuple # lo explico en el ejemplo. esta facil creo


"""collections es """

#En si sirve para un chingo de cosas 
#principalmente para listas tuplas y diccionarios 
#entre las funciones "mas utilizadas " segun , porque aun no le se muy bien
#estan
#counter que es para contar elementos en una lista asi ***************
#    
lista = [1,1,1,12,2,2,2,3,3,4,4,4,5]
print(Counter(lista))
#Counter({1: 3, 2: 3, 4: 3, 3: 2, 12: 1, 5: 1})  <- lo devuelve como en diccionario pero es de otro type

#funciona tanto para palabras, letras o numeros

x = Counter(lista)
print(x.most_common())     #<- tiene que ser un obj pSara heredar sus metodos
# Counter.mostcommon(aui van cuantos quieres mostrar )


#ejemplo de defaultdic   **************************
mi_dic = {'uno':'verde', 'dos':'azul', 'tres':'rojo'}

# print(mi_dic['cuatro']) <---  Esta madre da error porque no esta ese pedo

#pero si en cambio hacemos esto

mi_dic2 = defaultdict(lambda: "el elemento no se encontro" ) #<- asignamos lo que dira si no esta
mi_dic2['uno'] = 'verde'  #<-Agregamos un valor al nuevo diccionario 
print(mi_dic2['dos'])  # mostrara el mensaje de defaulrdicx


#namedtuple          **************************************
#okey, imaginemos que tenemos una tupla con tres elementos 
# y queremos acceder a alguno de ellos

mi_tupla = (500, 18, 65)

mi_tupla[1]  # esta madre da 18

#pero la tupla puede ser de un tamaño muy grande y esta cabron acordarse
# asi que se mejor le das un nombre 
# objeto  metodo   parametro obj  atributos
#tuplq nominada
Persona = namedtuple('Persona',['nombre','altura','peso']) #Es como una clase

manuel =  Persona('Manuel',1.70,200) #aqui le asignamos la "clase y atributos" asi se puede ver 

#esto facilita acceder a los elementos de la tupla, ya que solo es cuestion de llamar los tributos
print(manuel.altura)  # asi es mas facil un we y sus pendejadas de caracteristicas 
# tambien puedes acceder con el indice  manuel[atributo]
