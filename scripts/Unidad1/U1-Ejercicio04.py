""" Ingresar dos valores, convertirlos a enteros y mostrarlos en una lista junto a su suma """

valor1 = input("Ingrese primer valor ")
valor2 = input("Ingrese segundo valor ")

v1 = int(valor1)
v2 = int(valor2)

lista = [v1, v2, v1 + v2]

print(lista)