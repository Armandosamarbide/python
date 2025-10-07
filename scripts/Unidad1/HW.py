""" import sys

#Imprime HELLO WORLD
print("Hello World")
print(sys.version)
if 1>2: 
    print("Culo")
else:
    print("Caca") """
    
""" lista1 = ["manzana","banana","mandarina","ananá","frutilla","cereza","arándano"]
lista2 = ["manzana", 3, 4.5, "casa", [4, 7, "auto"] ]

print(lista1[2])

print(lista2[4]) """

"""
Si quiero poner dos strings o más juntos, se unen (concatenan) mediante el signo de más.

Ejercicio 2
. 
Cree una lista de frutas de 2 elementos, y realice un programa que muestre 
una oración conteniendo los dos elementos de la lista concatenándolos 
con texto para formar una oración con sentido.           	

"""


""" print("Me gusta la " + frutas[0] + " y la " + frutas[1]) """

""" print(frutas[0], 3) """

import random

frases = ["Me gusta la ", "Quiero una ", "Sueño con "]

frutas = ["uva", "pera", "manzana", "mandarina"]

frase = random.sample(frases,1)[0]

fruta = random.sample(frutas,1)[0]

print(frase + fruta )