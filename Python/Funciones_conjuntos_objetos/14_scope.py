'''
En este código, variable_global es una variable global que se puede acceder tanto dentro como fuera de la función mi_funcion(). 
Por otro lado, variable_local es una variable local que solo se puede acceder dentro de la función mi_funcion(). 
Intentar acceder a variable_local fuera de la función resultará en un NameError.

Los escopes permiten definir los alcances de una variable o funcion y trabajan en base a contextos para saber donde se invocan
'''


# Variable global
variable_global = "Soy una variable global"

def mi_funcion():
    # Variable local
    variable_local = "Soy una variable local"
    print(variable_local)
    print(variable_global)

mi_funcion()

# Intentando imprimir la variable local fuera de la función
try:
    print(variable_local)
except NameError:
    print("La variable local no está definida fuera de la función")

# Imprimiendo la variable global fuera de la función
print(variable_global)