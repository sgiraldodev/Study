'''
Crea una función en Python llamada es_palindromo que reciba una cadena de texto 
y determine si es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda, 
ignorando mayúsculas, espacios y tildes).

es_palindromo("Anita lava la tina")  # True
es_palindromo("Hola mundo")         # False
es_palindromo("Amo la paloma")      # True

'''
import unicodedata 

def es_palindromo(frase:str) -> bool:
    return frase == frase[::-1]
    
frase = str(input("Ingresa tu frase: "))
frase = frase.lower()
frase = frase.replace(" ", "")
frase = unicodedata.normalize('NFD', frase)
print(frase)
if es_palindromo(frase):
    print("Es Palindromo")
else:
    print("No es palindromo")
