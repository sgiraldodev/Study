print("\n")
print("#" * 15)
print("Las condiciones nos permiten validar los decisiones que nuestro programa tiene que ejecutar")
print("Se hace uso del if, else y else if")
print('\n')


stock = input("Ingrese el numero del inventario existente: ")
if stock == "":
    print("No se registró ningún valor")

else:
    stock = int(stock)

    if  (stock >= 100 and stock <= 1000):
        print("Estamos en quiebra")
    elif stock > 1100 and stock < 2000: 
        print("Nos sostenemos")

    else:
        print("Impresionante?")
        

    intNum = input ("Ingrese un numero entero: ")
    intNum = int(intNum)

    intNum = (intNum % 2)
    if intNum == 1:
        print("Es un numero impar")
    else:
        print("Es un numero Par", intNum)