## Esta funcionalidad controla la eliminación de registros de la BBDD.

import tkinter as tk
from crearbase import BBDD
from utilidades import Utilidades
from decoradores import log_actividad

class BorrarDisco:
    def __init__(self, frame_center, text_output):
        self.frame_center = frame_center
        self.text_output = text_output
        self.var_titulo = tk.StringVar()

    def mostrar_formulario(self):
        Utilidades.limpiar_frame_center(self.frame_center, self.text_output)

        tk.Label(self.frame_center, text="Baja de disco",
                font=("Arial", 14, "bold")).pack(pady=10)

        fila = tk.Frame(self.frame_center)
        fila.pack(pady=5, padx=10, anchor="w")

        tk.Label(fila, text="Título EXACTO del disco a borrar:",
                width=25, anchor="w").pack(side="left")

        tk.Entry(fila, textvariable=self.var_titulo, width=40).pack(side="left")

        tk.Button(self.frame_center, text="Buscar",
                command=self.ejecutar_baja).pack(pady=15)

    @log_actividad
    def ejecutar_baja(self):
        titulo = self.var_titulo.get()

        if not titulo:
            self.text_output.insert(tk.END, "Debe ingresar un título.\n")
            return

        con = None
        cursor = None

        try:
            con = BBDD.crear_conexion()
            cursor = con.cursor()

            cursor.execute("SELECT * FROM listadiscos WHERE titulo = %s", (titulo,))
            registros = cursor.fetchall()

            if not registros:
                self.text_output.insert(tk.END, "No se encontró el disco solicitado.\n")
            else:
                for r in registros:
                    cursor.execute("DELETE FROM listadiscos WHERE id = %s", (r[0],))
                    con.commit()
                    self.text_output.insert(tk.END, "Registro eliminado.\n")

        except Exception as e:
            self.text_output.insert(tk.END, f"Error al eliminar el disco: {e}\n")

        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()