# Genere una constante de texto que será la contraseña. luego pida al usuario que ingrese la contraseña. Mientras la constraseña no sea la correcta, debe continuar a pedir la contraseña. Si esta es correcta, se deja continuar al resto del programa

contador = 0
contraseña = "123"
entrada = input("Ingrese la contraseña: ")
while entrada != contraseña and contador < 3:
    entrada = input("Ingrese la contraseña: ")
print("Ha podido acceder al programa")