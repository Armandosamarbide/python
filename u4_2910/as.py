class Usuarios:

    def __init__(self, nombre):
        self.nombre = nombre

    def login(self,):
        print(self.nombre)

    @classmethod
    def metodo1(cls,):
        print("hola")    

    @staticmethod
    def rutina(a, b):
        print(a+b)




obj = Usuarios("Anna")
print(obj.login())
obj2 = Usuarios("Pedro")
print(obj2.login())

print(Usuarios.metodo1())