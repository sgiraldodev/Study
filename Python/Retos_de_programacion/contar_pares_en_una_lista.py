'''
Contar pares en una lista
Dada una lista de enteros, devuelve cuántos son pares.
'''

lista_enteros = [1, 3, 5, 6, 8, 11, 15, 16, 13, 90, 98, 66, 78]
print(type(lista_enteros))

contador = 0
impares = 0

for i in lista_enteros:
    if i % 2 == 0:
        contador += 1
    else:
        impares += 1

print(f'El numero de pares en la lista es de {contador} y de impares es {impares}')