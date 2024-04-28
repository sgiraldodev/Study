print("#" * 15)
print("Trabajar con Strings para capturar la información de sus posiciones")

strText1 = "Santiago Giraldo Aristizal"
print("Texto a trabajar:" , strText1)

print("#" * 15)
print("Capturar la tercera posición del String [2]")
print(strText1[2])


print("#" * 15)
print("Capturar la última posición del String con lenght")
print(strText1[len(strText1) - 1])

print("#" * 15)
print("Capturar la última posición del String con python (-1)")
print(strText1[-1])

print("#" * 15)
print("Capturar la posiciones del string entre la 5  la 10")
print(strText1[5:10])

print("#" * 15)
print("Cambiar al revez el orden del string (::)")
print("Al derecho =>", strText1[:8])
print("Al revez =>", strText1[8::-1])


print("#" * 15)
print("Ir desde un punto especifico hasta el final de un archivo [5:]")
print(strText1[5:])

print("#" * 15)
'''GitHub Copilot: El fragmento de código seleccionado `print(primos[3:10:2])` es un ejemplo de indexación y segmentación (slicing) de listas en Python.

En este caso, `primos` es una lista y `primos[3:10:2]` es una operación de segmentación en esa lista. La segmentación en Python se realiza utilizando la sintaxis `lista[inicio:fin:paso]`.

- `inicio` es el índice donde comienza la segmentación. En Python, la indexación comienza en 0, por lo que `3` se refiere al cuarto elemento de la lista.
- `fin` es el índice donde termina la segmentación. Sin embargo, este índice no se incluye en la segmentación. Por lo tanto, `10` significa que la segmentación se detendrá antes del undécimo elemento.
- `paso` es opcional y se refiere a la cantidad de índices que se saltarán en cada paso. En este caso, `2` significa que se tomará cada segundo elemento en el rango de `3` a `10`.

Por lo tanto, `print(primos[3:10:2])` imprimirá cada segundo elemento de la lista `primos` desde el cuarto elemento hasta el décimo elemento.

Resultado:
[7, 13, 19, 29]

'''
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
print(primos[3:10:2])

var = 8000 > 3330
print(var)