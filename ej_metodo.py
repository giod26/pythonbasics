class Persona:

    def __init__(self):
        self.edad = 18
        self.nombre = "Juan"
        print("Se ha creado a " + self.nombre + " de " + str(self.edad))
    def hablar(self,palabras = "Ni idea de que hablar"):
        print(self.nombre + ": " + palabras)

juan = Persona()
juan.hablar()
juan.hablar("Hola, esto es una prueba")