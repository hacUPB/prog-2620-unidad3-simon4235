compra = int(input("Ingrese el valor de la compra: "))
envio = 0
if compra < 100000:
    envio = 9000
total = compra + envio
print (f"El valor a pagar es ${total}")