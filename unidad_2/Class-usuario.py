class DescriptorUsuario:
    "Documentación para el descriptor"
    def __get__(self, instance, owner):
        print('Recuperar al usuario')
        print(self, instance, owner)
        return instance.__usuario.upper()
    
    def __set__(self, instance, valor):
        print('Modificar usuario')
        instance._usuario=valor
        
    def __delete__(self, instance, valor):
        print('Para borrar el usuario')
        instance._usuario=valor

class Usuario:
    
    def __init__(self, usuario):
        self._usuario = usuario
        
    def get_usuario(self,):
        return self._usuario
    
    def set_usuario(self, valor):
        print('Modificar usuario')
        self._usuario = valor
    
    def del_usuario(self,):
        print('remover el usuario')
        del self._usuario
        
    usuario=property(get_usuario, set_usuario, del_usuario, 'Datos a manejar')

## Descriptor: 

## Property (Es una clase especial de descriptor): una forma de acceder a los atributos de instancia para mirar, modificar o borrar.
