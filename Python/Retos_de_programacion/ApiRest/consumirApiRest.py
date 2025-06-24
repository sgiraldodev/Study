'''
Consumir la siguiente api rest : https://jsonplaceholder.typicode.com/posts y guardar la información 
en una lista(Array) para imprimir en pantalla.

Para hacer uso de la libreria requests se requiere instalarla.
    pip install requests      
'''

import requests
import json

# URL de la API
url = 'https://jsonplaceholder.typicode.com/posts'

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta JSON en un diccionario de Python
    data = response.json()
    #print(json.dumps(data, indent=4))    
    
    # Almacenar la información en un array
    array = []
    for index, item in enumerate(data):
        row = [item['userId'], item['id'], item['title'], item['body']]
        array.append(row)
        print(f"Fila {index + 1}: {row}") # Imprimir el número de fila y la fila
    
        
    user_id = array[99][0]
    print(f"User Id: {user_id} \n")

    id_u = array[99][1]
    print(f"Id: {id_u}\n")

    user_title = array[99][2]
    print(f"Title: {user_title}\n")

    user_body = array[99][3]
    print(f"Body: {user_body}\n")
    
else:
    print(f"Error en la solicitud: {response.status_code}")
    