import tkinter as tk
from ui_helpers import mostrar_inicio

def limpiar_pantalla(text_output, frame_center):
    text_output.delete("1.0", tk.END)
    mostrar_inicio(frame_center, text_output)

def salir(root):
    root.destroy()
