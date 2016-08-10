class Persona:

    def __init__(self,edad,nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a " + self.nombre + " de " + str(self.edad))
    def hablar(self, * palabras):
        for frase in palabras:
            print(self.nombre + ": " + frase)


class Chef(Persona):

    #def __init__(self):
        #super(Persona, self).__init__()
    def cocinar(self, comida):
        print("Yo cocino: " + comida)

juan = Persona(18, "Juan")
juan.hablar()
juan.hablar("Hola, esto es una prueba", "Estoy hablando otra vez")
omar = Chef(24, "Omar")
omar.cocinar("huevos revueltos")