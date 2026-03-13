def menu():
    opcion = 0
    while opcion < 1 or opcion > 4:
        print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 4:
            print("La opcion ingresada no es válida")
    return opcion
        

operacion = menu()
print(f"El usuario eligió la opción {operacion}")
