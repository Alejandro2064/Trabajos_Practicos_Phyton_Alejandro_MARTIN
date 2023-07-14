print( "\033[H\033[J")



fecha_nac = int(input("Ingrese su año de nacimiento "))
if fecha_nac <= 2005:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
