from Tkinter import *

class Interfaz:

    def __init__(self, contenedor):
        self.e1 = Label(contenedor, text = "Etiqueta1", fg = "black", bg = "white")
        self.e1.pack()

ventana = Tk()
miInterfaz = Interfaz(ventana)
ventana.mainloop()