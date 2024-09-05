class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def arrancar(self):
        return f"{self.marca} {self.modelo} ha arrancado"
    
class coche(vehiculo):
    def acelerar(self):    
        return f"{self.marca} {self.modelo} ha acelerado"
    
class moto(vehiculo):
    def caballito(self):
        return f"{self.marca} {self.modelo} esta piruteando"
    
auto = coche("Ford", "Fiesta")
motocicleta = moto("Zuzuki", "AX100")

print(f"Auto marca y modelo: {auto.marca} {auto.modelo}")
print(f"Motocicleta marca y modelo: {motocicleta.marca} {motocicleta.modelo}")

print(auto.arrancar())
print(auto.acelerar())
print(motocicleta.arrancar())
print(motocicleta.caballito())
"""
class coche(vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color
        
    def arrancar(self):
        return f"{self.marca} {self.modelo} de color {self.color} ha arrancado"
"""  
"""
Ejercicio 16
Crea una superclase llamada Animal con los siguientes métodos:
    __init__(self, nombre): Inicializa el nombre del animal.
    hablar(self): Debe ser un método abstracto (sin implementación) que represente el 
    sonido que hace el animal. Las subclases deben proporcionar una implementación 
    para este método.
Luego, crea dos subclases, Perro y Gato, que hereden de Animal. 
En estas subclases, implementa el método hablar() para representar 
los sonidos típicos de un perro y un gato respectivamente (por ejemplo, 
"Guau" y "Miau").
Finalmente, crea instancias de ambas subclases y muestra el nombre 
y el sonido de cada animal en pantalla.
"""  
#ejercicio
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    # def hablar(self):
    #     pass
class Perro(Animal):
    def hablar(self):
        return "Guau"
class Gato(Animal):
    def hablar(self):
        return "Miau"
perrito = Perro("Firulais")
gatito = Gato("Garfield")
print(f"{perrito.nombre} dice: {perrito.hablar()}")
print(f"{gatito.nombre} dice: {gatito.hablar()}")