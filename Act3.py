#Actividad 3 - Seminario de solucion de problemas de sistemas operativos
#Brizuela Arias Ulises Israel

from os import system 
from sys import exit
from collections import deque

def LeerArchivo():
    procesos = []
    with open("./procesos.txt", 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            proceso, ciclos, prioridad = linea.strip().split(',')
            procesos.append((proceso, int(ciclos), int(prioridad)))
    return procesos

def RoundRobin(procesos, Q):
    system('cls')
    cola = deque(procesos)
    while cola:
        proceso_actual = cola.popleft()
        nombre, quantum, p = proceso_actual
        print(f"Ejecuntando: {nombre}, con {quantum} quantum.")
        quantum -= Q
        if quantum > 0:
            cola.append((nombre, quantum, p))
            print(f"El proceso: {nombre} volvio a la cola con {quantum} quantum restantes.\n")
        else:
            print(f"Proceso {nombre} terminado.\n")
    input("presiona Enter para continuar...")
    Menu()

def SFJ(procesos):
    system('cls')
    cola = deque(sorted(procesos, key = lambda x: x[1]))
    while cola:
        proceso_actual = cola.popleft()
        nombre, tamaño, p = proceso_actual
        print(f"Proceso ejecutado: {nombre} con {tamaño} ciclos.\n")
    input("presiona Enter para continuar...")
    Menu()

def FIFO(procesos):
    system('cls')
    cola = deque(procesos)
    proceso_actual = cola.popleft()
    nombre, quantum, p = proceso_actual
    while cola:
        proceso_actual = cola.popleft()
        nombre, q, p = proceso_actual
        print(f"Proceso ejecutado: {nombre}.\n")
    input("presiona Enter para continuar...")
    Menu()

def Menu(): 
    system('cls')
    procesos = LeerArchivo()
    try:
        m = int(input("""
        SELECCIONA UNA OPCION.

        1.- ROUND ROBIN
        2.- SJF
        3.- FIFO
        4.- PRIORIDADES
        0.- SALIR
        
        # """))

        if m == 1:
            Quantum = 3
            RoundRobin(procesos, Quantum)
        elif m == 2: 
            SFJ(procesos)
        elif m == 3: 
            FIFO(procesos)
        elif m == 4: 
            print("opcion 4")
        elif m == 0:
            system('cls')
            exit();
        else:
            print("Opcion Invalida.")
            input("presiona Enter para continuar...")
            Menu()

    except ValueError: 
        print("Dato invalido.")
        input("presiona Enter para continuar...")
        Menu()


if __name__ == "__main__":
    Menu()