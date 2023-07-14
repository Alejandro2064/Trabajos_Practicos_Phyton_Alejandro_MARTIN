print( "\033[H\033[J")

harina = float(input("Ingrese los kilos de harina "))
azucar = float(input("Ingrese los kilos de azúcar "))
manteca = float(input("Ingrese los kilos de manteca "))

if harina>= 5 and azucar >= 1 and manteca >= 2:
    print("Puede realizar la receta")
if harina < 5:
    print("Falta harina debe completar 5 kilos")
if azucar < 1:
    print("Falta azúcar debe completar 1 kilo")
if manteca < 2:
    print("Falta manteca debe completar 2 kilos")
