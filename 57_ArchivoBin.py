#para este pedo se necesita del modulo  pickle
#es para el manejo de ficheros 

import pickle

lista = [1,2,3,4,5]

with open("57_Lista.pckl","wb") as fichero:    #write binari
    pickle.dump(lista,fichero)
    
# la función dump tiene dos argumentos: el objeto pickle,
#  que es la lista de tareas y un objeto file donde queremos escribir el pickle, que es todo.pickle. 

fichero = open("57_Lista.pckl","rb")
contenido = pickle.load(fichero)


print(fichero)
print(contenido)