print( "\033[H\033[J")

password = str

while password != "123456":
    password = input("Ingrese contraseña ")
    if password == "123456":
        print("Contraseña correcta. Ingreso aceptado")

    else:
        print("Contraseña incorrecta. Vuelva a intentar")

