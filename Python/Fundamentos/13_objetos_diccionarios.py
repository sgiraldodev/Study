import json


print("#" * 15)
print("Los diccionarios  son objetos json usados para el manejo de información")
print("Como resumen se podria definir esto ")

print("[ ] = Listas(ARRAYS)")
print("( ) = Tuplas")
print("{ } = Diccionarios / objetos")
print("set( ) = Conjuntos")


print("*" * 15)
print("objeto")

persona = {
    "nombre": "Santiago",
    "edad": 35,
    "novia":False    
}

print(persona)
print(type(persona))
print('Tamaño del objeto: ', len(persona))
print('extraer un valor del objeto, se usan los [], o el get(): ', (persona.get('edad')))
print('El beneficio de usar get() es que si la llave no existe, retorna un none.', (persona.get('eddad')))
print('\n\n')

print('*' * 15)
print('CRUD para objetos/diccionarios')
print('*' * 15)
print('\n')

print('modificar, cambiar el valor de edad a 26')
persona['edad'] = 26
print(persona)
print('\n')

print('Insertar nuevas llaves/valor Empresa, y musica')
persona["empresa"] = "MercadoLibre"
persona["musica"] = ["Rock", "electronica", "tango"]
print('Impresión del objeto actualizado:')
print(persona)
print('\n')

print('Insertar valor (DeathMetal) dentro de la lista musica en el diccionario')
persona["musica"].append('Death Metal')
print(persona)
print('\n')

print("Eliminar registro novia")
del persona["novia"]
print(persona)
print(type(persona))
print('\n')

################################################################################################################
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



