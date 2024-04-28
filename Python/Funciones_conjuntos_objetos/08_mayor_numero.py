print("Implementa una función que reciba una lista de números y devuelva el número más grande.")
print('*' * 15)
print('\n')

numeros = input("Ingresa varios numeros separados por coma: ")
numeros = numeros.replace(" ", "")
numeros = numeros.split(",")
print(numeros)
print('\n')

listNumeros = [int(x) for x in numeros]
print(listNumeros)
print('\n')

mayorNumero = max(listNumeros) 
print(mayorNumero)



'''NOTA
La función split() es un método de las cadenas en Python, no de los números. 
Esta función divide una cadena en una lista donde cada palabra es un elemento de la lista.
Si intentas usar split() en un número, obtendrás un error porque los números no tienen este método. 
Puedes hacer uso de list(str(cadena)) para convertirlo en string y asi usar split.
O se puede hacer uso de un for para recorrer cada datos en general
'''

