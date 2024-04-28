import random
import json

print('Crear un diccionario a partir de una lista(array) sin dictionary coprenhension')
print('*' * 50)
print('\n')

discosVendidosSlayerAno = [2000, 2001, 2005, 2006]
ventas = {}
for cantidad in discosVendidosSlayerAno:
    ventas[cantidad] = random.randint(1, 1000000)

print(json.dumps(ventas, indent= 4 ))

print('Forma con dictionary comprenhension')
ventasV2 = {cant:random.randint(1, 100000) for cant in discosVendidosSlayerAno}
print(ventasV2)
print('\n')

print('Iterar un diccionario con los numeros del 1 al 10')
print('*' * 50)
print('\n')
numeros = {}
for i in range(1, 10):
    numeros[i] = i * 2
print(numeros)
print('\n')

print('Iterar un diccionario con los numeros del 1 al 10 usando dictionary comprenhension')
print('*' * 50)
print('\n')
numeros = {i: i*2 for i in range(1, 10)}
print(numeros)
print('\n')

print('Invertir claves y valores en un diccionario')
print('*' * 50)
print('\n')
diccionario = {"a": 1, "b": 2, "c": 3}
print(json.dumps(diccionario, indent=4))
invertido = {key: value for value, key in diccionario.items()}
print(json.dumps(invertido, indent=4))

print('\n')
print('Recorrer dos listas  y crear un diccionario a partir de su iteracion')
print('*' * 50)

nombres = ['santiago', 'jhoana', 'sara']
edades = [22, 23, 24]
print(f'nombres: {nombres}')
print(f'edades: {edades}')
print(f'Union haciendo uso de list  y zip {list(zip(nombres, edades))}') # con zip, podemos unir varias listas, en una sola que almacena tuplas

#comprenhension
personas ={nombre: edad for nombre, edad in zip(nombres, edades)}
print(json.dumps(personas, indent=4))
print('\n')


'''
Filtrar elementos en un diccionario: Dado el siguiente diccionario, crea un nuevo diccionario que solo contenga los elementos cuyo valor sea mayor que 2.
'''
print('Filtrar elementos en un diccionario: Dado el siguiente diccionario, crea un nuevo diccionario que solo contenga los elementos cuyo valor sea mayor que 2.')
diccionario2 = {"a": 1, "b": 2, "c": 3, "d": 4}
print(json.dumps(diccionario2, indent=4))
mayor2= {a: b for a, b in diccionario2.items() if b > 2 }
print(json.dumps(mayor2, indent=4))
print('\n')

'''
Contar la frecuencia de los elementos en una lista: Dada la siguiente lista, crea un diccionario que cuente la frecuencia de cada elemento en la lista.
lista = ["a", "b", "a", "c", "b", "a", "d"]
'''
print('Dada la siguiente lista, crea un diccionario que cuente la frecuencia de cada elemento en la lista.')
lista = ["a", "b", "a", "c", "b", "a", "d"]
print(lista)

contador = {i:lista.count(i) for i in lista}
print(json.dumps(contador, indent=4))

print('\n')
print('Crear un diccionario de cuadrados: Crea un diccionario donde las claves sean los números del 1 al 5 y los valores sean los cuadrados de las claves.')
cuadrados = {num : num ** 2 for num in range(1, 6)}
print(json.dumps(cuadrados, indent=4))

print('\n')
print('Multiplicar por 2 una lista de numeros')
numerosPorDos = [2, 4, 6, 8]
resultadoNumeroPorDos = [i * 2 for i in numerosPorDos]
print (resultadoNumeroPorDos)


