import json

print('Crea un diccionario que almacene el nombre y el salario de varios empleados. Luego, muestra en pantalla el nombre del empleado con el salario más alto.')
print('*' * 50)
print('\n')


#crear diccionario
salarios = {
    'santiago':800,
    'robert':1800,
    'pablo':5800    
}
print(type(salarios))
print(json.dumps(salarios, indent=4))

print(max(salarios, key=salarios.get))