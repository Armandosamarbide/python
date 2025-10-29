import tkinter as tk
from crearbase import crear_base
from utilidades import limpiar_frame_center

def buscar(frame_center, text_output):
    limpiar_frame_center(frame_center, text_output)
    tk.Label(frame_center, text="Búsqueda de disco", font=("Arial", 14, "bold")).pack(pady=10)

    var_termino = tk.StringVar()
    fila = tk.Frame(frame_center)
    fila.pack(pady=5, padx=10, anchor="w")

    tk.Label(fila, text="Título o Artista:", width=25, anchor="w").pack(side="left")
    tk.Entry(fila, textvariable=var_termino, width=40).pack(side="left")
    tk.Button(frame_center, text="Buscar",
        command=lambda: ejecutar_busqueda(var_termino.get(), text_output)).pack(pady=15)

def ejecutar_busqueda(termino, text_output):
    if not termino:
        text_output.insert(tk.END, "No se ingresó un término de búsqueda.\n")
        return

    con = crear_base()
    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM listadiscos WHERE titulo LIKE %s OR artista LIKE %s",
        (f"%{termino}%", f"%{termino}%")
    )
    resultados = cursor.fetchall()

    if resultados:
        text_output.insert(tk.END, f"Resultados de búsqueda:\n")
        for r in resultados:
            text_output.insert(tk.END, f"ID: {r[0]}, Título: {r[1]}, Artista: {r[2]}, Año: {r[3]}, Género: {r[4]}\n")
    else:
        text_output.insert(tk.END, f"No se encontraron registros que coincidan con la búsqueda solicitada.\n")

    cursor.close()
    con.close()