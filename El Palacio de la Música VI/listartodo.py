
## Esta funcionalidad lista todos los registros en la BBDD

import tkinter as tk
from crearbase import BBDD


class ListarTodos:
    def __init__(self, text_output):
        self.text_output = text_output

    def mostrar(self):
        con = BBDD.crear_conexion()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM listadiscos")
        registros = cursor.fetchall()

        self.text_output.insert(tk.END, "=== TODOS LOS DISCOS (Título, Artista, Año, Género) ===\n")

        for r in registros:
            self.text_output.insert(tk.END, f"{r[1]}, {r[2]}, {r[3]}, {r[4]}\n")

        self.text_output.insert(tk.END, "\n")
        cursor.close()
        con.close()