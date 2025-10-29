import tkinter as tk
from crearbase import crear_base

def mostrar_todo(text_output):
    con = crear_base()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM listadiscos")
    registros = cursor.fetchall()
    
    text_output.insert(tk.END, "=== TODOS LOS DISCOS (Título, Artista, Año, Género)===\n")
    
    for r in registros:
        text_output.insert(tk.END, f"{r[1]}, {r[2]}, {r[3]}, {r[4]}\n")

    text_output.insert(tk.END, "\n")
    cursor.close()
    con.close()
