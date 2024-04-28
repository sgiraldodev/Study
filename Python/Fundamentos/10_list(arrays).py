print("#" * 15)
print("Trabajar con listas(Arrays) para almacenar información")


print("#" * 15)
print("Las listas o arrays se crean asignado varios datos a una variable entre []")
varArrayNames = ["Santiago", "Patricia", "Isabel"]
varArrayNumbers = [1,2,3,4]
varArrayCombinado = [1,"Andres",True]
print(varArrayNames, varArrayNumbers)

print("#" * 15)
print("Seleccionar la posicion 2 del array")
print(varArrayNames[1])

print("#" * 15)
print("ACtualizar el valor de la posición 2")
varArrayNames[1] = "Jimena"
print(varArrayNames[1])

print("#" * 15)
print("Seleccionar parte de un array")
print(varArrayNumbers[:2])

print("#" * 15)
print("VAlidar que exista el nombre Isabel en el array de nombres")
print('Isabel' in varArrayNames)