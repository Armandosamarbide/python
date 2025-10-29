import tkinter as tk
from crearbase import crear_base
from utilidades import limpiar_frame_center

def baja(frame_center, text_output):
    limpiar_frame_center(frame_center, text_output)
    tk.Label(frame_center, text="Baja de disco", font=("Arial", 14, "bold")).pack(pady=10)

    var_titulo = tk.StringVar()
    fila = tk.Frame(frame_center)
    fila.pack(pady=5, padx=10, anchor="w")
    tk.Label(fila, text="Título EXACTO del disco a borrar:", width=25, anchor="w").pack(side="left")
    tk.Entry(fila, textvariable=var_titulo, width=40).pack(side="left")
    tk.Button(frame_center, text="Buscar", command=lambda: ejecutar_baja(var_titulo.get(), text_output)).pack(pady=15)

def ejecutar_baja(titulo, text_output):
    if not titulo:
        text_output.insert(tk.END, "Debe ingresar un título.\n")
        return

    con = crear_base()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM listadiscos WHERE titulo = %s", (titulo,))
    registros = cursor.fetchall()

    if not registros:
        text_output.insert(tk.END, f"No se encontró el disco solicitado.\n")
    else:
        for r in registros:
            cursor.execute("DELETE FROM listadiscos WHERE id = %s", (r[0],))
            con.commit()
            text_output.insert(tk.END, f"Registro eliminado.\n")

    cursor.close()
    con.close()