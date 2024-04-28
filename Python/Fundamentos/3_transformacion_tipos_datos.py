print("\n")
print("#####")
print("En Python, una de sus ventajas es la flexibilidad, por lo que una misma variable podria cambiar su tipo \nde entera, a string, o a boolena:")
print('\n')

varGeneric = "Test"
print("Variable varGeneric ahora vale: ",varGeneric)
print(type(varGeneric))
print("\n")
print("#####")

varGeneric = 35
print("Variable varGeneric ahora vale: ",varGeneric)
print(type(varGeneric))
print("\n")
print("#####")

varGeneric = False
print("Variable varGeneric ahora vale: ",varGeneric)
print(type(varGeneric))
print("\n")
print("#####")

print("\n")
print("#####")
print("Formas de transformar tipos de variable de entero a string o viceseversa")

print("Suma basica teniendo un entero definido")
varAge = 10 #Variable de tipo Entera
print(type(varAge))
print("En 10 años, yo tengo", 30 + varAge)

print("Error sumando enteros con String que es el formato que retorna los input")
varAge = input("Digita tu edad:")
print(type(varAge))
print("En 10 años, yo tengo: Aca saldria este error: TypeError: unsupported operand type(s) for +: 'int' and 'str'")

print("\n")
print("#####")
print("Convirtiendo correctamente de String a Entero")
varAge = input("Digita tu edad:")
print(type(varAge))
print("Convertimos")
varAge = int(varAge)
print(type(varAge))
print("En 10 años, yo tengo:" , varAge + 10)
print("Otra manera de concatenar")
varAge += 10
print(f'En 10 años, yo tengo: {varAge}')


print("\n")
print("#####")
print("Definiendo tipos de variables desde el principio por orden")

varName: str
varEdad: int = 2
print(type(varEdad))

varNumero = int(input('Ingresa un numero:'))
print(f'El numero es {varNumero}')


varName = str(input('Digita tu nombre'))
varEdad = int(input('Digita tu edad'))
varTotal = (varEdad + 10)

print (f'Hola mi nombre es {varName}, tengo {varEdad} y en 10 años tendré {varTotal}')
print('Forma Fea: ' ,varName, 'tengo' ,varEdad, 'y en 10 años tendré',varEdad + 10)