print( "\033[H\033[J")

num = int(input("Ingresar un número "))

if num % 2 == 0:
    print("El numero es par")
else:
    print("El número es impar")
