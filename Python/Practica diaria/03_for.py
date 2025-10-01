import json

print('Crea un diccionario que almacene el nombre y la edad de varias personas. Luego, muestra en pantalla el nombre de la persona más joven.')
print('*' * 50)
print('\n')

#Solicitar nombres de las personas 
idNombres = str(input('Digite el nombre de las personas separado por comas (,): '))
#divide una cadena en una lista donde cada palabra es un elemento de la lista
idNombres = idNombres.split(',')
#quitamos los espacios en blanco con el metodo strip
nombres = [nombre.strip() for nombre in idNombres]
print(nombres)

#Solicitar las edades de las personas
idEdades = str(input('Digite las respectivas edades en el orden de los nombres ingresados, separados por comas: '))
idEdades = idEdades.split(',')
edades = [nombre.strip() for nombre in idEdades]
print(edades)

personas = {nombres[i]: edades[i] for i in range(len(nombres))}
print(json.dumps(personas, indent=4))
print('\n')

masjoven = min(personas, key=personas.get)
print(f'La persona más joven es {masjoven}')


