from builtins import bin

def binario_a_hexadecimal_complemento_a2(binario):
    mapeo_bin_hex = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

    es_negativo = binario[0] == '-'
    binario = binario.lstrip('-')

    if '.' in binario:
        entero, fraccion = binario.split('.')
    else:
        entero = binario
        fraccion = ''

    if es_negativo:
        entero = ''.join('1' if bit == '0' else '0' for bit in entero)  # Complemento a uno
        entero = bin(int(entero, 2) + 1)[2:]  # Complemento a dos

    hexadecimal_entero = ''.join(mapeo_bin_hex[entero[i:i+4]] for i in range(0, len(entero), 4))

    fraccion += '0' * ((4 - len(fraccion) % 4) % 4)  # Añadir ceros al final si es necesario
    hexadecimal_fraccion = ''.join(mapeo_bin_hex[fraccion[i:i+4]] for i in range(0, len(fraccion), 4))

    return ("-" if es_negativo else '') + hexadecimal_entero + ("." + hexadecimal_fraccion if fraccion else '')

# Solicitar al usuario un número binario
numero = input("Ingrese un número binario: ")

# Convertir el número a hexadecimal
hexadecimal = binario_a_hexadecimal_complemento_a2(numero)

# Imprimir el resultado
print("El número en hexadecimal es:", hexadecimal)