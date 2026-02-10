## Patrón Singleton: Cuando necesitamos que unicamente una instancia se encuentre seleccionable
## Cuando solo queremos que un usuario exista a la vez

class Usuarios():
    class __Usuarios:
        def __init__(self,):
            self.usuario=None
            
        def __str__(self):
            return repr(self)+ "--- "+self.usuario
        
        def imprimir(self,):
            print("Hola")
            
    instancia=None
    
    def __new__(cls):
        if not Usuarios.instancia:
            Usuarios.instancia=Usuarios.__Usuarios()
            
        return Usuarios.instancia
    
ana = Usuarios()
ana.usuario="anita"
print(ana)
print(ana.imprimir())
print("---"*23)
pedro = Usuarios()
pedro.usuario="pedrito"
print(pedro)
print(pedro.imprimir())



