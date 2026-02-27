promedio = float(input("Ingresar promedio: "))
nivel_socioeconomico = int(input("Ingresar nivel socioeconomico: "))
beca = promedio >= 9 or (promedio > 8 and nivel_socioeconomico == 1)
print("Puedes ser becado?", beca)