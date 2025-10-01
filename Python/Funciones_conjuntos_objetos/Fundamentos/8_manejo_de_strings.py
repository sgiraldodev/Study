print("\n")
print("#" * 15)
print("Manejo de funciones para trabajar con cadenas de texto")
print('\n')


print("#" * 15)
print("Método IN: Se encarga de validar si una cadena existe dentro de otra cadena")

strText1 = "Existe la palabra funcion en este texto?"
print(strText1)
if "funcion" in strText1:
    print("Si existe")
else:
    print("No existe")

print("#" * 15)
print("Método len: Cuenta el número de caracteres")

strText1 = "Existe la palabra funcion en este texto?"
numText1 = len(strText1)
print(numText1)

print("#" * 15)
print("Método upper: Convierte a mayusculas")
strText1 = "pasa a Mayusculas"
print(strText1.upper())

print("#" * 15)
print("Método lower: Convierte a minusculas")
strText1 = "PASA A MINUSCULAS"
print(strText1.lower())

print("#" * 15)
print("Método count: Cuenta cuantas repeticiones hay en una cadena, difiere entre mayusculas y minusculas")
strText1 = "PASA A MINUSCULAS"
print(strText1.count('A'))

print("#" * 15)
print("Método swapcase: Pasa de mayuscula a minuscula y viseversa")
strText1 = "PaSa a MINUSCULaS"
print(strText1.swapcase())

print("#" * 15)
print("Método startswitch: Valida si en el inicio de la cadena se comienza por algo especifico")
strText1 = "Valida si en el inicio de la cadena se comienza por algo especifico"
print(strText1.startswith('Valida'))

print("#" * 15)
print("Método endswitch: Valida si en el fin de la cadena se termia con algo especifico")
strText1 = "Valida si en el inicio de la cadena se comienza por algo especifico"
print(strText1.endswith('especifico'))

print("#" * 15)
print("Método replace: Reemplaza algo de una cadena por otra cosa definida")
strText1 = "Reemplaza algo de una cadena por otra cosa definida"
print(strText1.replace('cosa', 'palabra'))

print("#" * 15)
print("Método capitalize: Coloca la primera letra en mayuscula")
strText1 = "reemplaza algo de una cadena por otra cosa definida"
print(strText1.capitalize())

print("#" * 15)
print("Método title: Coloca la primera letra en mayuscula de cada palabra")
strText1 = "reemplaza algo de una cadena por otra cosa definida"
print(strText1.title())

print("#" * 15)
print("Método isdigit: Valida si dentro de un string existe un numero")
strText1 = "25"
print(strText1.isdigit())

print("#" * 15)
print("Reto: Pasar lo que digite el usuario en un input a minusculas")
strText1 = input("Digita tu nombre en mayusculas: ")
strText1 = strText1.lower()
print(strText1)
