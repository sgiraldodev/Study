import json
"""
Este archivo contiene ejemplos de ciclos en Python.

Los ciclos son estructuras de control que permiten repetir un bloque de código varias veces.
En Python, existen dos tipos de ciclos: el ciclo while y el ciclo for.

El ciclo while se ejecuta mientras se cumpla una condición. El bloque de código dentro del ciclo se repetirá
hasta que la condición sea falsa.

El ciclo for se utiliza para iterar sobre una secuencia de elementos, como una lista o una cadena de texto.
En cada iteración, el bloque de código dentro del ciclo se ejecuta con un elemento diferente de la secuencia.

Ambos ciclos son muy útiles para automatizar tareas repetitivas y realizar operaciones en conjunto con los elementos de una secuencia.

"""

# Código con ejemplos de ciclos en Python
# ...

print("Ejemplo de ciclo while para que termine hasta que se cumpla la condición")
print("*" * 15)
print("\n")

counter = 0
while counter < 10:
    counter += 1
    print(counter)
    
    
print("\n")
print("Romper el ciclo con break cuando sea 10")

counter2 = 0

while counter2 < 20:
    print(counter2)
    counter2 += 1
    
    if counter2 == 10:
        print("Se rompe el ciclo porque es 10")
        break   
    
print("\n")
print("Uso del continue para saltar el 10")

counter3 = 0
while counter3 < 20:
    counter3 += 1
    
    if counter3 == 10:
        print("Se salta el 10")
        continue
    
    print(counter3)

print("\n")
print('/' * 15)
print("Ciclo for")

print("El ciclo for hacer uso de la función range() para iterar sobre una secuencia de datos")
print("range(10) es una secuencia de 10 elementos, desde el 0 hasta el 9")
print("range(1, 11) es una secuencia de 10 elementos, desde el 1 hasta el 10")
print("range(1, 11, 2) es una secuencia de 5 elementos, desde el 1 hasta el 10, de 2 en 2")

for element in range(1, 11, 3): #element puede ser cualquier nombre
    print(element)

print("\n")

for i in range(1, 11):
    print(i)    

print("\n")
print("Recorrer una lista con un ciclo for")
print("La lista es: ")  
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

for i in lista:
    print(i)
    
print("\n")
print("recorrer un objeto diccionario con un ciclo for")

print("El objeto diccionario es: ") 
print("\n")
producto = {
    "nombre": "book",
    "quantity": 3,
    "price": 4.99
}
print(producto)

for key in producto:    
    print(key, '=>' ,producto[key])

print("\n")

print("Otra forma de recorrer un objeto diccionario con un ciclo for")
for key, value in producto.items():
    print(f"{key} => {value}")
    
#crea una lista de diccionarios de nombres y edades de personas
print("\n")
print("lista de diccionarios de nombres y edades de personas")
print("\n")
people = [
    {
        'name': 'Santiago',
        'age': 35,
        'email': 'santiago@example.com'
    },
    {
        'name': 'Luis',
        'age': 36,
        'email': 'luis@example.com'
    },
    {
        'name': 'Juan',
        'age': 37,
        'email': 'juan@example.com'
    },
    {
        'name': 'Pedro',
        'age': 38,
        'email': 'pedro@example.com'
    },
    {
        'name': 'Maria',
        'age': 39,
        'email': 'maria@example.com'
    }
]
print(json.dumps(people, indent=4))

for persona in people:
    print(f"Nombre:{persona['name']}")
    

print("\n")
print("reto platzi")
'''
En este desafío, se te proporcionará una lista de números llamada my_list. 
Tu tarea es recorrer esta lista y utilizar un ciclo para seleccionar solo los números positivos. 
Luego, debes agregar estos números a una nueva lista llamada new_list. 
Al final del ciclo, debes imprimir los valores contenidos en new_list utilizando la función print.

Por ejemplo, si la lista es [1, -1, 2, -2, 3, -3, 4, -4], 
después de realizar las operaciones descritas, 
la lista new_list debería contener solo los números positivos, es decir, [1, 2, 3, 4].
'''
my_list = [1,-1,2,-2,3,-3,4,-4]
new_list = []
print(my_list)
# Escribe tu solución 👇

print("\n")
print("Solucion estable")
for i in my_list:
    if i > 0:
        new_list.append(i)
        
print(new_list)


print("\n")
print("Solucion optimizada")
my_list = [1,-1,2,-2,3,-3,4,-4]
new_list = [num for num in my_list if num > 0]
print(new_list)

print("\n")
print("for anidado")
print("\n")
print("Creamos una lista de listas")

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(matriz)


print("Recorremos la lista de listas con un for anidado")
for fila in matriz:
    print(f"fila => {fila}")
    for columna in fila:
        print(f"columna => {columna}")