"""
Escribe un programa en Python que realice operaciones matemáticas simples 
(suma, resta, multiplicación y división) utilizando una función. 
El programa debe permitir al usuario ingresar dos números y seleccionar una operación para realizar.
Instrucciones:
   1 Define una función llamada calculadora que acepte tres argumentos: 
   num1, num2 y operacion. Esta función debe realizar la operación especificada 
   (suma, resta, multiplicación o división) y devolver el resultado.
   2 Solicita al usuario que ingrese dos números (num1 y num2) y 
   la operación (+, -, * o /) que desea realizar.
   3 Llama a la función calculadora con los números ingresados y 
   la operación seleccionada, y muestra el resultado en pantalla.
"""
def calculadora(num1, num2, operacion):
    if operacion == "+":
        resultado = num1 + num2
        return resultado
    elif operacion == "-":
        resultado = num1 - num2
        return resultado
    elif operacion == "*":
        resultado = num1 * num2
        return resultado
    elif operacion == "/":
        resultado = num1 / num2
        return resultado
    else:
        print("Operacion no valida")
num1 = int(input("Ingrese el primer numero: "))     
num2 = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion que desea realizar: ")
resultado = calculadora(num1, num2, operacion)
print("El resultado de la operacion es: ",resultado)