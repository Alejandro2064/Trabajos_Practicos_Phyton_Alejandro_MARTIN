print( "\033[H\033[J")

print("Lo que le dijo el amigo es verdad. A continuacion la demostracion")
print(" ")

monto = int(input("Ingrese el monto a depositar: "))
tiempo = int(input("Ingrese el periodo en años: "))

plazoFijo_50 = monto + ((monto * ((1 + 0.5) ** tiempo - 1)))

print(" ")
print("*** Plazo Fijo - Interes del 0.50 % anual (Con cobro de dividendos anuales) ***")
print(" ")
print("Los dividendos del Plazo Fijo son: ", round(plazoFijo_50, 2))
print(" ")

print("*** Plazo Fijo - Interes del 0.42 % anual (Con cobro de dividendos mensuales de 3.5 %) ***")
print(" ")

plazoFijo_42 = monto + ((monto * ((1 + 0.035) ** (tiempo*12) - 1)))

print("Los dividendos del Plazo Fijo son: ", round(plazoFijo_42, 2))
print(" ")