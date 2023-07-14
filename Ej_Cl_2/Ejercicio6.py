print( "\033[H\033[J")

numero1 = int(input("Ingrese un numero positivo: "))
numero2 = int(input("Ingrese un numero positivo: "))

resultSinExtrem = (numero2 * (numero2 + 1) / 2) - ((numero1-1) * ((numero1-1)+1) / 2) - numero1 - numero2
resultExtrem = (numero2 * (numero2 + 1) / 2) - ((numero1-1) * ((numero1-1)+1) / 2)

print("El resultado de la suma sin extremos es:",int(resultSinExtrem))
print("El resultado de la suma con extremos es:",int(resultExtrem))


