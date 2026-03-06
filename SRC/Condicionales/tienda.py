# una tienda ofrece una promoción, por la compra de 3 artículos, el costo del elemento de menor valor tiene un descuento del 50%

articulo_1 = int(input("Ingrese el valor del primer artículo: "))
articulo_2 = int(input("Ingrese el valor del segundo artículo: "))
articulo_3 = int(input("Ingrese el valor del tercer artículo: "))
if articulo_1 < articulo_2:
    menor = articulo_1
elif articulo_2 < articulo_3 :
    menor = articulo_2
else:
    menor = articulo_3
total = articulo_1 + articulo_2 + articulo_3 - menor * 0.5
print(f"El valor total de la compra es {total}")