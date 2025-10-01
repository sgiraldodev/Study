def hexadecimal_a_decimal(hexadecimal):
    signo = -1 if hexadecimal[0] == '-' else 1
    hexadecimal = hexadecimal.lstrip('-')

    try:
        entero, fraccion = hexadecimal.split('.')
    except ValueError:
        entero = hexadecimal
        fraccion = '0'

    decimal_entero = int(entero, 16)

    decimal_fraccion = 0
    for i in range(len(fraccion)):
        decimal_fraccion += int(fraccion[i], 16) / (16 ** (i + 1))

    return signo * (decimal_entero + decimal_fraccion)


# Solicitar al usuario un número hexadecimal
numero = input("Ingrese un número hexadecimal: ")

# Convertir el número a decimal
decimal = hexadecimal_a_decimal(numero)

# Imprimir el resultado
print("El número en decimal es:", decimal)