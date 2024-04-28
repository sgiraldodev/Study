print("\n\n")
print("#####")
print("Con el comando PRINT se muestra algo en pantalla")


#Uso de comentarios en Python
print("\n\n")
print("#####")
print("Para comentar una sola lina se usa #, para varias lineas se usa la triple comilla simple(''')")

######
print("\n\n")
print("#####")
'''
Uso de comentarios 
multilinea en 
Python '''
print("Para comentar varias lineas se usa la triple comilla simple(''')");

######
print("\n\n")
print("#####")
print("Desde el comando print tambien se pueden hacer operaciones aritmeticas: por ej 2x2 =", 2 * 2)
print("Por orden de prioridad, python toma encuenta primero parentesis, potenciacion, multiplicacion, division y suma")
print(5 + (5 * 9) / 2)

######
print("\n\n")
print("#####")
print("Variables 1 en Python")
print("Dependiendo de la forma como se alamcence la informacion en una varible python reconoce su tipo. \nSi esta entre ('') o (comilla doble) seria string. Si es sin comillas seria numerica. Si es con punto seria float o decimal")

strVariable1 = "Santiago";
strVariable2 = "Giraldo";
intVariable3 = 34;

#Formas de concatenar
print("\n")
print("#####")
print("Formas de concatenar")
print(strVariable1, strVariable2 + " " + "Aristizabal")
print(strVariable1, strVariable2, "Aristizabal", intVariable3)

#Funcion input en Python
print("\n")
print("#####")
print("Funcion input en Python")
strVariable4 = ""
strVariable4 = input("Digita una canción que te guste: ")
print("La canción digitada es:", strVariable4)
