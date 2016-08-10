from abc import ABCMeta, abstractmethod

class Persona:
    __metaclass__ = ABCMeta
    def __init__(self,edad,nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a " + self.nombre + " de " + str(self.edad))
    @abstractmethod
    def hablar(self) : pass


class Deportista(Persona):

    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.__deporte = deporte
        #super(Deportista, self).__init__()
    def practicar(self):
        print(self.nombre + ": Voy a practicar")
    def verDeporte(self):
        return self.__deporte
    def hablar(self, * palabras):
        for frase in palabras:
            print(self.nombre + ": " + frase)


juan = Deportista(18, "Juan", "futbol")
juan.hablar("Hola, esto es una prueba", "Estoy hablando otra vez")
gary = Deportista(22, "Gary", "natacion")
print("Gary practica: " + gary.verDeporte())