import tkinter as tk
import re
from crearbase import crear_base
from utilidades import limpiar_frame_center

def alta(frame_center, text_output, entradas):
    limpiar_frame_center(frame_center, text_output)
    tk.Label(frame_center, text="Dar de alta un nuevo disco", font=("Arial", 14, "bold")).pack(pady=10)

    for campo in ["Título", "Artista", "Año", "Género"]:
        frame_fila = tk.Frame(frame_center)
        frame_fila.pack(pady=3, padx=78)
        tk.Label(frame_fila, text=f"{campo}:", width=25, anchor="w").pack(side="left")
        var = tk.StringVar()
        tk.Entry(frame_fila, textvariable=var, width=40).pack(side="left")
        entradas[campo] = var

    tk.Button(frame_center, text="Guardar", command=lambda: grabar_alta(entradas, text_output)).pack(pady=15)

def grabar_alta(entradas, text_output):
    titulo = entradas["Título"]
    artista = entradas["Artista"]
    anio = entradas["Año"]
    genero = entradas["Género"]

    patron_texto = "^[A-Za-záéíóúÁÉÍÓÚñÑ0-9 ]+$"

    if re.match(patron_texto, titulo.get()) and re.match(patron_texto, artista.get()):
        con = crear_base()
        cursor = con.cursor()
        sql = "INSERT INTO listadiscos(titulo, artista, anio, genero) VALUES(%s, %s, %s, %s)"
        data = (titulo.get(), artista.get(), anio.get(), genero.get())
        cursor.execute(sql, data)
        con.commit()
        text_output.insert(tk.END, f"Registro agregado: {data}\n")
        cursor.close()
        con.close()
    else:
        text_output.insert(tk.END, "Error en los campos Título, Artista o Año\n")