#encapsulamiento
class encap:
    def __init__(self):
        #publico
        #self.numero = 0
        #privado
        self.__numero = 0

    def operacion(self):
        #publico
        #print(self.numero + 20)
        #privado
        print(self.__numero + 20)

    def resultado(self):
        #publico
        #return self.numero
        #privado
        return self.__numero
    
ejemplo = encap()
ejemplo.operacion()
ejemplo.numero = 100
print(ejemplo.resultado())
