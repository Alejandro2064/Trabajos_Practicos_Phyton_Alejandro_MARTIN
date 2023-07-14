print( "\033[H\033[J")

# Escribir una función que reciba una lista de números y devuelva otra lista 
# con el cuadrado de cada uno de sus componentes.

def cuadrado ():
    lista=[]
    lista_cuadr = []
    cant = int(input("Ingrese la cantidad de números de la lista "))
    for i in range(cant):
        num=float(input("Ingrese un número "))
        lista.append(num)
        cuadr = num ** 2 
        lista_cuadr.append(cuadr)
    print("La lista ingresada es " , lista)
    print("La lista con sus números al cuadrado es ", lista_cuadr)
    return
    
    #Programa principal
cuadrado()
