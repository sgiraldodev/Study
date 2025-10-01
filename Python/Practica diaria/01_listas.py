print('1. Crea una diccionario que reciba una lista de números y devuelva la suma de todos los elementos.')
print('*' * 50)
print('\n')


#Solicitar al usuario que ingrese una lista de números
entrada_usuario = input("Ingrese una lista de números separados por comas: ")
# Convertir la entrada del usuario en una lista de números
lista = [int(numero) for numero in entrada_usuario.split(",")]
# Inicializar un diccionario vacío
diccionario = {}
# Calcular la suma de todos los elementos de la lista
suma = sum(lista)
# Agregar la suma al diccionario
diccionario['suma'] = suma
# Imprimir el diccionario
print(diccionario)
print('\n')