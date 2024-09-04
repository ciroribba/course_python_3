#Listas
"""
Las listas en Python son estructuras de datos que, a diferencia de las tuplas, 
son mutables, lo que significa que puedes modificar, agregar y eliminar elementos 
después de que la lista ha sido creada. 
Las listas se definen usando corchetes [] y sus elementos también se separan por comas.
"""
mi_lista = [1, 2, 3, "hola", True]
print(mi_lista)
print(mi_lista[0])
mi_lista[1] = 20
print(mi_lista)
mi_lista.append("nuevo")
print(mi_lista)
del mi_lista[2]
print(mi_lista)
#ejercicio 
frutas = ["manzana", "pera", "uva", "sandia", "melon"]
for fruta in frutas:
    print(fruta)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = sum(numeros)
print(suma)
#Ejercicio
"""
Escribe un programa en Python que cree una lista de colores y 
luego muestre cada color en una línea separada.
Instrucciones:
   1 Crea una lista llamada colores que contenga varios nombres de colores 
   (por ejemplo, "rojo", "verde", "azul", etc.).
   2 Utiliza un bucle for para recorrer la lista de colores.
   3 En cada iteración del bucle, muestra un color en una línea 
   separada utilizando la función print().
"""
colores = ["rojo", "verde", "azul", "amarillo", "naranja", "rosa", "morado"]
for color in colores:
    print(color)