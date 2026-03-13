def factorial(numero):
    if numero < 0: 
        return print("No se puede realizar la operación factorial con números negativos")
    elif numero == 0:
        return 1
    else:
        acumulador = 1
        for factor in range(1, numero + 1):
            acumulador *= factor
        return acumulador
entrada = int(input("Ingrese el valor al cual desea ejecutar el factorial: "))
resultado = factorial(entrada)
print(resultado)