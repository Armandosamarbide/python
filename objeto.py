## Persona → clase (plantilla)
## p1, p2 → objetos
## __init__ → constructor
## self → referencia al objeto actual

class Disco:
    def __init__(self, titulo, artista, anio):
        self.titulo = titulo
        self.artista = artista
        self.anio = anio

    def descripcion(self):
        return f"{self.titulo} - {self.artista} ({self.anio})"

disco1 = Disco("Moving Pictures", "Rush", 1981)
disco2 = Disco("Operation: Mindcrime", "Queensrÿche", 1988)

print(disco1.descripcion())
print(disco2.descripcion())