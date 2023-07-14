print( "\033[H\033[J")

def factorial(num):
    if num == 0:
        return 1
    else:
        a = 1
    for i in range(1, num + 1):
        a = a * i
    return a

# Programa principal

n= int(input("Ingrese numero "))
print(factorial(n))