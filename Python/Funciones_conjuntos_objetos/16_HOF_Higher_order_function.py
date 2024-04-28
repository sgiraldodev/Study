'''
las funciones de orden superior, o "higher-order functions" en inglés, son funciones que pueden recibir otras funciones como argumentos y/o devolver 
funciones como resultado. En otras palabras, las funciones de orden superior tratan a las funciones como ciudadanos de primera clase, 
permitiendo que sean manipuladas y utilizadas de manera flexible en el código.

Esto es posible en lenguajes de programación que admiten funciones como objetos de primera clase, como Python. Al utilizar funciones de orden superior, 
podemos escribir código más modular, reutilizable y flexible.


'''

# #Un ejemplo común de una función de orden superior es la función map(). Esta función toma una función y una secuencia como argumentos, y aplica la función 
# #a cada elemento de la secuencia, devolviendo una nueva secuencia con los resultados. Aquí hay un ejemplo:

# En este ejemplo, la función cuadrado() se pasa como argumento a la función map(), que la aplica a cada elemento de la lista numeros. 
# El resultado es una nueva lista con los cuadrados de los números originales.

def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = map(cuadrado, numeros)

print(list(cuadrados))  # Output: [1, 4, 9, 16, 25]

print('+' * 50)
print('\n')
print('Funcion que llame a otra funcion para sumar')

def sumar(x):
    return x + 1


def funcion_hof(x, funcion):
    return x + funcion(x)

resultado = funcion_hof(2, sumar) #En este escenario, al llamar a la funcion sumar no uso el () ya que no le defino paramentros para procesar.
print(resultado)

