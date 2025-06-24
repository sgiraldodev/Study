import random #Libreria para generar numeros aleatorios
import colorama #Libreria para dar color a la consola


from colorama import Fore, Back, Style, init #Instanciamos los atributos necesarios para dar color a la consola

init()  # Inicializa Colorama

print(Fore.CYAN + ".")

print("*" * 150)
print("Juego de Picas y Fijas en Python")
print("Desarrollado por Santiago Giraldo Aristizabal CC:1053786121")
print("sgiraldodevs@gmail.com")
print("*" * 150)
print("REGLAS DEL JUEGO")
reglasJuego = """
Un dígito es PICA cuando aparece en el número CLAVE generado, pero en una posición diferente a la del número del intento, 
Un dígito es una FIJA cuando está en el número CLAVE en la misma posición del número del intento). 
"""
print(reglasJuego)
#print(Style.RESET_ALL + "Restablecer estilo")


#variales
numero_minimo = 1000
numero_maximo = 9999
numero_de_intentos = 12
numero_aleatorio = 0
ciclo_actual = 0
numero_jugador = 0
tupla_numero_digitado  = 0
tupla_numero_sistema  = 0


#funcion para genenerar un numero aletario de 4 digitos
def generar_numero_aleatorio():
    return random.randint(numero_minimo,numero_maximo)

#funcion para convertir el numero en una tupla para poder realizar operaciones sobre cada digito.
def conversion_tupla(numero):
    return tuple(int(digito) for digito in str(numero))

def validar_numero_fijas(tupla_sistema, tupla_usuario):
    fijas = 0
    i = 0
    for digito in tupla_sistema:
        if digito == tupla_usuario[i]:
            fijas += 1        
        i += 1  # Incrementar el contador manualmente
    print(f"Tienes {fijas} fijas")
    return fijas

def validar_numero_picas(tupla_sistema, tupla_usuario, numero_fijas):
    picas = 0
    for digito in tupla_usuario:
        if digito in tupla_sistema:
            picas += 1
    picas -=numero_fijas        
    print(f"Tienes {picas} picas")
    return picas

print(Fore.BLUE + f"Número de intentos permitidos: {numero_de_intentos}")

#Invocamos la funcion para crear el numero aleatorio y asignamos a una variable el resultado
numero_aleatorio = generar_numero_aleatorio()
print(f"Número a adivinar: ????") 


#Empezamos a hacer una iteración que es el numero maximo de intentos para el jugador
for i in range(0, numero_de_intentos):

    #Solicitamos que el usuario ingrese el numero que va a adivinar.
    ciclo_actual = i + 1
    print(f"Intento numero: {ciclo_actual}, te restan {numero_de_intentos - ciclo_actual}")
    print('\n')
    numero_jugador = (int(input(f"Adivina el numero de 4 cifras entre {numero_minimo} y {numero_maximo}:")))
   
    if numero_jugador < numero_minimo or numero_jugador > numero_maximo:
      print(Fore.RED + f"El numero ingresado debe estár entre el rango de {numero_minimo} y {numero_maximo}. Vuelve a intentarlo")
      break

    print(f"Número digitado en el intento  {[i + 1]}: {numero_jugador}")
    
    #Hacemos una validacion inicial de si el numero ingresado por el jugador corresponde al generado
    if (numero_aleatorio == numero_jugador):    
        if ciclo_actual <= 2:
            print(Fore.GREEN + "!!!!!!!!!!Excelente, eres un maestro y estas fuera del alcance de los demás!!!!!!!!!!!!!! GANASTE!!!!")        
            break
        elif ciclo_actual >2 and ciclo_actual <= 4:
            print(Fore.GREEN + "!!!!!!!!!!Muy bueno, puedes ser un gran competidor!!!!!!!!!!!!!! GANASTE!!!!")
            break        
        elif ciclo_actual >4 and ciclo_actual <= 8:
            print(Fore.GREEN + "!!!!!!!!!!Bien, estas progresando debes romper tus límites!!!!!!!!!!!!! GANASTE!!!!")  
            break      
        elif ciclo_actual >8 and ciclo_actual <= 9:
            print(Fore.GREEN + "!!!!!!!!!Regular, Aún es largo el camino por recorrer!!!!!!!!!!!!! GANASTE!!!!")  
            break      
        else:
            print(Fore.GREEN + "!!!!!!!!!Mal, este juego no es para ti")
            print(f"Número a adivinar: {numero_aleatorio}") 
            break
    else:
        #Convertimos a tuplas los numeros ingresados por el usuario y generados por el sistema
        tupla_numero_digitado = conversion_tupla(numero_jugador)
        #print(f"Conversión a Tupla numero digitado:{tupla_numero_digitado}")
        
        tupla_numero_sistema = conversion_tupla(numero_aleatorio)
        #print(f"Conversión a Tupla numero del sistema:{tupla_numero_sistema}")       
       
        #Invocamos función que se encarga de identificar el numero de picas
        numero_fijas = validar_numero_fijas(tupla_numero_sistema, tupla_numero_digitado)
        numero_picas = validar_numero_picas(tupla_numero_sistema, tupla_numero_digitado, numero_fijas)
        print(f"Tienes un total de {numero_fijas} fijas y {numero_picas} picas. ¡Sigue intentandolo!")
        
print(f"Número adivinado: {numero_aleatorio}")        
print(Fore.LIGHTRED_EX + "Fin del Juego..............")