import random #Libreria para generar numeros aleatorios
import colorama #Libreria para dar color a la consola
import time


from colorama import Fore, Back, Style, init #Instanciamos los atributos necesarios para dar color a la consola

init()  # Inicializa Colorama

print(Fore.CYAN + ".")

print("*" * 150)
print("Juego Memoria con números en Python")
print("Desarrollado por Santiago Giraldo Aristizabal CC:1053786121")
print("sgiraldodevs@gmail.com")
print("*" * 150)
print("REGLAS DEL JUEGO")
reglasJuego = """
Mira con atención el numero que aparecerá en pantalla. Al borrarse digitalo. Si aciertas, continúa con el siguiente número. 
"""
print(reglasJuego)

numero_a_generar = 0 #Valor inicial del rango numerico
tiempo = 8
vigente = True


#funcion para genenerar un numero aletario de 4 digitos
def generar_numero_aleatorio(numero_a_generar):
        return random.randint(0,numero_a_generar)

def imprimir_enter(n):
    for _ in range(n):
        print()

def contador_segundos(duracion, numero_a_recordar):
    
    print(f"Mira con atención el siguiente número: {numero_a_recordar}")
    
    for i in range(duracion, 0, -1):
        print(f"Tiempo restante: {i} segundos", end='\r')
        time.sleep(1)
        
    # Ejemplo de uso: imprimir 10 líneas en blanco
    imprimir_enter(100)
    print("¡Tiempo terminado!")
    
    
numero_a_recordar = generar_numero_aleatorio(100000)
contador_segundos(tiempo, numero_a_recordar)

numero_digitado = (int(input("Digita el número mostrado:")))
while vigente:
    if numero_digitado == numero_a_recordar:
        print("Bien hecho, tienes una buena memoria")
        nuevo_numero =  numero_a_recordar * 100
        numero_a_recordar = generar_numero_aleatorio(nuevo_numero)
        contador_segundos(tiempo, numero_a_recordar)
        numero_digitado = int(input("Digita el número mostrado: "))
    else:
        print("Número incorrecto. Fin del juego.")
        vigente = False

