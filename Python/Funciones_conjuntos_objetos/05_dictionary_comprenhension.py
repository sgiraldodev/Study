import json #Importar libreria para imprimir objetos(diccionarios) de forma ordenada
import random #Importar libreria para generar numeros aleatorios
import statistics # Libreria para calculos y promedios


print('Crear un objeto(diccionario) con una iteracion de numeros')
new_list_numbers = {}

for i in range(1, 11):
    new_list_numbers[i] = i * 3
print(json.dumps(new_list_numbers, indent=4))
print('\n')

print('Crear un objeto(diccionario) con una iteracion de numeros con list comprehension')
new_list_numbers2 = {i: i * 2 for i in range(1, 11)}
print(json.dumps(new_list_numbers2, indent=4))
print('\n')

print('Iterar una lista(array) y crear un objeto(diccionario)')
array_paises = ['Col', 'Arg', 'Per', 'Bra', 'Chi', 'Ecu', 'Uru', 'Par', 'Bol', 'Ven']
new_list_countries = {}

for id in array_paises:
	new_list_countries[id] = random.randint(1, 100)
print(json.dumps(new_list_countries, indent=4))
print('\n')

print('Iterar una lista(array) y crear un objeto(diccionario) con list comprehension')
new_list_countries2  ={id: random.randint(1, 100) for id in array_paises}
print(json.dumps(new_list_countries2, indent=4))
print('\n')

print('Iterar dos listas(array) y crear un objeto(diccionario) con list comprehension')
names=['Santiago', 'Jessica', 'Patricia']
edad=[30, 28, 60]

new_list_names = {names[i]: edad[i] for i in range(len(names))}
print(json.dumps(new_list_names, indent=4))
print('\n')

print('*' * 50)

print('Iterar objetos(diccionarios) y aplicar condiciones')
new_list_countries3 = ['col', 'arg', 'per', 'bra', 'chi', 'ecu', 'uru', 'par', 'bol', 'ven']
print(new_list_countries3)
print('\n')

print('Generar un numero de poblacion aleatorio para cada pais')
population = {num: random.randint(1, 50) for num in new_list_countries3}
print(json.dumps(population, indent=4))

print('\n')
print('Filtrar los paises que tengan una poblacion mayor a 20 millones')

list_may_20 = {pais: population[pais] for pais in population if population[pais] > 20}
print(json.dumps(list_may_20, indent=4))



