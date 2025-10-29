import tkinter as tk

def limpiar_frame_center(frame_center, text_output):
    for widget in frame_center.winfo_children():
        if widget != text_output:
            widget.destroy()

def mostrar_inicio(frame_center, text_output):
    limpiar_frame_center(frame_center, text_output)

def limpiar_pantalla(text_output, frame_center):
    text_output.delete("1.0", tk.END)
    mostrar_inicio(frame_center, text_output)

def salir(root):
    root.destroy()