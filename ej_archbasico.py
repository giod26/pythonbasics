def escribir(dat1,dat2,dat3):
    texto = open('prueba.txt', 'w')
    texto.write(dat1)
    texto.write(dat2)
    texto.write(dat3)
    print("\nSe escribio en el archivo")
    texto.close()

escribir("Hola ", "mundo ", "feliz")

def leer():
    texto = open("prueba.txt", "r")
    print(texto.read())
    texto.close()

leer()
