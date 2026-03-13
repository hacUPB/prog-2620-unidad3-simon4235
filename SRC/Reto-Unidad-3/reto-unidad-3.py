combustible_inicial = float(input("Ingrese el combustible inicial en Kg: "))
combustible_actual = combustible_inicial
reserva_legal = 1500 #La reserva legal de un a320 son 1500 Kg
consumo_por_kilometro = 2.5 #El consumo promedio de un a320 son 2.5 Kg por Km
consumo_headwind = 1.2 #El consumo durante un headwind aumenta en un 20% (100% + 20%)
consumo_tailwind = 0.83 #El consumo durante un tailwind se reduce en un 17% (100% - 17%)
direccion_viento = ""
tramo_actual = 0
consumo_tramo = 0
consumo_total = 0
distancia_tramo = 0
distancia_total = 0

def calcular_consumo_tramo(distancia_tramo, direccion_viento):
    if direccion_viento == "headwind": #Consumo durante un headwind
        consumo_tramo = consumo_por_kilometro * distancia_tramo * consumo_headwind
    elif direccion_viento == "tailwind":#Consumo durante un tailwind
        consumo_tramo = consumo_por_kilometro * distancia_tramo * consumo_tailwind
    else: #Consumo sin viento, o con un crosswind
        consumo_tramo = consumo_por_kilometro * distancia_tramo
    return consumo_tramo

for tramo_actual in range(1, 6): #For, para repetir la funcion cinco veces
    distancia_tramo = float(input(f"Ingrese la distancia del tramo {tramo_actual} en Km: "))
    direccion_viento = str(input(f"Ingrese la dirección del viento del tramo {tramo_actual} (Headwind, Tailwind, Crosswind, None): ")).lower()
    
    consumo_tramo = calcular_consumo_tramo(distancia_tramo, direccion_viento) #Se reemplaza la variable por el return de la función

    combustible_actual -= consumo_tramo
    consumo_total += consumo_tramo
    distancia_total += distancia_tramo

    if combustible_actual > reserva_legal: #Este condicional determina si el tramo es seguro, de lo contrario sale del for
        print("Este tramo se puede realizar de manera segura")
    else:
        break

    print("Tramo Actual: ",tramo_actual)
    print(f"Consumo Tramo {tramo_actual}: {consumo_tramo} Kg")    
    print(f"Combustible Actual: {combustible_actual} Kg")

if combustible_actual > reserva_legal:
    print("El aterrizaje fue exitoso")
else:
    print("Alerta, el combustible ha llegado a la reserva lega. El avión no fue capaz de completar el vuelo y aterrizará en el aeropuerto más cercano")

print(f"Se logró llegar al tramo: {tramo_actual}")
print(f"El combustible restante fue: {combustible_actual} Kg")
print(f"El consumo total fue: {consumo_total} Kg")
print(f"La distancia total fue: {distancia_total} Km")



    