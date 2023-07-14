print( "\033[H\033[J")

#Escribir un programa que permita ingresar dos números por
#  pantalla y muestre como resultado la division entera
#  entre ellos y el resto. ¿Y cómo sería si hacemos una
#  división común?

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

coc = num1 // num2
resto = num1 % num2
div = num1 / num2

print("Cociente", coc)
print("Resto", resto)
print("Division", round(div,2))