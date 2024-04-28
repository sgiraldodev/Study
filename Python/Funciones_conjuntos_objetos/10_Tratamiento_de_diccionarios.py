import json


print("metodos para listar información de los objetos")
print("*" * 15)

objeto_diccionario = {
    "nombre":"santiago",
    "edad": 35,
    "profesion": "desarrollador"
}
print(json.dumps(objeto_diccionario, indent= 4))
print('\n')

print("Metodo items: El método items() devuelve una lista(TUPLAS) con los keys y values del diccionario ")
print(objeto_diccionario.items())
print(type(objeto_diccionario))
print('\n')

print("keys: El método keys() devuelve una lista con todas las keys del diccionario.")
print(objeto_diccionario.keys())
print('\n')

print("values: El método values() devuelve una lista con todos los values o valores del diccionario.")
print(objeto_diccionario.values())
print('\n')


print("Convertir un diccionario en tuplas para luego convertirlo a una lista y poder ser tratado.")
Tuplas = objeto_diccionario.items()
print(Tuplas)
listaTuplas = list(Tuplas)
print(listaTuplas[0])
print('\n')
