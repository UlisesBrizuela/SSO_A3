#Actividad 3 - Seminario de solucion de problemas de sistemas operativos
#Brizuela Arias Ulises Israel
import os
import sys
from time import sleep


def menu(): 
    os.system('cls')
    try:
        m = int(input("""
        SELECCIONA UNA OPCION.

        1.- ROUND ROBIN
        2.- SJF
        3.- FIFO
        4.- PRIORIDADES
        0.- SALIR
        
        : """))

        if m == 1: 
            print("opcion 1")
        elif m == 2: 
            print("opcion 2")
        elif m == 3: 
            print("opcion 3")
        elif m == 4: 
            print("opcion 4")
        elif m == 0:
            os.system('cls')
            sys.exit();
        else:
            print("Opcion Invalida")
            sleep(1)
            menu()

    except ValueError: 
        print("Dato invalido")
        sleep(1)
        menu()


if __name__ == "__main__":
    menu()