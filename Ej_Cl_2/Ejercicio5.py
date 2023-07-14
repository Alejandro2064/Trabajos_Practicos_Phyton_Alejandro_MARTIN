print( "\033[H\033[J")

cantPers = int(input("Ingrese la cantidad de personas: "))
dinPorPers = int(input("ingrese el dinero de cada comensal: "))
precioPlato = int(input("Ingrese el precio del plato: "))

cantPlatos = cantPers * dinPorPers / precioPlato
vuelto = (cantPers * dinPorPers) - (int(cantPlatos) * precioPlato)

print("La cantidad de platos a consumir son:", int(cantPlatos))
print("El vuelto es $", vuelto)
