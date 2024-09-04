#ciclos for
#Ejercicio 6: Crear una lista con 10 frutas y recorrerla con un ciclo for,
frutas = ["banana", "manzana", "pera", "naranja", "mandarina", "kiwi", "sandia", "melon", "coco", "frutilla"]
contador = 0
for i in frutas:
    #print(f"Fruta #{contador}: {frutas[contador]}")
    contador += 1
    print(f"Fruta #{contador}: {i}")
    if contador == 5:
        break
print("Fin del ciclo")
#Ejercicio
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")
print("Fin del ciclo")
#Ejercicio Descripción: Escribe un programa en Python que calcule el promedio de una lista de números.
numeros = [1,2,3,4,5,6,7,10,9,8]
suma = 0
contador = 0
for numero in numeros:
    suma += numero
    contador += 1
    if contador == len(numeros):
        promedio = suma / contador
        print(f"El promedio de la lista de números es {promedio}")
print("Fin del ciclo")
numeros = [1,5,10,15,20]
#Otra forma de hacerlo
suma = 0
for i in numeros:
    suma = suma + i
suma = suma/len(numeros)
print(f"El promedio de los número en la lista seleccionada es {suma}.")
