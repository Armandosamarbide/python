import tkinter as tk
import tkinter.font as tkFont

from crearbase import BBDD
from alta import AltaDisco
from baja import BajaDisco
from modificacion import ModificarDisco
from busqueda import BuscarDisco
from listartodo import ListarTodos
from utilidades import Utilidades


class InterfazApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Disquería EL PALACIO DE LA MÚSICA")
        self.root.geometry("800x800")

        self._configurar_frames()
        self._configurar_widgets()

        BBDD.crear_tabla()
        Utilidades.mostrar_inicio(self.frame_center, self.text_output)

    def _configurar_frames(self):
        self.frame_left = tk.Frame(self.root, bg="#434966", width=200)
        self.frame_left.pack(side="left", fill="y")

        self.frame_center = tk.Frame(self.root, bg="white")
        self.frame_center.pack(side="left", fill="both", expand=True)

        self.text_output = tk.Text(self.frame_center, wrap="word")
        self.text_output.pack(fill="both", expand=True, padx=10, pady=10)

        self.entradas = {}

    def _configurar_widgets(self):
        fuente = tkFont.Font(weight="bold", family="Courier", size=10)

        botones = [
            ("Alta", lambda: AltaDisco(self.frame_center, self.text_output, self.entradas).mostrar_formulario()),
            ("Baja", lambda: BajaDisco(self.frame_center, self.text_output).mostrar_formulario()),
            ("Modificación", lambda: ModificarDisco(self.frame_center, self.text_output, self.entradas).mostrar_formulario_busqueda()),
            ("Búsqueda", lambda: BuscarDisco(self.frame_center, self.text_output).mostrar_formulario()),
            ("Mostrar todo", lambda: ListarTodos(self.text_output).mostrar()),
            ("Limpiar pantalla", lambda: Utilidades.limpiar_pantalla(self.text_output, self.frame_center)),
            ("Quit", lambda: Utilidades.salir(self.root)),
        ]

        for texto, comando in botones:
            tk.Button(
                self.frame_left,
                text=texto,
                font=fuente,
                width=17,
                height=2,
                command=comando
            ).pack(padx=10, pady=10)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = InterfazApp()
    app.run()
