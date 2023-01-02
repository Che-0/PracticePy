"""este desmadre es una cuenta bancaria segun"""

from numpy import True_


class Persona:


    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):


    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance


    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.numero_cuenta}, {self.balance}"


    def depositar(self, x):
        self.balance += x


    def retirar(self, x):
        if x <= self.balance:
            self.balance -= x
        else:
            print("no tienes dinero")


def crear(nom, ape, cue, bal):
    return Cliente(nom, ape, cue, bal)


def inicio():
    print("Bienvenido, por favor ingresa los siguientes datos: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cuenta = (input("Numero de cuenta: "))
    balance = int(input("Balance: "))

    cliente1 = crear(nombre, apellido, cuenta, balance)
    print(cliente1)

    while True:
        print("""Que quieres hacer?
        1. Depositar
        2. Retirar
        3. Ver datos 
        4. Salir
        """)
        op = int(input("numero: "))

        if op == 1:
            dinero = int(input("Ingresa la cantidad: "))
            cliente1.depositar(dinero)
        elif op == 2:
            retiro = int(input("Ingresa la cantidad a retirar: "))
            cliente1.retirar(retiro)

        elif op == 3:
            print(f"los datos de tu cuenta son {cliente1}")

        elif op == 4:
            return False
inicio()

#pylint  37_Banco.py -r y