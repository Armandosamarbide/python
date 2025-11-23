import tkinter as tk
from crearbase import BBDD
from utilidades import Utilidades


class ModificarDisco:
    def __init__(self, frame_center, text_output, entradas):
        self.frame_center = frame_center
        self.text_output = text_output
        self.entradas = entradas
        self.var_titulo = tk.StringVar()
        self.id_registro = None

    def mostrar_formulario_busqueda(self):
        Utilidades.limpiar_frame_center(self.frame_center, self.text_output)

        tk.Label(self.frame_center, text="Modificar Disco", font=("Arial", 14, "bold")).pack(pady=10)

        fila = tk.Frame(self.frame_center)
        fila.pack(pady=5, padx=10, anchor="w")

        tk.Label(fila, text="Título a modificar:", width=25, anchor="w").pack(side="left")
        tk.Entry(fila, textvariable=self.var_titulo, width=40).pack(side="left")

        tk.Button(self.frame_center, text="Buscar", command=self.ejecutar_busqueda).pack(pady=25)

    def ejecutar_busqueda(self):
        titulo_buscado = self.var_titulo.get()

        if not titulo_buscado:
            self.text_output.insert(tk.END, "Debe ingresar un título.\n")
            return

        con = BBDD.crear_conexion()
        cursor = con.cursor()

        cursor.execute("SELECT * FROM listadiscos WHERE titulo = %s", (titulo_buscado,))
        registro = cursor.fetchone()

        if registro:
            self.mostrar_formulario_modificacion(registro)
        else:
            self.text_output.insert(tk.END, "No se encontró ningún disco.\n")

        cursor.close()
        con.close()

    def mostrar_formulario_modificacion(self, registro):
        Utilidades.limpiar_frame_center(self.frame_center, self.text_output)

        self.id_registro = registro[0]

        campos = ["Título", "Artista", "Año", "Género"]
        valores = [
            registro[1],
            registro[2],
            str(registro[3] or ""),
            registro[4] or ""
        ]

        for campo, valor in zip(campos, valores):
            fila = tk.Frame(self.frame_center)
            fila.pack(pady=5, padx=10, anchor="w")

            tk.Label(fila, text=f"{campo}:", width=25, anchor="w").pack(side="left")

            var = tk.StringVar(value=valor)
            tk.Entry(fila, textvariable=var, width=40).pack(side="left")

            self.entradas[campo] = var

        tk.Button(self.frame_center, text="Guardar cambios", command=self.guardar_cambios).pack(pady=5)
        tk.Button(self.frame_center, text="Cancelar", command=lambda: Utilidades.mostrar_inicio(self.frame_center, self.text_output)).pack(pady=5)

    def guardar_cambios(self):
        titulo = self.entradas["Título"].get()
        artista = self.entradas["Artista"].get()
        anio = self.entradas["Año"].get()
        genero = self.entradas["Género"].get()

        con = BBDD.crear_conexion()
        cursor = con.cursor()
        sql = "UPDATE listadiscos SET titulo=%s, artista=%s, anio=%s, genero=%s WHERE id=%s"
        data = (titulo, artista, anio, genero, self.id_registro)

        cursor.execute(sql, data)
        con.commit()
        cursor.close()
        con.close()

        self.text_output.insert(tk.END, "Registro modificado.\n")
        Utilidades.mostrar_inicio(self.frame_center, self.text_output)
