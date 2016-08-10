edad = input("Ingresa tu edad: ")
genero = raw_input("Genero (M/F): ")
if(int(edad) >= 18):
     if(genero == "M" or genero == "m"):
          print("ID: " + "MA" + str(edad) + "+")
     else:
          print("ID: " + "FE" + str(edad) + "+")
else:
     if(genero == "F" or genero == "f"):
          print("ID: " + "Fe" + str(edad) + "-")
     else:
          print("ID: " + "Ma" + str(edad) + "-")