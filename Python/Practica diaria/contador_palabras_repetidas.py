'''
Escribe una función en Python llamada contar_palabras que reciba un texto y devuelva un diccionario con cada palabra y cuántas veces aparece.

Ej
texto = "Hola mundo hola Python mundo mundo"
print(contar_palabras(texto))

Salida esperada
{'hola': 2, 'mundo': 3, 'python': 1}
print('Generar un numero de poblacion aleatorio para cada pais')
population = {num: random.randint(1, 50) for num in new_list_countries3}

print('Iterar dos listas(array) y crear un objeto(diccionario) con list comprehension')
names=['Santiago', 'Jessica', 'Patricia']
edad=[30, 28, 60]

new_list_names = {names[i]: edad[i] for i in range(len(names))}
print(json.dumps(new_list_names, indent=4))
print('\n')

'''

def contar_palabras(palabra:str) -> set:
    palabra = palabra.split(' ')
    palabra = list(palabra)
    return palabra


frase = str(input("Ingrese la frase: "))
diccionario = contar_palabras(frase)
print(diccionario)