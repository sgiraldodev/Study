import statistics

print('Escribe un programa que solicite al usuario una lista de números y calcule el promedio de los números ingresados.')
print('*' * 50)
print('\n')

#Recibir los numeros a promediar
numeros = input('Digite los numeros a promediar separados por coma: ')
numeros = numeros.replace(' ', '')
numeros = numeros.split(',')
print(f'lista con los valores tipo string {numeros}')

#convertir la lista de string a int para poder usar la libreria statics
numeros = [int(numero) for numero in numeros]
print(f'lista con los valores ya convertidos a int{numeros}')

promedio = statistics.mean(numeros)
print(f'El promedio del los numeros ingrsados es: {promedio}')
