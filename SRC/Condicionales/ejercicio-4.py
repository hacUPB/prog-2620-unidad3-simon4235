edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 125:
    if edad < 6:
        etapa = "Infancia"
    elif edad < 12:
        etapa = "Niñez"
    elif edad < 20:
        etapa = "Adolescencia"
    elif edad < 25:
        etapa = "Juventud"
    elif edad < 60:
        etapa = "Adultez"
    else:
        etapa = "Ancianidad"
    print(f"La etapa de la persona es {etapa}")
else:
    print("El número ingresado no es una edad válida")