print( "\033[H\033[J")

num = int(input("Ingrese un número "))
if num % 2 == 1:    
    for i in range (1, num + 1, 2):
        for j in range (1, i + 1, 2):
            print(j, end=" " )
        print (" ")
    print(" ")  
    for i in range (1, num + 1, 2):
        for j in range (i, -1, -2):
            print(j, end = " " )
        print (" ")
elif num % 2 == 0:
    for i in range (0, num + 1, 2):
            for j in range (0, i + 1, 2):
                print(j, end=" " )
            print (" ")
    print(" ")  
    for i in range (0, num + 1, 2):
        for j in range (i, -1, -2):
            print(j, end = " " )
        print (" ")
