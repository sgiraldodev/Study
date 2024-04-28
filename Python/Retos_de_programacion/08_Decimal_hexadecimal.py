def decimal_a_hexadecimal(decimal):
    """
    Convierte un número decimal en su representación hexadecimal.

    Args:
        decimal (float): El número decimal a convertir.

    Returns:
        str: La representación hexadecimal del número decimal.
    """
    entero = int(decimal)
    fraccion = decimal - entero

    hexadecimal_entero = hex(entero)[2:]

    hexadecimal_fraccion = ""
    while fraccion:
        fraccion *= 16
        digit = int(fraccion)
        if digit < 10:
            hexadecimal_fraccion += str(digit)
        else:
            hexadecimal_fraccion += chr(ord('A') + digit - 10)
        fraccion -= digit
        if len(hexadecimal_fraccion) > 5:  # Limitar la precisión
            break

    return hexadecimal_entero + "." + hexadecimal_fraccion


# Solicitar al usuario un número decimal
numero = float(input("Ingrese un número decimal: "))

# Convertir el número a hexadecimal
hexadecimal = decimal_a_hexadecimal(numero)

# Imprimir el resultado
print("El número en hexadecimal es:", hexadecimal)