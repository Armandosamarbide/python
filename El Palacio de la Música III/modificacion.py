import tkinter as tk
from crearbase import crear_base
from utilidades import limpiar_frame_center, mostrar_inicio

def modificacion(frame_center, text_output, entradas):
    limpiar_frame_center(frame_center, text_output)
    tk.Label(frame_center, text="Modificar Disco", font=("Arial", 14, "bold")).pack(pady=10)

    frame_fila = tk.Frame(frame_center)
    frame_fila.pack(pady=5, padx=10, anchor="w")
    tk.Label(frame_fila, text="Título a modificar:", width=25, anchor="w").pack(side="left")

    var_titulo = tk.StringVar()
    tk.Entry(frame_fila, textvariable=var_titulo, width=40).pack(side="left")
    tk.Button(frame_center, text="Buscar", command=lambda: ejecutar_modificacion(var_titulo.get(), frame_center, text_output, entradas)).pack(pady=25)

def ejecutar_modificacion(titulo_buscado, frame_center, text_output, entradas):
    if not titulo_buscado:
        text_output.insert(tk.END, "Debe ingresar un título.\n")
        return

    con = crear_base()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM listadiscos WHERE titulo = %s", (titulo_buscado,))
    registro = cursor.fetchone()   

    if registro:
        limpiar_frame_center(frame_center, text_output)
        campos = ["Título", "Artista", "Año", "Género"]
        valores = [registro[1], registro[2], str(registro[3] or ""), registro[4] or ""]

        for campo, valor in zip(campos, valores):
            frame_fila = tk.Frame(frame_center)
            frame_fila.pack(pady=5, padx=10, anchor="w")

            tk.Label(frame_fila, text=f"{campo}:", width=25, anchor="w").pack(side="left")
            var = tk.StringVar(value=valor)   
            tk.Entry(frame_fila, textvariable=var, width=40).pack(side="left")
            entradas[campo] = var

        tk.Button(frame_center, text="Guardar cambios",
                command=lambda: grabar_modificacion(registro[0], entradas, text_output, frame_center)).pack(pady=5)
        tk.Button(frame_center, text="Cancelar", command=lambda: mostrar_inicio(frame_center, text_output)).pack(pady=5)
    else:
        text_output.insert(tk.END, f"No se encontró ningún disco.\n")

    cursor.close()
    con.close()

def grabar_modificacion(id_registro, entradas, text_output, frame_center):
    titulo = entradas["Título"].get()
    artista = entradas["Artista"].get()
    anio = entradas["Año"].get()
    genero = entradas["Género"].get()

    con = crear_base()
    cursor = con.cursor()
    sql = "UPDATE listadiscos SET titulo=%s, artista=%s, anio=%s, genero=%s WHERE id=%s"
    data = (titulo, artista, anio, genero, id_registro)

    cursor.execute(sql, data)
    con.commit()
    cursor.close()
    con.close()

    text_output.insert(tk.END, f"Registro modificado.\n")
    mostrar_inicio(frame_center, text_output)