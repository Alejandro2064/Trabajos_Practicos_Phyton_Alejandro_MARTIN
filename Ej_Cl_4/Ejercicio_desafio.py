import os
print( "\033[H\033[J")
"""
Escribir una función que reciba una lista con los nombres de los alumnos de un curso, 
sus promedios y el valor mínimo necesario para aprobar y muestre solamente los que 
no deben recursar la materia, ordenados por orden alfabético.
"""

def curso():
    nombres = []
    notas = []
    cant = int(input("Ingrese la cantidad de alumnos "))
    #aprobar = float(input("Ingrese la nota mínima para aprobar "))
    for i in range(cant):
        nombre = input("Ingrese el nombre del alumno ")
        nombres.append(nombre)
        nota = float(input("Ingrese la nota "))
        notas.append(nota)
    cls = lambda:os.system('cls')
    cls()
    print("Las datos ingresados son")
    print(" ")
    nombres.sort()
    for i in range(cant):
        print("La nota de",nombres[i], "es: ",notas[i])
    """a = dict(zip(nombres, notas))
    if a.items > aprobar:
        print(a)
        """
    return()
    
# Programa principal

curso()