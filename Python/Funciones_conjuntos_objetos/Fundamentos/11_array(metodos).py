print("#" * 15)
print("Metodos usados para arrays")

print("#" * 15)
print("CRUD")


print("Crear array")
arrayNumbers = [2,4,1,3,5,6,9]
arrayNombres = ["Santiago", "Jessica"]
print(arrayNumbers)

print("Seleccionar posicion 3")
print(arrayNumbers[2])

print("Actualizar ultima posición por un 10")
arrayNumbers[-1] = 10
print(arrayNumbers)

print("Metodo append: agrega al final de la lista")
arrayNumbers.append(20)
print(arrayNumbers)

print("Metodo insert: agrega al en la posicion de la lista deseada, en este caso luego del 6.")
arrayNumbers.insert(6, 7)
print(arrayNumbers)

print("Fusionar varios arrays: Es concatenando con el +")
arrayNumbers = arrayNumbers + arrayNombres
print(arrayNumbers)

print("Metodo index: identifica la posición de un valor en un array. Para este caso identifique la palabra Santiago,  y se reemplaza por novio")
varPosicion = arrayNumbers.index('Santiago')
arrayNumbers[varPosicion] = "Novio"
print(arrayNumbers)

print("Metodo remove: identifica la posición de un valor en un array. Para este caso identifique la palabra Novio,  y lo elimina")
arrayNumbers.remove('Novio')
print(arrayNumbers)

print("Metodo pop: Elimina el ultimo elemento de la lista, en este caso Patricia. Tambien si se le indica la posición a borrar lo hace.")
arrayNumbers.pop()
arrayNumbers.pop(0)
print(arrayNumbers)

print("Metodo reverse: Cambia el orden del array.")
arrayNumbers.reverse()
print(arrayNumbers)

print("Metodo sort: Ordena los valores de un array tanto numericamente como strings. IMPORTANTE QUE SOLO APLICA PARA NUMEROS O STRINGS, PERO NO MEZCLADOS")
arrayNumbers.sort()
print(arrayNumbers)