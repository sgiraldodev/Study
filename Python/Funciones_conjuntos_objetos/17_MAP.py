'''
La función map() en Python es una función de orden superior que toma una función y un iterable (como una lista, tupla, etc.) 
como argumentos, y devuelve un objeto map que es un iterable resultado de aplicar la función proporcionada a cada elemento del iterable dado

Por lo tanto, la función map() es útil cuando quieres aplicar una función a cada elemento de un iterable y obtener un nuevo iterable con los resultados.
'''


print('\n')
print('Multiplicar por 2 una lista de numeros para transformar cada elemento de manera tradicional')
print('*' * 50)

lista = [2, 4, 6, 8, 10]
multiplicacion = [i * 2 for i in lista]
print(f'Lista inicial {lista}')
print(f'Lista transformada {multiplicacion}')

print('\n')
print('Multiplicar por 2 una lista de numeros para transformar cada elemento con MAP y lamnda')
print('*' * 50)

multiplicacionMAP = list(map(lambda i: i * 2, lista))
print(f'Lista inicial {lista}')
print(f'Lista transformada {multiplicacionMAP}')

print('\n')
print('Multiplicar por su cuadraro una lista de numeros con MAP y una funcion normal')
print('*' * 50)

def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = map(cuadrado, numeros)
print(list(cuadrados))


print('\n')
print('Sumar los valores de dos listas diferentes usando MAP')
print('*' * 50)

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7]


sumandoListas = list(map(lambda var1, var2: var1 + var2, lista1, lista2))
print(f'Lista 1 = {lista1}')
print(f'Lista 2 = {lista2}')
print(f'Resultado = {sumandoListas}')
