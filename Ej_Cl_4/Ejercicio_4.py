print( "\033[H\033[J")

def iva ():
    monto= float(input("Ingrese el monto "))
    porcIva = float(input("Ingrese el porcentaje de Iva "))
    a = monto + (monto * porcIva/100)
    print("El valor final con Iva es: $", a)
    return 

# Programa principal

iva()

