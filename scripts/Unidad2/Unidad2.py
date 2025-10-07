# WHILE

""" x = 0
vuelta = 1
while x < 30:
    x += 6
    print("En la vuelta #" + str(vuelta) + ", X: " + str(x))
    vuelta += 1
else:
    x1 = str(x)
    print("Terminamos cuando x vale: " + x1) """
    
""" ----------------------------"""
    
""" x = input("Ingrese una cifra ")

print(type(x))
x= int(x)
print(type(x))

x /= 2

print(x) """

#IF-THEN-ELSE-ELSIF

import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

edad = input("Ingrese edad")

edad = int(edad)

if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")