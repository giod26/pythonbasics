class Persona:

    def __init__(self):
        self.edad = 18
        self.nombre = "Juan"
        print("Se ha creado a " + self.nombre + " de " + str(self.edad))
    def hablar(self, ** palabras):
        for frase in palabras:
            print(self.nombre + ": " + palabras[frase])

juan = Persona()
juan.hablar()
juan.hablar(t1 = "Hola, esto es una prueba", t2 = "Estoy hablando otra vez")