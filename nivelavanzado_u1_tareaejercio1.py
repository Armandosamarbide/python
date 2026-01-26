class Empleado:
    __slots__=['nombre', "__dict__"]

    def ver_nombre(self,):
        self.accion()

class Gerente(Empleado):
    def __init__(self, nombre):
        self.nombre = nombre
        self.apellido = ""
    #delegacion    
    def accion(self,):
        print("El nombre del Gerente del banco Bancor es: " + self.nombre)
    #uso sobrecarga __str__
    def __str__(self, ):
        return "El nombre del Gerente es: " + self.nombre
    def __add__(self, apellido):
        self.apellido = apellido
        return "El apellido del gerente es:" +  self.apellido
objeto1=Gerente("Jorge")
objeto1.ver_nombre()
print(objeto1)
objeto2 = objeto1 + " Bugliotti"
print(objeto2)
