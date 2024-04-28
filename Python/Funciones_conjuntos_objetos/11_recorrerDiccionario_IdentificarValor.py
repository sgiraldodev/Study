
clients = [
  {
    "client": "John Doe",
    "saving_account": True,
    "City": "New York",
    "Date": "2022-01-01",
    "bank": "Citibank",
    "balance": 5000
  },
  {
    "client": "Jane Smith",
    "saving_account": False,
    "City": "Los Angeles",
    "Date": "2022-01-02",
    "bank": "Wells Fargo",
    "balance": 10000
  },
  {
    "client": "Michael Johnson",
    "saving_account": True,
    "City": "Chicago",
    "Date": "2022-01-03",
    "bank": "Chase",
    "balance": 7500
  },
  {
    "client": "Emily Davis",
    "saving_account": True,
    "City": "Houston",
    "Date": "2022-01-04",
    "bank": "Citibank",
    "balance": 3000
  },
  {
    "client": "Daniel Wilson",
    "saving_account": False,
    "City": "Phoenix",
    "Date": "2022-01-05",
    "bank": "US Bank",
    "balance": 6000
  },
  {
    "client": "Olivia Martinez",
    "saving_account": True,
    "City": "Philadelphia",
    "Date": "2022-01-06",
    "bank": "PNC Bank",
    "balance": 9000
  },
  {
    "client": "William Anderson",
    "saving_account": True,
    "City": "San Antonio",
    "Date": "2022-01-07",
    "bank": "TD Bank",
    "balance": 4000
  },
  {
    "client": "Sophia Taylor",
    "saving_account": False,
    "City": "San Diego",
    "Date": "2022-01-08",
    "bank": "Citibank",
    "balance": 7000
  },
  {
    "client": "David Thomas",
    "saving_account": True,
    "City": "Dallas",
    "Date": "2022-01-09",
    "bank": "SunTrust",
    "balance": 5500
  },
  {
    "client": "Isabella Hernandez",
    "saving_account": True,
    "City": "San Jose",
    "Date": "2022-01-10",
    "bank": "Citibank",
    "balance": 8000
  },
  {
    "client": "Joseph Lopez",
    "saving_account": False,
    "City": "Austin",
    "Date": "2022-01-11",
    "bank": "Regions Bank",
    "balance": 3500
  },
  {
    "client": "Sofia Gonzalez",
    "saving_account": True,
    "City": "Jacksonville",
    "Date": "2022-01-12",
    "bank": "M&T Bank",
    "balance": 6500
  },
  {
    "client": "Charles Wilson",
    "saving_account": True,
    "City": "San Francisco",
    "Date": "2022-01-13",
    "bank": "Huntington Bank",
    "balance": 9500
  },
  {
    "client": "Santiago Giraldo",
    "saving_account": False,
    "City": "San Francisco",
    "Date": "2022-01-14",
    "bank": "First Republic Bank",
    "balance": 4500
  },
  {
    "client": "Matthew Hall",
    "saving_account": True,
    "City": "Columbus",
    "Date": "2022-01-15",
    "bank": "Santander Bank",
    "balance": 7500
  },
  {
    "client": "Harper Young",
    "saving_account": True,
    "City": "Fort Worth",
    "Date": "2022-01-16",
    "bank": "Comerica Bank",
    "balance": 5000
  },
  {
    "client": "Ethan Hernandez",
    "saving_account": False,
    "City": "San Francisco",
    "Date": "2022-01-17",
    "bank": "Fifth Third Bank",
    "balance": 8000
  },
  {
    "client": "Amelia King",
    "saving_account": True,
    "City": "Detroit",
    "Date": "2022-01-18",
    "bank": "BMO Harris Bank",
    "balance": 5500
  },
  {
    "client": "Daniel Green",
    "saving_account": True,
    "City": "Seattle",
    "Date": "2022-01-19",
    "bank": "Union Bank",
    "balance": 9000
  },
  {
    "client": "Daniela",
    "saving_account": False,
    "City": "Denver",
    "Date": "2022-01-20",
    "bank": "CIT Bank",
    "balance": 4000
  }
]
'''
1. Imprimir los nombres de todos los clientes que tienen una cuenta de ahorros.
2. Crear una lista con los nombres de todos los clientes que viven en "San Francisco".
3. Crear una lista bidimensional donde cada sublista contiene el nombre del cliente y su saldo.
4. Imprimir los nombres de los clientes cuyo saldo es mayor que 5000.
5. Crear una lista con los nombres de todos los clientes que tienen una cuenta de ahorros y viven en "Indianapolis".
6. Crear una lista bidimensional donde cada sublista contiene el nombre del cliente y el nombre del banco si el cliente tiene una cuenta de ahorros.
'''

print("Imprimir los nombres de todos los clientes que tienen una cuenta de ahorros.")
print('*' *15)
print('\n')

for i in clients:
    if i["saving_account"] == True:
        print(i["client"])
        

print('\n')
print("Crear una lista con los nombres de todos los clientes que viven en San Francisco.")
print('*' *15)
print('\n')

clientesSanFrancisco = []


for i in clients:
    if i["City"] == "San Francisco":
        clientesSanFrancisco.append(i["client"])
        
print(clientesSanFrancisco)

san_francisco_clients = [i["client"] for i in clients if i["City"] == "San Francisco"]
print(san_francisco_clients)