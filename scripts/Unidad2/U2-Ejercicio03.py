# Escriba un programa que consulte por la edad de la persona e informe:
# Si la persona no está en edad de trabajar.
# Si la persona está en edad de trabajar, con su edad.
# Si la persona está a un año de jubilarse.

import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

edad = input("Ingrese edad ")
edad = int(edad)

if edad >= 16 and edad != 64:
    print("Legalmente habilitado para trabajar")
elif edad >= 16 and edad == 64:
    print("Legalmente inhabilitado para trabajar, a un año de edad legal de jubilación")
elif edad < 16:
        print("No habilitado legalmente para trabajar")
    