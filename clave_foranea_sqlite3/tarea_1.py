"""
 En donde:
1)	 La clase padre tenga un método de instancia llamado “ver_nombre”, 
que permita ver el nombre del empleado 
2)	La clase hija permita durante la instanciación, instanciar el atributo nombre 
(Está instancia la llamaremos objeto1)
3)	La clase hija implemente el método __str__ para presentar un mensaje que contenga 
el nombre del usuario cada vez que se invoque el objeto1.
4)	La clase hija implemente el método __add__ de forma de poder crear una segunda
 instancia objeto2 que apunte a la primera “objeto1” y le agregue un apellido.
5)	Visualice el apellido en pantalla. 

"""

class Empleados(): 
    def __init__(self, nombre):
        self.nombre=nombre

    def ver_nombre(self,):
        print("El empleado es: " + self.nombre)


class Gerente(Empleados): 
    def __str__(self, ):
        return "El nombre es: " + self.nombre

    def __add__(self, dato):
        return self.nombre + " " + dato

obj1=Gerente("Nico")
obj1.ver_nombre()
print("---"*23)
print(obj1)
print("---"*23)
obj2 = obj1 + "Perez"
print(obj2)