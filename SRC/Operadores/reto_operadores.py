edad_usuario = int(input("Edad del usuario: "))
saldo_billetera = float(input("Saldo en la billetera: "))
tiene_suscripcion_premium = bool(input("Tiene suscripción Premium? "))
edad_minima = 17
precio_juego = 60
descuento = 0.1
compra_exitosa = edad_usuario >= edad_minima \
and (saldo_billetera >= precio_juego \
or (tiene_suscripcion_premium \
and saldo_billetera >= precio_juego*descuento))
print("Puede comprar el juego?", compra_exitosa)