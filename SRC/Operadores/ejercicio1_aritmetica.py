cuenta = float(input("Cuenta: "))
personas = int(input("Numero de personas: "))
propina = cuenta*0.15
total = cuenta + propina
pago_individual = total/personas
print("Total: ", total)
print("Propina: ", propina)
print("Pago individual: ", pago_individual)