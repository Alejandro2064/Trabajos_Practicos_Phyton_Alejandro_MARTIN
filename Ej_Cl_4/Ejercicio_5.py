print( "\033[H\033[J")

def promedio ():
    lista=[]
    suma = 0
    cant = int(input("Ingrese la cantidad de números de la lista "))
    for i in range(cant):
        num = float(input("Ingrese el número "))
        lista.append(num)
        suma = suma + num
    prom = suma/cant
    print("La lista es", lista)
    print ("El promedio de los valores de la lista es",prom)
    return 

# Programa principal

promedio()



