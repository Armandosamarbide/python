## Patrón observador: los observadores (?) están como "espiando" el tema

## Un tema (Subject) mantiene un estado
## Varios observadores (Observers) están "espiando" ese tema
## Cuando el estado del tema cambia, todos los observadores son notificados
## El objeto les avisa cuando hay cambios

## Clase base del objeto observado

class Subject:
    def __init__(self):
        self.observadores = []

    ## Registra un observador
    
    def agregar(self, obj):
        self.observadores.append(obj)
        
    ## Elimina un observador

    def quitar(self, obj):
        self.observadores.remove(obj)

    ## Recorre los observadores y llama a update()
    
    def notificar(self):
        for observador in self.observadores:
            observador.update()

## Subject

class TemaConcreto(Subject):
    def __init__(self):
        super().__init__() ## Inicializa la lista de observadores
        self.estado = None

    def set_estado(self, value):
        self.estado = value
        self.notificar()

    def get_estado(self):
        return self.estado


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self):
        print("Actualización dentro de Observador ConcreteObserverA")
        self.estado = self.observado_a.get_estado()
        print("Estado =", self.estado)
        
class ConcreteObserverB(Observador):
    def __init__(self, obj):
        self.observado_b = obj
        self.observado_b.agregar(self)

    def update(self):
        print("Actualización dentro de Observador ConcreteObserverB")
        self.estado = self.observado_b.get_estado()
        print("Estado =", self.estado)


tema1 = TemaConcreto()
observador_a = ConcreteObserverA(tema1)
observador_b = ConcreteObserverB(tema1)
tema1.set_estado(1)