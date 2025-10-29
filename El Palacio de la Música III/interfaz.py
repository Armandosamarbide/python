import tkinter as tk
import tkinter.font as tkFont
from crearbase import crear_tabla
from alta import alta
from baja import baja
from modificacion import modificacion
from busqueda import buscar
from listartodo import mostrar_todo
from utilidades import limpiar_pantalla, salir, mostrar_inicio

def crear_interfaz():
    root = tk.Tk()
    root.title("Disquería EL PALACIO DE LA MÚSICA")
    root.geometry("800x800")

    frame_left = tk.Frame(root, bg="#434966", width=200)
    frame_left.pack(side="left", fill="y")

    frame_center = tk.Frame(root, bg="white")
    frame_center.pack(side="left", fill="both", expand=True)

    text_output = tk.Text(frame_center, wrap="word")
    text_output.pack(fill="both", expand=True, padx=10, pady=10)

    entradas = {}

    fuente = tkFont.Font(weight="bold", family="Courier", size=10)
    anchor = 17
    altor = 2
    pad_x = 10
    pad_y = 10

    botones = [
        ("Alta", lambda: alta(frame_center, text_output, entradas)),
        ("Baja", lambda: baja(frame_center, text_output)),
        ("Modificación", lambda: modificacion(frame_center, text_output, entradas)),
        ("Búsqueda", lambda: buscar(frame_center, text_output)),
        ("Mostrar todo", lambda: mostrar_todo(text_output)),
        ("Limpiar pantalla", lambda: limpiar_pantalla(text_output, frame_center)),
        ("Quit", lambda: salir(root))
    ]

    for texto, comando in botones:
        tk.Button(frame_left, text=texto, font=fuente, width=anchor, height=altor, command=comando)\
            .pack(padx=pad_x, pady=pad_y)

    crear_tabla()
    mostrar_inicio(frame_center, text_output)

    root.mainloop()