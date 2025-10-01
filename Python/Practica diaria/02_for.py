
print('2. Escribe un programa que solicite al usuario una frase y cuente cuántas veces aparece cada palabra en la frase.')
print('*' * 50)
print('\n')

# Solicitar al usuario que ingrese una frase
frase = input("Por favor, ingrese una frase: ")
# Dividir la frase en palabras
palabras = frase.split()
# Crear un diccionario vacío para almacenar las palabras y sus recuentos
recuentos = {}
# Para cada palabra en la lista de palabras
for palabra in palabras:
    # Si la palabra ya está en el diccionario, incrementar su recuento
    if palabra in recuentos:
        recuentos[palabra] += 1
    # Si la palabra no está en el diccionario, agregarla con un recuento de 1
    else:
        recuentos[palabra] = 1

# Imprimir el diccionario, que contiene las palabras y sus recuentos
print(recuentos)