contador = 1
while contador <= 100:
    print(contador)
    contador += 1
    if contador == 60:
        break
print("Fin del ciclo")
#Ejercicio conteno año nuevo
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1
print("Feliz año nuevo")
#Ejercicio pedir que usuario que ingrese un numero, y cuando coloque negativo, se detenga el ciclo y nos de la suma de todos los ingresados
suma = 0
numero = int(input("Ingresa un numero positivo o numero negativo para terminar el ciclo: "))
while numero >= 0:
    suma += numero
    numero = int(input("Ingresa un numero positivo o numero negativo para terminar el ciclo: "))
print(f"La suma de los números ingresados es {suma}")
print("Fin del ciclo")
#Ejercicio En esta tarea, se te pide crear un programa en Python que cuente desde 1 hasta un número límite ingresado por el usuario. El programa debe utilizar un bucle while para llevar a cabo el conteo y mostrar los números en orden ascendente. Una vez que se alcance el número límite, el programa debe imprimir "Conteo completado".
numero = int(input("Ingresa un número límite para contar: "))
contador = 1
while contador <= numero:
    print(contador)
    contador += 1
print("Conteo completado")
