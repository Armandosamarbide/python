## Esta funcionalidad controla la búsqueda de elementos en la BBDD.

import tkinter as tk
from crearbase import BBDD
from utilidades import Utilidades
from decoradores import log_actividad


class BuscarDisco:
    def __init__(self, frame_center, text_output):
        self.frame_center = frame_center
        self.text_output = text_output
        self.var_termino = tk.StringVar()

    def mostrar_formulario(self):
        Utilidades.limpiar_frame_center(self.frame_center, self.text_output)

        tk.Label(self.frame_center, text="Búsqueda de disco", font=("Arial", 14, "bold")).pack(pady=10)

        fila = tk.Frame(self.frame_center)
        fila.pack(pady=5, padx=10, anchor="w")

        tk.Label(fila, text="Título o Artista:", width=25, anchor="w").pack(side="left")
        tk.Entry(fila, textvariable=self.var_termino, width=40).pack(side="left")

        tk.Button(self.frame_center, text="Buscar", command=self.ejecutar_busqueda).pack(pady=15)

    @log_actividad
    def ejecutar_busqueda(self):
        termino = self.var_termino.get()

        if not termino:
            self.text_output.insert(tk.END, "No se ingresó un término de búsqueda.\n")
            return

        con = BBDD.crear_conexion()
        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM listadiscos WHERE titulo LIKE %s OR artista LIKE %s",
            (f"%{termino}%", f"%{termino}%")
        )
        resultados = cursor.fetchall()

        if resultados:
            self.text_output.insert(tk.END, "Resultados de búsqueda:\n")
            for r in resultados:
                self.text_output.insert(tk.END, f"ID: {r[0]}, Título: {r[1]}, Artista: {r[2]}, Año: {r[3]}, Género: {r[4]}\n")
        else:
            self.text_output.insert(tk.END, "No se encontraron registros que coincidan con la búsqueda solicitada.\n")

        cursor.close()
        con.close()