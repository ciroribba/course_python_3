x = 5
if x > 5:
    print('x es mayor que 5')
elif x < 5:
    print('x es menor que 5')
else:
    print('x es igual a 5')
# ejercicio 
# 1. Crear un programa que solicite al usuario ingresar su edad y muestre en pantalla si es mayor de edad o no.
x = int(input('Ingrese su edad: '))
if x < 12:
    print('Eres un niño')
elif x < 18:
    print('Eres un adolescente')
elif x < 30:
    print('Eres un joven')
else:
    print('Eres un adulto')
# Pedir la calificación del estudiante
calificacion = float(input("Por favor, ingresa tu calificación: "))

# Verificar y mostrar el resultado
if calificacion >= 90:
    print("¡Felicidades! Has aprobado con una calificación sobresaliente.")
elif calificacion >= 70:
    print("Has aprobado satisfactoriamente.")
elif calificacion >= 60:
    print("Has aprobado, pero necesitas mejorar un poco.")
else:
    print("Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación.")