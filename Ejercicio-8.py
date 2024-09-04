nombre = "Ciro"
apellido = "Zeballo Ribba"
frase = "Hola esta es una frase"
print("Hola, mi nombre es", nombre, apellido, "y mi frase es:", frase)
print("Hola, mi nombre es {} {} y mi frase es: {}".format(nombre, apellido, frase))
print(f"Hola, mi nombre es {nombre} {apellido} y mi frase es: {frase}")
longitud = len(frase)
print("La longitud de la frase es:", longitud)
print(apellido[5])
print(apellido[5:12])
print(apellido[:5])
palabras = frase.split()
#Lista de palabras
print(palabras)
#Lista de letras
letras = list(frase)
print(letras)
print(" ".join(palabras))
print("".join(letras))
print(frase.upper())
print(frase.lower())
cambio = frase.replace("Hola", "Chau")
print(cambio)
for x in apellido:
    print(x)
