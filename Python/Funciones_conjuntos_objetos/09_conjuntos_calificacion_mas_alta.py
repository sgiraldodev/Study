estudiantes = [
    {
        "name": "John Doe",
        "calification": "85"
    },
    {
        "name": "Jane Smith",
        "calification": "92"
    },
    {
        "name": "Mike Johnson",
        "calification": "78"
    },
    {
        "name": "Sarah Williams",
        "calification": "90"
    },
    {
        "name": "David Brown",
        "calification": "87"
    },
    {
        "name": "Emily Davis",
        "calification": "95"
    },
    {
        "name": "Michael Wilson",
        "calification": "82"
    },
    {
        "name": "Olivia Taylor",
        "calification": "89"
    },
    {
        "name": "Jacob Anderson",
        "calification": "93"
    },
    {
        "name": "Sophia Martinez",
        "calification": "88"
    }
]

max_calification = max(estudiantes, key=lambda x: int(x["calification"]))
print("El estudiante con la calificación más alta es:", max_calification["name"])
print('*' * 15)
print('\n')

primerNombre = list(estudiantes)
print(primerNombre[0]["name"])