print("\n")
print("#" * 15)
print("Los operadores logicos nos permiten definir los caminos en los que el codigo va a ejecutarse o como va a ejecutarse")
print('\n')

print("Los operadores lógicos son and (y) or (o) not (no) y sirven para comprobar si dos o más operandos son ciertos (True) o falsos (false) y nos devolverá como resultado True o False. Normalmente los solemos utilizar mucho en los condicionales para devolver un booleano comparando varios elementos.Lógica")
print('\n')
print("Otro operador importante:")
print('\n')
print("En cambio el operador Not sirve para indicar el contrario de un booleano como True / False. Si colocamos un Not True estaríamos diciendo “No verdadero” y Not False “No falso”. En una condición si no es verdadero nos devolverá false y si no es false nos devolverá verdadero!")

print("#" * 15)

a = 2
b = 3
c = not(a > b)
print(c)
c = (a == 3 or b == 3)
print(c)
c = (a > b and b < a)
print(c)

stock = input("Ingrese el numero del inventario existente: ")
stock = int(stock)

print(stock >= 100 or stock <= 1000)
print(stock >= 100 and stock <= 1000)
print(not(stock >= 100 and stock <= 1000))