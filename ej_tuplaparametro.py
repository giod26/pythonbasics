class Persona:

    def __init__(self):
        self.edad = 18
        self.nombre = "Juan"
        print("Se ha creado a " + self.nombre + " de " + str(self.edad))
    def hablar(self, * palabras):
        for frase in palabras:
            print(self.nombre + ": " + frase)

juan = Persona()
juan.hablar()
juan.hablar("Hola, esto es una prueba", "Estoy hablando otra vez")