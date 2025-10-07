persona1 = ["Pepe%Grillo", "Perez", 4, "41112222"] 
persona2 = ["Juan", "Sanchez", 12, "42223333"]

empleados= []
empleados.extend([persona1,persona2])

## print(empleados)

## Split se usa para partir, el argumento que recibe es el elemento a partir del cual lo debo partir. Otro podría ser un ".", un ","

print(persona1[0].split("%")[-1])



