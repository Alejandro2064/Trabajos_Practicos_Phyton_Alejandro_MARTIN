print( "\033[H\033[J")
jubilado = str

edad = int(input("Ingrese su edad "))
if edad >18:
    jubilado = input("Si es jubilado ingrese (si): ")

if jubilado == "si":
    print("Debe pagar $ 500")
elif edad < 2:
    print("El ingreso es gratis")
elif edad <= 4:
    print("Debe pagar $ 100")
elif edad <= 10:
    print("Debe pagar $ 200")
elif edad <= 18:
    print("Debe pagar $ 400")
elif edad > 18:
    print("Debe pagar $ 1000")



