#diccionarios
"""
Los diccionarios en Python son estructuras de datos que almacenan pares de clave-valor.
A diferencia de las listas y las tuplas, en un diccionario, cada elemento está compuesto 
por una clave y un valor asociado. Los diccionarios son mutables, 
lo que significa que puedes modificar, agregar o eliminar pares de clave-valor después de que 
el diccionario ha sido creado. Los diccionarios se definen usando llaves {}
"""
mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}
perfil = mi_diccionario
print(perfil)
print(perfil["nombre"])
print("La edad es",perfil["edad"])
#ejercicio diccionario anidado
personas = {
    "persona1": {
        "nombre": "Juan",
        "edad": 25,
        "ciudad": "Madrid"
    },
    "persona2": {
        "nombre": "Maria",
        "edad": 30,
        "ciudad": "Barcelona"
    },
    "persona3": {
        "nombre": "Pedro",
        "edad": 35,
        "ciudad": "Valencia"
    }
}
print(personas)
print("********")
print(personas["persona1"])
print("********")
print(personas["persona2"]["nombre"])
print("********")
print(personas.__len__())
datos = personas["persona3"]
print(datos["nombre"])
persona1 = {
    "nombre": None,
    "edad": None,
    "ciudad": None,
    "telefono": None,
}
persona1["nombre"] = input("Ingrese su nombre: ")
persona1["edad"] = int(input("Ingrese su edad: "))
persona1["ciudad"] = input("Ingrese su ciudad: ")
persona1["telefono"] = input("Ingrese su telefono: ")
print(persona1)
#ejercicio diccionario anidado
"""
Instrucciones:
   1 Crea un diccionario llamado datos_personales con las siguientes claves: "nombre", "edad", 
   "direccion" y "telefono". Inicializa todos los valores a None.
   2 Solicita al usuario que ingrese su nombre, edad, dirección y 
   número de teléfono y almacena cada valor en el diccionario datos_personales.
   3 Muestra en pantalla los datos ingresados por el usuario utilizando las claves del diccionario.
"""
datos_personales = {
    "nombre": None,
    "edad": None,
    "direccion": None,
    "telefono": None
}
datos_personales["nombre"] = input("Ingrese su nombre: ")
datos_personales["edad"] = int(input("Ingrese su edad: "))
datos_personales["direccion"] = input("Ingrese su direccion: ")
datos_personales["telefono"] = input("Ingrese su telefono: ")
print("Nombre:",datos_personales["nombre"], "\nEdad:",datos_personales["edad"], "\nDireccion:",datos_personales["direccion"], "\nTelefono:",datos_personales["telefono"])