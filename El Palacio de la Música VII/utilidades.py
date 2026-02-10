## Esta funcionalidad controla el borrado de pantalla y la salida de la aplicación

import tkinter as tk

class Utilidades:

    @staticmethod
    def limpiar_frame_center(frame_center, text_output):
        # destruimos todos los widgets excepto el text_output
        for widget in frame_center.winfo_children():
            if widget != text_output:
                widget.destroy()

    @staticmethod
    def mostrar_inicio(frame_center, text_output):
        Utilidades.limpiar_frame_center(frame_center, text_output)
        # aquí podés agregar contenido inicial si lo necesitás después

    @staticmethod
    def limpiar_pantalla(text_output, frame_center):
        text_output.delete("1.0", tk.END)
        Utilidades.mostrar_inicio(frame_center, text_output)

    @staticmethod
    def salir(root):
        root.destroy()