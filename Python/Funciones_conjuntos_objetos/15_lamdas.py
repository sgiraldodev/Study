'''
Funciones lambda
****************
Las funciones lambda o anónimas son un tipo de funciones en Python que típicamente se definen en una línea y cuyo código a ejecutar suele ser pequeño. 
Resulta complicado explicar las diferencias
'''

print('Funcion trandicional para sumar')
def suma(a, b):
    return a + b
print(suma(1, 1))

print('+' * 50)
print('\n')
print('Funcion LAMBDA sumar')
print((lambda a , b: a + b)(2, 4) )

print('+' * 50)
print('\n')
print('Funcion LAMBDA incrementar un numero forma 1')
print((lambda a : a + 1)(2)) # aca despues de la funcion se colocan los valores que recibiria

print('\n')
print('Funcion LAMBDA incrementar un numero forma 2, que es asignado a una variable tipo lamnda')
incrementv2 = lambda a : a + 1
print(incrementv2(2))
print(type(incrementv2))