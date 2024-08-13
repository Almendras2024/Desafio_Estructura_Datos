# Importar el texto desde un archivo
with open("lorem_ipsum.txt", "r") as archivo:
    texto = archivo.read()

# Contar la cantidad de caracteres distintos
caracteres_distintos = set(texto)
cantidad_caracteres_distintos = len(caracteres_distintos)

# Contar el número de palabras distintas
palabras = texto.split()
palabras_distintas = set(palabras)
cantidad_palabras_distintas = len(palabras_distintas)

# Imprimir los resultados
print("Cantidad de caracteres distintos:", cantidad_caracteres_distintos)
print("Cantidad de palabras distintas:", cantidad_palabras_distintas)