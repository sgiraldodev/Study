'''FUNCION BASiCA'''
def hola(saludo):
    print(f'Hola {saludo}')
    
hola('Mundo')

print('\n')
print('+' * 50)

'''FUNCION BASiCA que recibe datos'''
def suma(val1, val2):
    print(val1 + val2)
suma(2, 2)

'''FUNCION BASiCA que llama a una funcion dentro de otra funcion'''
print('\n')
print('+' * 50)
print('Funcion dentro de otra funcion')

def llamados(val1, val2):
    print(val1 + val2)
    hola('mundo2')

llamados(2, 2)

'''FUNCION que recibe y retorna valores'''
print('\n')
print('+' * 50)
print('Uso del RETURN para Funciones que reciban y retornen datos')

suma = 0
for x in range(1, 4):
    suma += x
print(suma)

def suma(min, max):
    suma2 = 0
    for i in range(min, max):
        suma2 += i

    return suma2

resultado = suma(10, 20)
print(f'El resultado es: {resultado} ')

'''FUNCION para retornar mas de un valor y definir arg por defecto'''
print('\n')
print('+' * 50)
print('FUNCION para sacar el volumen')

def volumen(tamaño=1, ancho=1, profundidad=1):
    return tamaño * ancho * profundidad, 'return adicional'

result = volumen(1, 2, 3) #Aca le enviamos los datos
result2 = volumen() #Aca NO le enviamos los datos y el toma los argumentos por defecto
result3 = volumen(ancho = 5) #Aca le enviamos un argumento especifico. Tiene que tener el mismo nombre definido en la funcion.
print(f'Con datos: {result} y sin datos sino con argumentos= {result2}, y con datos especificos: {result3}')

'''FUNCION para retornar varios valores'''
print('\n')
print('+' * 50)
print('Multiples retur')

def multiplicacion(v1 = 1, v2 = 1):
    return v1 * v2 , 'dato adicional', 1234

print(f'Llamado a la funcion: {multiplicacion(2, 4)}')
dato2 = multiplicacion()
print(f'Segundo return: {dato2[1]}')

'''SEGUNDA FORMA para retornar varios valores'''
print('\n')
print('+' * 50)
print('Para almacenar los valores del los return de la funcion, se deben de invocar con el mismo numero de posisiciones')

return1, return2, return3 = multiplicacion()
print(f'Valor del return1 = {return1}, valor del return2=  {return2}, valor del return3=  {return3}')


print('\n')
print('+' * 50)
print ('Funciones con return condicionados')

def message_creator(text):
    # Escribe tu solución 👇
    if text == 'computadora':
        return 'Con mi computadora puedo programar usando Python'
    elif text == 'celular':
        return'En mi celular puedo aprender usando la app de Platzi'
    elif text == 'cable':
        return '¡Hay un cable en mi bota!'
    else:
        return 'Artículo no encontrado'


text = ''
response = message_creator(text)
print(response)