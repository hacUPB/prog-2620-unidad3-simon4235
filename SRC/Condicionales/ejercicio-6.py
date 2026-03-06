peso = float(input("Ingrese el peso de su paquete (gramos): "))
if peso > 5000:
    print("El peso del paquete excede el peso máximo")
else:
    zona = int(input("Ingrese la zona a la que se dirige el paquete: "))
    if zona > 5 or zona < 1:
        print("La zona ingresada no es válida")
    else:
        match zona:
            case 1:
                costo = peso * 11
                print("La ubicación es América del norte")
            case 2:
                costo = peso * 10
                print("La ubicación es América Central")
            case 3:
                costo = peso * 12
                print("La ubicación es América del Sur")
            case 4:
                costo = peso * 24
                print("La ubicación es Europa")
            case 5:
                costo = peso * 27
                print("La ubicación es Asia")
print(f"El valor del envio es {costo}")