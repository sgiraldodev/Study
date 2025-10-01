print('\n')
print("1.Imprime todos los números del 1 al 100.")
print('+' * 50)
print('\n')

print("2.Imprime todos los números pares del 1 al 100.")
print('+' * 50)
print('\n')

print("version 1")
for i in range(0, 100):
    if(i%2) == 0:
        print(i)

print("version 2")
for i in range(0, 100, 2): #al agregar el tercer valor en range, lo que hacemos es definirle que salte de 2 en 2, por eso si comenzamos de 0 va a revisar los pares, si es desde el 1 los impares.
    print(i)

print('\n')
print("3.mprime todos los números impares del 1 al 100.")
print('+' * 50)
print('\n')

print("version 1")
impares = [i for i in range(0, 100) if i % 2 != 0]
print (impares)
print('\n')

print("version 2")
for i in range(1, 100, 2):
    print (i)
print('\n')

print('\n')
print("4.Imprime todos los números del 1 al 100 que son divisibles por 7.")
print('+' * 50)
print('\n')

multiplos7 = [i for i in range(0, 100) if i % 7 == 0]
print(multiplos7)

print('\n')
print("5.Imprime todos los números del 1 al 100, pero imprime Fizz para los números divisibles por 3, '\n' fuzz para los números divisibles por 5 y FizzBuzz para los números divisibles por ambos.")
print('+' * 50)
print('\n')

for i in range(1, 101):
    if (i % 3 == 0):
        if(i % 5 == 0):
            print(f'FizzBuzz-{i}')
        print(f'Fizz-{i}')    
    elif (i % 5 == 0):
        print(f'Fuzz-{i}')

print('\n')
print('Forma 2')

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f'FizzBuzz - {i}')
    elif i % 3 == 0:
        print(f'Fizz-{i}')
    elif i % 5 == 0:
        print(f'Buzz-{i}')



print('\n')
print("6.Imprime la suma de todos los números del 1 al 100")
print('+' * 50)
print('\n')

sumatoria = [i for i in range(1, 101)]
print(sum(sumatoria))

print('\n')
print('Forma 2')
suma = sum(range(1, 101))
print(suma)



print('\n')
print("7. Imprime la suma de todos los números pares del 1 al 100 en orden inverso")
print('+' * 50)
print('\n')

suma = [i for i in reversed(range(1, 101)) if i % 2 == 0]
print(sum(suma))