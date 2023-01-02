
class Pajaro:

    alas = True 

    def __init__(self,color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("estoy piando")


#metodo de instancia, puede alterar toda la clase 
#necesita como primer parametro obligatorio self
    def volar(self,metros):
        print(f"El pajaro volo {metros} metros")

#metodo de clase 
# se necesita el decorador @ y classmethod y el argumento cls
#@classmethod

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huvos")


# Esto es para no hacer ningun cambio a un objeto
#una funcion 
    @staticmethod
    def mirar():
        print("el puto pajaro mira")

Pajaro.poner_huevos(5)
Pajaro.mirar()
#pajaro1 = Pajaro("rojo","perico")
#pajaro1.piar()
#pajaro1.volar(20)