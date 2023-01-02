#Bueno, este pedo tienen bastantes usos en realidad
#para  identificar un formato, asi se podria decir, creo 

### Caracteres especiales ###   

# /d    digito numerico 
# /w    alfanumeriico
# /s    espacion en blanco  

#cuando estan en mayusculas es lo contrario 

# /D    NO digitos numerico 
# /W    No alfanumeriico
# /S    No espacion en blanco  


### cuantificadores ### 

#  +    aparece 2 o mas veces  
# {n}   se repite d{n} veces
# {n,m}  se repite de n a m veces \w{2,5}
# {n}    desde n hacia arriba d{n,}
# *      0 o mas veces 
# ?      aparece 1 o 0    


from cmath import pi
import re 

texto = "Si necesitasa ayuda ps ayuda"

patron = "ayuda"

#busqueda  = re.search(patron,texto)  <- solo te da el primer resultado, pero 
#si hay mas de uno no te los devuelve, SOLO EL PRIMERO 

busqueda  = re.findall(patron,texto)   #<--- encuentra todas las apariciones
print(busqueda)

#para acceder a cada elemento

for hallazgo in re.finditer(patron, texto):     #<- en una iteracion 
    print(hallazgo.span()) 