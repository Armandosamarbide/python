# Escriba un programa que consulte al usuario si desea permanecer en el sitio web y si la respuesta es afirmativa imprimir en pantalla “Bienvenido”, 
# en caso contrario escribir en pantalla “Nos vemos pronto”

import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

saludo = input("Desea permanecer en el sitio web S/N ")

if saludo == "s" or saludo == "SS":
    print("Welcome")
elif saludo == "n" or saludo == "N":
    print("Hasta la próxima")
else:
    print("Opción inválida, vuelva a probar")