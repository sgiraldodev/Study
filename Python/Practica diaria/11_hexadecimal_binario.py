def hexadecimal_a_binario_complemento_a2(hexadecimal):
    mapeo_hex_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    es_negativo = hexadecimal[0] == '-'
    hexadecimal = hexadecimal.lstrip('-')

    if '.' in hexadecimal:
        entero, fraccion = hexadecimal.split('.')
    else:
        entero = hexadecimal
        fraccion = ''

    binario_entero = ''.join(mapeo_hex_bin[digito] for digito in entero)

    if es_negativo:
        binario_entero = ''.join('1' if bit == '0' else '0' for bit in binario_entero)  # Complemento a uno
        binario_entero = bin(int(binario_entero, 2) + 1)[2:]  # Complemento a dos

    binario_fraccion = ''.join(mapeo_hex_bin[digito] for digito in fraccion)

    return binario_entero + ("." + binario_fraccion if fraccion else '')

# Solicitar al usuario un número hexadecimal
numero = input("Ingrese un número hexadecimal: ")

# Convertir el número a binario en complemento a dos
binario = hexadecimal_a_binario_complemento_a2(numero)

# Imprimir el resultado
print("El número en binario en complemento a dos es:", binario)