# Escriba un programa que solicite el ingreso de un número y muestre en pantalla si es par o impar. 


import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

num = input("Ingrese número ")
num = int(num)

if num % 2 == 0 and num != 0:
    print("Par")
elif num % 2 != 0:
    print("Impar")
else:
    print("Cero")