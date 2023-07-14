print( "\033[H\033[J")

def num_pares():
    lista = []
    lista_par = []
    cant = int(input("Ingrese la cantidad de numeros de la lista "))
    for i in range(cant):
        num = int(input("Ingrese un numero "))
        lista.append(num)
        if num % 2 == 0:
            lista_par.append(num)
    print ("Los numeros de la lista son", lista)
    print("Los numeros pares son", lista_par)
    return


    #Programa principal

num_pares()