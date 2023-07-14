print( "\033[H\033[J")


monto = int(input("Ingrese el monto a depositar: "))
tiempo = int(input("Ingrese el periodo en años: "))

plazoFijo = monto + ((monto * ((1 + 0.5) ** tiempo - 1)))

print(" ")
print("*** Plazo Fijo - Interes del 0.50 % anual ***")
print(" ")
print("Los dividendos del Plazo Fijo son: ", round(plazoFijo, 2))
print(" ")
print("*** Bonos y Acciones de la Bolsa - Intreres del 0.25 % semestral ***")
print(" ")

bono = monto + ((monto * ((1 + 0.25) ** (tiempo*2) - 1)))

print("Los dividendos de los Bonos son: ", round(bono, 2))
print(" ")
print("Conviene la inversion en Bonos")
print(" ")



