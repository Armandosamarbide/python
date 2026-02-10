## En este formulario se hace el alta de nuevos registros.

import tkinter as tk
import re
from crearbase import BBDD
from utilidades import Utilidades
from decoradores import log_actividad

class NuevoDisco:
    
    def __init__(self, frame_center, text_output, entradas):
        self.frame_center = frame_center
        self.text_output = text_output
        self.entradas = entradas

    def mostrar_formulario(self):
            
        Utilidades.limpiar_frame_center(self.frame_center, self.text_output)

        tk.Label(self.frame_center, text="Dar de alta un nuevo disco",
                font=("Arial", 14, "bold")).pack(pady=10)

        for campo in ["Título", "Artista", "Año", "Género"]:
            fila = tk.Frame(self.frame_center)
            fila.pack(pady=3, padx=78)

            tk.Label(fila, text=f"{campo}:", width=25, anchor="w").pack(side="left")

            var = tk.StringVar()
            tk.Entry(fila, textvariable=var, width=40).pack(side="left")

            self.entradas[campo] = var

        tk.Button(self.frame_center, text="Guardar",
                command=self.guardar_registro).pack(pady=15)

    @log_actividad
    def guardar_registro(self):
        titulo = self.entradas["Título"]
        artista = self.entradas["Artista"]
        anio = self.entradas["Año"]
        genero = self.entradas["Género"]

        patron = r"^[A-Za-záéíóúÁÉÍÓÚñÑ0-9 ]+$"

        if re.match(patron, titulo.get()) and re.match(patron, artista.get()):
            con = None
            cursor = None
            try:
                con = BBDD.crear_conexion()
                cursor = con.cursor()

                sql = """INSERT INTO listadiscos(titulo, artista, anio, genero)
                        VALUES (%s, %s, %s, %s)"""
                data = (titulo.get(), artista.get(), anio.get(), genero.get())

                cursor.execute(sql, data)
                con.commit()

                self.text_output.insert(tk.END, f"Registro agregado: {data}\n")

            except Exception as e:
                self.text_output.insert(tk.END, f"Error al guardar el registro: {e}\n")

            finally:
                if cursor is not None:
                    cursor.close()
                if con is not None:
                    con.close()

        else:
            self.text_output.insert(tk.END, "Error en los campos Título o Artista\n")