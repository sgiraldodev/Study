'''
Crea una clase llamada Coche que permita representar un carro con estas características:

Atributos:
marca
modelo
velocidad (inicialmente en 0)

Métodos:
acelerar() → aumenta la velocidad en 10.
frenar() → reduce la velocidad en 10 (sin bajar de 0).
mostrar_estado() → imprime la marca, modelo y velocidad actual.
'''

class Coche:
    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        print(f"Vehículo {self.marca} {self.modelo} con velocidad: {self.velocidad} km/h")

    def acelerar(self):
        self.velocidad += 10
        print(f"El vehículo {self.marca} {self.modelo} aceleró. Nueva velocidad: {self.velocidad} km/h")

    def frenar(self):
        if self.velocidad >= 10:
            self.velocidad -= 10
        else:
            self.velocidad = 0
        print(f"El vehículo {self.marca} {self.modelo} frenó. Nueva velocidad: {self.velocidad} km/h")

    def mostrar_estado(self):
        print(f"El vehículo {self.marca} {self.modelo} va a {self.velocidad} km/h")

# Prueba
mi_auto = Coche("Chevrolet", "Onix Turbo RS", 100)
mi_auto.acelerar()

#mi_auto.acelerar()
#mi_auto.frenar()
#mi_auto.mostrar_estado()
