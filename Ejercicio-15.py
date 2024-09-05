class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años')

#se crea una instancia
persona1 = Persona('Juan', 28)
persona1.saludar() # Hola, mi nombre es Juan y tengo 28 años
persona2 = Persona('Maria', 30)
persona2.saludar() # Hola, mi nombre es Maria y tengo 30 años
print("**************")
print("**************")

#Ejercicio 2
class calculadora1:
    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir por cero")
        
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

calc = calculadora1()
resultsuma = calc.sumar(num1, num2)
resultresta = calc.restar(num1, num2)
resultmulti = calc.multiplicar(num1, num2)
resuldiv = calc.dividir(num1, num2)

print(f"La suma de {num1} + {num2} es: {resultsuma}")
print(f"La resta de {num1} - {num2} es: {resultresta}")
print(f"La multiplicación de {num1} * {num2} es: {resultmulti}")
print(f"La división de {num1} / {num2} es: {resuldiv}")
"""
Ejercicio 3
class calculadora1:
    def __init__(self, numero):
        self.resultado = numero

    def sumar(self, numero):
        self.resultado += numero
    
    def restar(self, numero):
        self.resultado -= numero

    def multiplicar(self, numero):
        self.resultado *= numero

    def dividir(self, numero):
        if numero != 0:
            self.resultado /= numero
        else:
            print("No se puede dividir por cero")

    def obtener_resultado(self):
        return self.resultado
    
calculo = calculadora1(0)
calculo.sumar(4)
calculo.restar(2)
calculo.multiplicar(3)
calculo.dividir(2)

resultado = calculo.resultado
print("Resultado ",resultado) # 3
"""
#Tarea:
class ContadorPalabras:
    def __init__(self):
        self.contador = 0

    def contar(self, texto):
        palabras = texto.split()
        self.contador += len(palabras)

    def obtener_contador(self):
        return self.contador

instancia_contador = ContadorPalabras()

texto = "Hola Mundo, aqui practicando Python"
instancia_contador.contar(texto)
