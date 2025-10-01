def decimal_a_binario_complemento_a2(decimal):
    entero = int(decimal)
    fraccion = abs(decimal - entero)

    binario_entero = bin(abs(entero))[2:]
    if decimal < 0:  # Solo tomar el complemento a dos si el número es negativo
        binario_entero = ''.join('1' if bit == '0' else '0' for bit in binario_entero)  # Complemento a uno
        binario_entero = bin(int(binario_entero, 2) + 1)[2:]  # Complemento a dos

    binario_fraccion = ""
    while fraccion:
        fraccion *= 2
        if fraccion >= 1:
            binario_fraccion += '1'
            fraccion -= 1
        else:
            binario_fraccion += '0'
        if len(binario_fraccion) > 10:  # Limitar la precisión
            break

    return binario_entero + "." + binario_fraccion


# Solicitar al usuario un número decimal
numero = float(input("Ingrese un número decimal: "))

# Convertir el número a binario en complemento a dos
binario = decimal_a_binario_complemento_a2(numero)

# Imprimir el resultado
print("El número en binario en complemento a dos es:", binario)