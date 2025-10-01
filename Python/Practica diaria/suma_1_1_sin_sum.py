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