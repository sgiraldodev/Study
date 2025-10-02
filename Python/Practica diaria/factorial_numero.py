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