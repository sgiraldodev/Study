print('List Comprehension es una forma de optimizar el codigo y hacerlo mas legible')
print('\n')
print('Estrucutra de un list comprehension: # lista = [expresión for elemento in iterable] / cuadrados = [i**2 for i in range(5)]')

print('\n')
print('Estrucutra de un list comprehension cuando tiene un condicional: # lista = [expresión for elemento in iterable if condición]')
'''
Por lo tanto la expresión sólo se aplicará al elemento si se cumple la condición. 
Veamos un ejemplo con una frase, de la que queremos saber el número de erres que tiene.

frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
#['r', 'r', 'r', 'r']
'''


print('\n')
print('Forma 1:Crear una lista de numeros y recorrerla con un for manera tradicional')
array_numbers = [1,2,3,4,5,6,7,8,9,10]
for i in array_numbers:
    print(i)


print('\n')
print('Forma 2: Crear una lista en base a un range y recorrerla con un for')
array_numbers_2 = []
for j in range(1,11):
    array_numbers_2.append(j)
    
print(array_numbers_2)

print('\n')
print('Forma 3: Crear una lista con list comprehension')
array_numbers_3 = [lista for lista in range(1,11)]
print(array_numbers_3)


print('\n')
print('Operaciones dentro de los list comprehension: Multiplicar por 2 los numeros de la lista')
array_numbers5 = [pares * 2 for pares in range(1, 13)]
print(array_numbers5)




print('\n')
print('Condiciones dentro de los list comprehension: Identificar los numeros pares FORMA CLASICA')
array_numbers6_clasica = []
for pares_c in range(1, 13):
    if pares_c % 2 == 0:
        print('Es par')
        array_numbers6_clasica.append(pares_c)	
print(array_numbers6_clasica)


print('\n')
print('Condiciones dentro de los list comprehension: Identificar los numeros pares FORMA OPTIMIZADA')
array_numbers6_list = [pares_l for pares_l in range(1, 13) if pares_l % 2 == 0]
print(array_numbers6_list)     



