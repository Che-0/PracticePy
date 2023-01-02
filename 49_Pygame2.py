from turtle import distance
from numpy import mat
import pygame
import random
import math

pygame.init()   # <-- inicializamos 

pantalla = pygame.display.set_mode((800,600))  #modo en el que se muestra la pantalla (alto,ancho)
#para ubibar objetos tenemos que tener en cuenta es, es practicamente el plano

#  _ __ __ __ __ __ x
#  |
#  |
#  | 
#  |
#  |
#  y

#Titulo e icono
pygame.display.set_caption("Invasion Espacial")   # Titulo
icono = pygame.image.load("49_Pygame2.png")       # asiganamos png a var
pygame.display.set_icon(icono)                    # cambiamos icono 32 pixeles de preferencia

# Jugador
img_jugador = pygame.image.load('49_Nave.png')    # asignamos a var  64 px esa utilice
#establecemos su posicion x y
jugador_x = 336      # la mita es 400 pero le restamos los 64 de la img y da 336 
jugador_y = 500      # 600 - 64 =  536
jugador_x_cambio =0


# enemigo
img_enemigo = []    # asignamos a var  64 px esa utilice
#establecemos su posicion x y
enemigo_x = []       
enemigo_y = []      
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append( pygame.image.load('49_Alien.png'))    # asignamos a var  64 px esa utilice
    #establecemos su posicion x y
    enemigo_x.append(random.randint(0,700))      
    enemigo_y.append(random.randint(50,200))      
    enemigo_x_cambio.append(.5)
    enemigo_y_cambio.append(50)


#bala
bala = pygame.image.load('49_Bala.png')    # asignamos a var  64 px esa utilice
#establecemos su posicion x y
bala_x = 0       
bala_y = 500     
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False


fondo = pygame.image.load("49_Fondo.jpg")

# txt final de game
furnte_final = pygame.font.Font("freesansbold.ttf",40)

def texto_final():
    mi_fuente_final = fuente.render("GAME OVER", True,(255,255,255))
    pantalla.blit(mi_fuente_final,(60,200))



#puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf",32)  #pide dos val name de fuente y tamaño 
texto_x = 10 
texto_y = 10 

#fun mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje:  {puntaje}", True ,(255,255,255))   #imprimir  txt y algo y rgb
    pantalla.blit(texto,(x,y))

#funcion jugador
def jugador(x,y): 
                     #img       tupla de ancho y alto   (x,y)
    pantalla.blit(img_jugador, (x,y))   # blit es arrojar , lo arroja a la pantalla , algo asi 

#funcion enemigo
def enemigo(x,y,ene): 
                     #img       tupla de ancho y alto   (x,y)
    pantalla.blit(img_enemigo[ene], (x,y))   # blit es arrojar , lo arroja a la pantalla , algo asi 


#disparar bala 
def disparar(x,y):
    global bala_visible
    bala_visible = True

    pantalla.blit(bala,(x+16,y+10))

#colision
def colision(x_1,y_1,x_2,y_2):

    distancia = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_2-y_1,2))
    if distancia < 27:
        return True
    else:
        return False

#loop del juego
se_ejecuta = True
while se_ejecuta:
    
    #pantalla.fill((153,0,153))                  # En formato RGB
#    jugador_x += .1                     #que aumente en cada iteracion .1 px


    #imagen fondo
    pantalla.blit(fondo,(0,0)) #ubicacion

    for evento in pygame.event.get():           # Acccion salida
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:       # reconoce cualquier tecla apretada
            if evento.key == pygame.K_LEFT:
                #print("flecha izquierda presionada") 
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                #print("flecha derecha presionada")
                jugador_x_cambio = +1
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar(bala_x,bala_y)
        
        if evento.type == pygame.KEYUP:         # suelta el boton (deja de presionar)
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                #print("La flecha fue soltada")
                jugador_x_cambio = 0

        
 
    jugador_x += jugador_x_cambio    #actualiza pos de x

    #mantener en el margen        (no tiene que pasar de -1)
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x  >= 700:                     # 800 -64  = 736
        jugador_x = 700                        # este es derecha


#   Enemigo
    for e in range(cantidad_enemigos):

        #fin
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]=1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]    #actualiza pos de x

        #mantener en el margen al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 700:                     
            enemigo_x_cambio[e] = -1       
            enemigo_y[e] += enemigo_y_cambio[e]

        #verifi colision
        colisionn = colision(enemigo_x[e],enemigo_y[e],bala_x,bala_y)
        if colisionn:
            bala_y = 500
            bala_visible = False
            puntaje +=1 
            #print(puntaje)
            enemigo_x[e] = random.randint(0,700)       
            enemigo_y[e] = random.randint(50,200) 

        
        enemigo(enemigo_x[e],enemigo_y[e],e)

    #movimiento bala
    if bala_y <= -64:
        bala_y =500
        bala_visible = False
    
    if bala_visible:
        disparar(bala_x,bala_y)
        bala_y -= bala_y_cambio 


    #primero se pinta la pantalla y despues el personaje o quedaria tapado
    jugador(jugador_x,jugador_y)

    mostrar_puntaje(texto_x,texto_y)

    pygame.display.update( )                    #se tiene que hacer el update para aplicar changes