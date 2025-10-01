print("#" * 15)
print("Las tuplas  son listas(arrays) inmutables, los cuales luego de creados no pueden ser modificados. Sirven mas como una estructura de lectura")
print("A diferencia de las listas(ARRAYS)  no se usa [], sino ()")
print('\n')

print("Crear Tupla")
tupla_list = ('Santiago', 'Jessica')
print(tupla_list)
print(type(tupla_list))
print('\n')

print("Las tuplas son inmutales y no se pueden modificar, descomentar el eje")
#tupla_list[0] = "Juan"
#print(tupla_list)
print('\n')


print("Para transformar una tupla a una lista(ARRAY) normal, basta con usar la función list, con eso se puede agregar lo requerido")
tupla_list = list(tupla_list)
print(tupla_list)
print(type(tupla_list))
print('\n')

print("Para transformar una lista(ARRAY) a una TUPLA, se usa la funcion tuple")
tupla_list = tuple(tupla_list)
print(tupla_list)
print(type(tupla_list))




