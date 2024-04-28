print('MAP para diccionarios ')
print('\n')



print('Usa map para recorrer un diccionario y extraer las tallas de las camisa y usal filter para una talla especifica')
diccionario1 = [
    {
        "nombre": "Santiago",
        "apellido": "Giraldo",
        "talla": "XL"
        
    },
    {        
        "nombre": "Felipe",
        "apellido": "Giraldo",
        "talla": "L"
    }, 
    {
        "nombre": "Andres",
        "apellido": "Giraldo",
        "talla": "M"
    }
]

print(diccionario1)
#Crea una lista, y usa map donde guarde el valor a registar, recorriendo la lista diccionario1
tallas = (list(map(lambda item : item['talla'], diccionario1))) 
tallasEspecifica = (list(filter(lambda item: item['talla'] == 'L', diccionario1)))
print(tallas)
print(tallasEspecifica)
print('\n')



print('*' * 50)
print('Usar la funcion de orden superior(filter) para recorrer un diccionario e identificar la persona mayor ')

personas = [
    {
        "nombre": "Santiago",
        "edad": 30
    },
    {        
        "nombre": "Felipe",
        "edad": 25
    }, 
    {
        "nombre": "Andres",
        "edad": 35
    }
]
print(personas)
mayores = (list(filter(lambda persona: persona['edad'] > 30, personas)))
print(mayores)
print('\n')


print('*' * 50)
print('Agregar un nuevo elemento al diccionario de personas usando map ')
print(personas)

def add_city(item):
    item['ciudad'] = 'Pereira'
    return item

personasV2 = (list(map(add_city, personas)))
print(personasV2)
print(personas) # ACA NO APLICA INMUTABILIDAD Y SE MODIFICO LA LISTA ORIGINAL


personas2 = [
    {
        "nombre": "Santiago",
        "edad": 30
    },
    {        
        "nombre": "Felipe",
        "edad": 25
    }, 
    {
        "nombre": "Andres",
        "edad": 35
    }
]

print('*' * 50)
print('MAP con INMUTABILIDAD, es decir que al modificar una lista luego de usar el MAP no modifique el estado de una lista original')
def add_city_inmutable(item):
    itemInmutable = item.copy()
    itemInmutable['ciudad'] = 'Manizales'
    return itemInmutable
    
personasInmutabilidad = (list(map(add_city_inmutable, personas2)))
print(personas2)
print(personasInmutabilidad)