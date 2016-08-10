telef = raw_input("Tienes telefono: ")

if 'si'in telef:
    opc1 = raw_input("Fijo o movil: ")
    if 'fijo' in opc1:
        print("Te marco por la noche")
    elif 'movil' in opc1:
        print("Te mando whats")
else:
    print("te veo despues")