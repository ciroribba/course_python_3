"""
Una tupla en Python es una estructura de datos similar a una lista, 
pero con la diferencia clave de que las tuplas son inmutables. 
Esto significa que, una vez creada, no se puede modificar: no puedes cambiar, 
añadir ni eliminar elementos dentro de una tupla. 
Las tuplas se definen usando paréntesis () y sus elementos se separan por comas.
"""
mi_tupla1 = (1, 2, 3, 4, 5)
mi_tupla2 = ('a', 'b', 'c', 'd', 'e')
mi_tupla3 = (1, 'a', 2, 'b', 3.14, 'Hola Mundo')
print(mi_tupla1)
print(mi_tupla2[0])
print(mi_tupla3[5])
#ejericio
personas = (("Juan", 25),("Maria", 17),("Luis", 30),("Ana", 24))
print("Mayores de edad")
for nombre, edad in personas:
    if edad >= 18:
        print(nombre, edad)
print("Menores de edad")
for nombre, edad in personas:
    if edad < 18:
        print(nombre, edad)
#ejercicio
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
suma = sum(numeros)
print("La suma de los numeros es:", suma)
""" 
En este ejercicio, los estudiantes deben crear un programa en Python 
que verifique si una palabra ingresada por el usuario está presente 
en una tupla predefinida de palabras. 
El programa debe informar al usuario si la palabra está o no en la tupla.
"""
tupla_ejercicio = ('hola', 'mundo', 'python', 'programacion', 'tupla')
palabra_buscar = input("Ingrese una palabra: ").lower()
if palabra_buscar in tupla_ejercicio:
    print("La palabra está en la tupla")
else:
    print("La palabra no está en la tupla.")
