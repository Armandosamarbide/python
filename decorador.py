## Un decorador es una función que envuelve a otra función.

def mi_decorador(func):
    def envoltura():
        print("Antes")
        func()
        print("Después")
    return envoltura


@mi_decorador
def saludar():
    print("Hola")
    
    
class Usuario(): pass

print(type(Usuario))

