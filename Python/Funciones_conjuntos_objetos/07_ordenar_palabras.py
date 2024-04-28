print("Escribe un programa que solicite al usuario una lista de palabras y las ordene alfabéticamente.")
print('*' * 15)
print('\n')


palabras = input('Digite varias palabras o numeros separados por coma:')
palabras = palabras.replace(" ", "")
palabras = palabras.split(",")
palabrasOrdenadas = sorted(palabras)
print(palabras)
print(palabrasOrdenadas)

