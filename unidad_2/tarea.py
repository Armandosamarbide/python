class DescriptorEdad:

    def __set__(self, instance, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        elif valor >= 0 and valor < 18:
            print("Esta persona no puede trabajar\n")
        elif valor > 60 and valor < 65:
            print("Esta persona esta pronta a jubilarse\n")
        elif valor >= 65:
            print("Esta persona ya está jubilada\n")
        instance._edad = valor

    def __get__(self, instance, owner):
        print("Validando edad del empleado...\n")
        return instance._edad


class Empleados:
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario

    edad = DescriptorEdad()


gonzalo = Empleados("Gonzalo", "Lugo", 24, 1650000)
jaimito = Empleados("Jaimito", "Perez", 64, 1650000)
jaimita = Empleados("Jaimita", "Rodriguez", 65, 1800000)
alex = Empleados("Alex", "Gonzales", 16, 1500000)
alexa = Empleados("Alexa", "Martinez", -15, 1760000)