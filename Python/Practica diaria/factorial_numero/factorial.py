    
'''
for i in range(5):          # 0..4
    print(i)

for i in range(1, 6):       # 1..5
    print(i)

for i in range(10, 0, -2):  # 10,8,6,4,2
    print(i)

for i in range(1, 10, 4):  # 10,8,6,4,2
    print(i)

Seis ejercicios para practicar (con for)

Contador simple
Escribe una función que imprima los números del 1 al n en una sola línea separados por espacios.

Suma 1..n
Calcula y devuelve la suma de 1 a n usando un for (sin sum).

Factorial (iterativo)
Repite el ejercicio del factorial con for (si n=0, devuelve 1).



Contar vocales en un texto
Dado un string, cuenta cuántas vocales (a,e,i,o,u, mayúsculas/minúsculas) contiene.

Tabla de multiplicar
Dado un entero n, imprime su tabla de multiplicar del 1 al 10 (formato n x i = resultado).
'''
#Forma mas pro Contador simple
'''
def numeros(num: int) -> None:
    if num < 1:
        print("El número debe ser mayor a 0")
        return
    print(" ".join(str(i) for i in range(1, num + 1)))

numero = int(input('Digite un numero: '))
numeros(numero)

#Forma normal Contador simple
def numeros(num: int) -> None:
    if num < 1:
        print("El número debe ser mayor a 0")
        return
    for i in range(1, num + 1):
        print(i, end = ' ')
        
    

numero = int(input('Digite un numero: '))
numeros(numero)
'''

'''
#Suma 1..n
#Calcula y devuelve la suma de 1 a n usando un for (sin sum).

def suma_numeros(num:int) -> None:
    if num < 1:
        print('El número no puede ser negativo')
    contador = 0
    for i in range(1, num + 1):
        contador += i
        
    print(f'La suma de los numeros es {contador}')

numero = int(input('Digita un numero para realizar la suma: '))
suma_numeros(numero)
'''

#Factorial (iterativo)
#Repite el ejercicio del factorial con for (si n=0, devuelve 1).

def factorial(num:int) -> None:
    if num == 0:
        return 1
    elif num < 1:
        print('El numero no puede ser negativo')
    else:
        operacion = 1
        for i in range(num, 0, -1):
            operacion *= i
        
    print(f'El factorial es {operacion}')

numero = int(input('Digita un numero para realizar el factorial: '))
factorial(numero)