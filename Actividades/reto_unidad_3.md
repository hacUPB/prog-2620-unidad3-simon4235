# Reto unidad 3
Simón Alvarez  
Edilberto Contreras  

### Pseudocódigo:

inicio  

leer combustible_inicial  
combustible_actual = combustible_inicial  
reserva_legal = 1500  
tramo_actual = 0  
consumo_total = 0  
distancia_total = 0
consumo_por_kilometro = 2.5  
consumo_headwind = 1.2  
consumo_tailwind = 0.83  

mientras combustible_actual > reserva_legal  
    tramo_actual = tramo_actual + 1  
    leer distancia_tramo  
    leer direccion_viento  
    si direccion_viento == headwind  
        consumo_tramo = consumo_por_kilometro * distancia_tramo * consumo_headwind  
    si no  
        si dreccion_viento == tailwind  
            consumo_tramo = consumo_por_kilometro * distancia_tramo * consumo_tailwind  
        si no  
            consumo_tramo = consumo_por_kilometro * distancia_tramo  
        fin si  
    fin si  

    combustible_actual = combustible_actual - consumo_tramo
    consumo_total = consumo_total + consumo_tramo
    distancia_total = distancia_total + distancia_tramo

    imprimir tramo_actual  
    imprimir consumo_tramo  
    imprimir combustible_actual

    si combustible_actual > reserva_legal
        imprimir "Este tramo se puede realizar de manera segura"
    fin si
fin mientras

imprimir "Alerta, el combusible ha llegado a la reserva legal, el avión aterrizará en el aeropuerto mas cercano"  
imprimir tramo_actual
imprimir combustible_actual  
imprimir consumo_total  
imprimir distancia_total  

fin

