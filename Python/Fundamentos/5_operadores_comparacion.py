print("\n")
print("#####")
print("Operadores de comparación, relacionales, bit a bit, en en Python")
print('\n')



print("\n")
print("#####")
print("Operadores de comparación o racionales")
print('\n')

print(" >	Devuelve True si el operador de la izquierda es mayor que el operador de la derecha	12 > 3 devuelve True")
print(" <	Devuelve True si el operador de la derecha es mayor que el operador de la izquierda	12 < 3 devuelve False")
print(" ==	Devuelve True si ambos operandos son iguales	12 == 3 devuelve False")
print(" >=	Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha	12 >= 3 devuelve True")
print(" <=	Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda	12 <= 3 devuelve False")
print(" !=	Devuelve True si ambos operandos no son iguales. 2 != 3 = True")

print("\n")
print("#####")
print("Operadores Logicos")
print('\n')

print("and	Devuelve True si ambos operandos son True	a and b")
print("or	Devuelve True si alguno de los operandos es True	a or b")
print("not	Devuelve True si alguno de los operandos False	not a")

a = 2
b = 3
c = not(a > b)
print(c)
c = (a == 3 or b == 3)
print(c)
c = (a > b and b < a)
print(c)

print("#####")
print("Operadores de Pertenencia")
print('\n')

print("Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).")
print("in y not in son operadores de pertenencia.")
print("in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.")
print("not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.")

a = [1,2,3,4,5]
  
#Esta 3 en la lista a?
print(3 in a) # Muestra True 
  
#No está 12 en la lista a?
print(12 not in a) # Muestra True
  
str = "Hello World"
  
#Contiene World el string str?
print("World" in str) # Muestra True
  
#Contiene world el string str? (nota: distingue mayúsculas y minúsculas)
print("world" in str) # Muestra False  

print("code" not in str)# Muestra True