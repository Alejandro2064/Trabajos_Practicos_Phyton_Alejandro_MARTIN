print( "\033[H\033[J")

peso = int(input("Ingrese cuantos kilos pesa: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura**2)

print("El IMC de la persona es de", round(imc, 1))