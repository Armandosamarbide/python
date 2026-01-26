from modelo import Abmc
objmodelo = Abmc()
class Controlador():

    def alta_controlador(self, nombre, apellido, telefono):
        return objmodelo.alta(nombre, apellido, telefono)

    def borrar_controlador(self, mi_id):
        return objmodelo.borrar_por_id(mi_id)

    def consultar_controlador(self, nombre):
        return objmodelo.consultar_por_nombre(nombre)

    def obtener_todos(self, ):
        return objmodelo.consultar_todos()
