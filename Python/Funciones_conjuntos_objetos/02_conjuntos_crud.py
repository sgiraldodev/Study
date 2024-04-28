print("Aplicar el CRUD a un conjunto y otras funciones")
print('*'*50)
print('\n')


print('Crear un conjunto de Paises en Python')
print('*'*50)

set_countries = {'Colombia', 'Peru', 'Argentina', 'Chile', 'Colombia', 'Peru', 'Argentina', 'Chile'}    
print(set_countries)


print('\n')
print('Obtener el tamaño de un conjunto')
size = len(set_countries)
print(size)

print('\n')
print('Saber si un elemento existe en un conjunto')

varCountry = 'Colombia'
country_sel = (varCountry in set_countries)
print(country_sel)

print('\n')
print('Agregar un elemento a un conjunto(add)')
set_countries.add('Mexico')
print(set_countries)

print('\n')
print('Modificar un elemento de un conjunto(update), Venezuela', 'Ecuador')
set_countries.update({'Venezuela', 'Ecuador'})
print(set_countries)

print('\n')
print('Eliminar un elemento de un conjunto(remove)(Venezuela)')
print('El remove lanza una excepcion si el elemento no existe')
set_countries.remove('Venezuela')
print(set_countries)

print('\n')
print('Eliminar elemento de un conjunto(discard)')
print('El discard no lanza una excepcion si el elemento no existe')
set_countries.discard('Mexico')
print(set_countries)