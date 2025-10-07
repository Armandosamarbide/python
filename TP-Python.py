import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import mysql.connector
import re

## Conectamos a la BBDD

def crear_base():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="discos"
    )

## Creamos la tabla, si no existe

def crear_tabla():
    con = crear_base()
    cursor = con.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS listadiscos (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        titulo VARCHAR(100) NOT NULL,
        artista VARCHAR(30) NOT NULL,
        anio INT(4),
        genero VARCHAR(30)
    )
    """
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()

## "Reseteo" de la pantalla

def limpiar_frame_center():
    for widget in frame_center.winfo_children():
        if widget != text_output:
            widget.destroy()

## Vuelve a la "pantalla inicial", llamando a la función anterior"

def mostrar_inicio():
    limpiar_frame_center()

## ALTA

def alta():

    limpiar_frame_center()
    tk.Label(frame_center, text="Dar de alta un nuevo disco", font=("Arial", 14, "bold")).pack(pady=10)

    for campo in ["Título", "Artista", "Año", "Género"]:
        frame_fila = tk.Frame(frame_center)
        frame_fila.pack(pady=3, padx=78)
        tk.Label(frame_fila, text=f"{campo}:", width=25, anchor="w").pack(side="left")
        var = tk.StringVar()
        tk.Entry(frame_fila, textvariable=var, width=40).pack(side="left")
        entradas[campo] = var

    tk.Button(frame_center, text="Guardar", command=guardar_alta).pack(pady=15)

## Habilitamos la BBDD para guardar el nuevo dato

def guardar_alta():
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

## BAJA

def baja():
    limpiar_frame_center()
    tk.Label(frame_center, text="Baja de disco", font=("Arial", 14, "bold")).pack(pady=10)

    var_titulo = tk.StringVar()
    fila = tk.Frame(frame_center)
    fila.pack(pady=5, padx=10, anchor="w")
    tk.Label(fila, text="Título EXACTO del disco a borrar:", width=25, anchor="w").pack(side="left")
    tk.Entry(fila, textvariable=var_titulo, width=40).pack(side="left")

    tk.Button(frame_center, text="Buscar", command=lambda: ejecutar_baja(var_titulo.get())).pack(pady=15)


## Buscamos el registro en la BBDD y lo borramos. Si no se lo encuentra, devuelve un mensaje de error

def ejecutar_baja(titulo):
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
            text_output.insert(tk.END, f"Registro eliminado: {r}\n")

    cursor.close()
    con.close()

## Modificación

def modificacion():
    limpiar_frame_center()
    
    tk.Label(frame_center, text="Modificar Disco", font=("Arial", 14, "bold")).pack(pady=10)
    
    frame_fila = tk.Frame(frame_center)
    frame_fila.pack(pady=5, padx=10, anchor="w")
    tk.Label(frame_fila, text="Título a modificar:", width=25, anchor="w").pack(side="left")
    
    var_titulo = tk.StringVar()
    tk.Entry(frame_fila, textvariable=var_titulo, width=40).pack(side="left")
    tk.Button(frame_center, text="Buscar", command=lambda: ejecutar_modificacion(var_titulo.get())).pack(pady=25)

def ejecutar_modificacion(titulo_buscado):
    if not titulo_buscado:
        text_output.insert(tk.END, "Debe ingresar un título.\n")
        return
    
    con = crear_base()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM listadiscos WHERE titulo = %s", (titulo_buscado,))
    registro = cursor.fetchone()   
    
    if registro:
        
        limpiar_frame_center()

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
                command=lambda: guardar_modificacion(registro[0])).pack(pady=5)
        tk.Button(frame_center, text="Cancelar", command=mostrar_inicio).pack(pady=5)
    else:
        text_output.insert(tk.END, f"No se encontró ningún disco.\n")

    cursor.close()
    con.close()

def guardar_modificacion(id_registro):
    
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
    mostrar_inicio() 

## Búsqueda de registros

def buscar():
    limpiar_frame_center()
    tk.Label(frame_center, text="Búsqueda de disco", font=("Arial", 14, "bold")).pack(pady=10)

    var_termino = tk.StringVar()
    fila = tk.Frame(frame_center)
    fila.pack(pady=5, padx=10, anchor="w")

    tk.Label(fila, text="Título o Artista:", width=25, anchor="w").pack(side="left")
    tk.Entry(fila, textvariable=var_termino, width=40).pack(side="left")
    tk.Button(frame_center, text="Buscar",
        command=lambda: ejecutar_busqueda(var_termino.get())).pack(pady=15)

## Ejecutamos la búsqueda del término recibido en el paso anterior

def ejecutar_busqueda(termino):
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

## Listar todos los registros cargados

def mostrar_todo():
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

## Limpiar la pantalla

def limpiar_pantalla():
    text_output.delete("1.0", tk.END)
    mostrar_inicio()
    
## Salir del programa

def salir():
    root.destroy()

## Definición y styling de la pantalla, los botones y los colores

root = tk.Tk()
root.title("Disquería EL PALACIO DE LA MÚSICA")
root.geometry("800x800")

frame_left = tk.Frame(root, bg="#434966", width=200)
frame_left.pack(side="left", fill="y")

## Con estas variables definimos el styling de los botones

fuente = tkFont.Font(weight="bold", family="Courier", size=10)
anchor = 17
altor = 2
pad_x = 10
pad_y = 10

## BOTONERA

boton_alta = tk.Button(frame_left, text="Alta", font=fuente, width=anchor, height=altor, command=alta)
boton_alta.pack(padx=pad_x, pady=pad_y)

boton_baja = tk.Button(frame_left, text="Baja", font=fuente, width=anchor, height=altor, command=baja)
boton_baja.pack(padx=pad_x, pady=pad_y)

boton_mod = tk.Button(frame_left, text="Modificación", font=fuente, width=anchor, height=altor, command=modificacion)
boton_mod.pack(padx=pad_x, pady=pad_y)

boton_busqueda = tk.Button(frame_left, text="Búsqueda", font=fuente, width=anchor, height=altor, command=buscar)
boton_busqueda.pack(padx=pad_x, pady=pad_y)

boton_mostrar = tk.Button(frame_left, text="Mostrar todo", font=fuente, width=anchor, height=altor, command=mostrar_todo)
boton_mostrar.pack(padx=pad_x, pady=pad_y)

boton_limpiar = tk.Button(frame_left, text="Limpiar pantalla", font=fuente, width=anchor, height=altor, command=limpiar_pantalla)
boton_limpiar.pack(padx=pad_x, pady=pad_y)

boton_salir = tk.Button(frame_left, text="Quit", font=fuente, width=anchor, height=altor, command=salir)
boton_salir.pack(padx=pad_x, pady=pad_y)

frame_center = tk.Frame(root, bg="white")
frame_center.pack(side="left", fill="both", expand=True)

text_output = tk.Text(frame_center, wrap="word")
text_output.pack(fill="both", expand=True, padx=pad_x, pady=pad_y)

entradas = {}

crear_tabla()
mostrar_inicio()

root.mainloop()