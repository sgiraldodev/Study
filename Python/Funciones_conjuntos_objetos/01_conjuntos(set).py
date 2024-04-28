'''
Los sets en Python son una estructura de datos usada para almacenar elementos de una 
manera similar a las listas(arrays), pero con ciertas diferencias.

Los elementos de un set son únicos, lo que significa que no puede haber elementos duplicados.

Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.
Sus elementos deben ser inmutables.
Para crear un set en Python se puede hacer con set() y pasando como entrada 
cualquier tipo iterable, como puede ser una lista. 
Se puede ver como a pesar de pasar elementos duplicados como dos 8 y 
en un orden determinado, al imprimir el set no conserva ese orden
y los duplicados se han eliminado.

'''

print('Ejemplo 1: Crear un conjunto de Paises en Python')
print('*'*50)

set_countries = {'Colombia', 'Peru', 'Argentina', 'Chile', 'Colombia', 'Peru', 'Argentina', 'Chile'}
print(set_countries)
print(type(set_countries))

print('\n')
print('Crear un conjunto de varios tipos de datos')
print('*'*50)

set_types = {1, 2, True, False, 'Hola', 3.1416, 1, 2, True, False, 'Hola', 3.1416}
print(set_types) 
print(type(set_types))

print('\n')
print('Crear un conjunto a partir del string Hooola')
print('*'*50)

set_string = set('Hooola') #No se duplica
print(set_string)
print(type(set_string))

print('\n')
print('Crear un conjunto a partir de una Tupla')
print('*'*50)

set_tuple = set((1, 1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(set_tuple)
print(type(set_tuple))

print('\n')
print('Crear un conjunto a partir de una lista(ARRAY)')
print('*'*50)

set_numbers = set([1, 1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
print(set_numbers)
print(type(set_numbers))

print('\n')
print('Convertir un conjunto a una lista')
print('*'*50)

lista_numbers = list(set_numbers)   
print(lista_numbers)
print(type(lista_numbers))


