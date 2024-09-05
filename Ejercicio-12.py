#funciones
def es_par(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)
es_par(5)
es_par(4)
def saludar(nombre):
    print("Hola",nombre)
saludar("Juan")
def sumar(a,b):
    resultado = a + b
    return resultado
dato = sumar(8,7)
print(dato)
print("***************")
#una forma
def sumaIngresada():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    resultado = a + b
    print("resultado",resultado)
sumaIngresada()
#segunda forma
numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
resultado2 = sumar(numero1,numero2)
resultado_2 = (resultado2)
print(resultado_2)
#ejercicio2
def es_par2(num):
    if num % 2 == 0:
        return True
    else:
        return False

numeropar = int(input("Ingrese un numero: "))
if es_par2(numeropar) == True:
    print("El numero es par")
else:
    print("El numero es impar")
#ejercicio3
def listanumeros(lista):
    maximo = max(lista)
    return maximo
lista = [100,258,3,40,5,65874,7,8,987,10]
valor = listanumeros(lista)
print("El numero max de la lista es: ",valor)


