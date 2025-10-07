## Listas

persona1 = ["Pepe%Grillo", "Perez", 4, "41112222"] 
persona2 = ["Juan", "Sanchez", 12, "42223333"]

## Diccionarios

persona3 = {'nombre': "Pepe%Grillo", 'apellido': "Perez", 'edad': 14, 'telefono': "41112222"}

print("Imprimimos el nombre")
print(persona3['nombre'])

## Otra manera

print("Imprimimos el apellido")
print(persona3.get("apellido"))

## Imprimo las claves

print("Imprimo las claves")
print(persona3.keys())

## Imprimo los valores

print("Imprimo los valores")
print(persona3.values())

## Imprimo todo

print("Todo")
print(persona3.items())

## Longitud

print("Cantidad de elementos del diccionario")
print(len(persona3))

## Acá le decimos que agarre la clave y el valor en 0 y los meta en una lista, en la posición 0

print("Agarrá los valores en la posición 0 y metelos en una lista, en la misma posición")

key0, value0 = list(persona3.items())[0]

## Y los imprimimos

print(key0, value0)