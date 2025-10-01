# Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es negativo
if numero < 0:
    es_negativo = True
    numero = abs(numero)
else:
    es_negativo = False

# Inicializar la cadena binaria
binario = ""

# Convertir el número a binario
while numero > 0:
    residuo = numero % 2
    binario = str(residuo) + binario
    numero = numero // 2

# Agregar el signo negativo si es necesario
if es_negativo:
    binario = "-" + binario

# Imprimir el resultado
print("El número en binario es:", binario)
