#vamos a usar un modulo
import miprimermodulo
import modulo_personalizado
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
suma = miprimermodulo.suma(num1,num2)
resta = miprimermodulo.resta(num1,num2)
multiplicacion = miprimermodulo.multiplicacion(num1,num2)
print("la suma es ",suma)
print("la resta es ",resta)
print("la multiplicacion es ",multiplicacion)
numero = int(input("Ingrese un numero: "))
if modulo_personalizado.es_par(numero):
    print("El numero es par")       
else:
    print("El numero es impar")