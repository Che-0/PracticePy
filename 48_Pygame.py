from multiprocessing import parent_process
import pygame

#esta madre se parece a tkinter respecto a lo de las 
#ventanas


pygame.init()   # <-- inicializamos 


#tamaño  de ventana

pantalla = pygame.display.set_mode((800,600))  #modo en el que se muestra la pantalla (alto,ancho)

se_ejecuta = True


# esto lo mantiene en bucle para que no se cierre de putazo 
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

# pygame esta basado en acciones ( eventos )
# asi que por eso mismo checamo en todo momento que tipo de eventos han transcurrido
# con el ciclo while y el ciclo for
# for almacena en evento cualquier accion realizada y la pasa como argumento al if
# para hacer posteriormente la comparacion, QUIT es el evento de presiomar el tache
# para cerrar la ventana, cuando esto pasa el programa termina 

