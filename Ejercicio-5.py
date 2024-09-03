numero1 = 7
#match
match numero1:
    case 1:
        print("El número es 1")
    case 2:
        print("El número es 2")
    case 3:
        print("El número es 3")
    case _:
        print("El número no es ni 1, ni 2, ni 3")
#ejercicio match
numero = int(input("Ingrese un número: "))
match numero%2:
    case 0:
        print("El número es par")
    case 1:
        print("El número es impar")
numero2 = int(input("Ingrese un número: "))
match numero2:
    case 0:
        print("El número es cero")
    case numero2 if numero2 % 2 == 0:
        print("El número es par")
    case numero2 if numero2 % 2 == 1:
        print("El número es impar")
    case _:
        print("El número no conocido")
numero3 = int(input("Ingrese su edad: "))
match numero3:
    case 0:
        print("Es un bebé")
    case numero3 if numero3 > 0 and numero3 < 18:
        print("Es un menor de edad")
    case numero3 if numero3 >= 18 and numero3 < 65:
        print("Es un adulto")
    case _:
        print("Es un adulto mayor")
        