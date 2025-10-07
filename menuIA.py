import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import mysql.connector
import re

## CONECTAMOS A LA BBDD

def crear_base():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="discos"
    )

## CREAMOS LA TABLA EN CASO DE QUE NO EXISTA

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

## "RESETEO" DE LA PANTALLA

def limpiar_frame_center():
    for widget in frame_center.winfo_children():
        if widget != text_output:
            widget.destroy()

## VUELVE A LA "PANTALLA INICIAL" LLAMANDO A LA FUNCIÓN ANTERIOR

def mostrar_inicio():
    limpiar_frame_center()

## ALTA

def alta():
    limpiar_frame_center()
    
    ## Título del formulario y cómo se mostrará en pantalla
    
    tk.Label(frame_center, text="Dar de alta un nuevo disco", font=("Arial", 14, "bold")).pack(pady=10)
    
    ## Diccionario con los campos que vamos a llenar
    
    campos = ["Título", "Artista", "Año", "Género"]
    
    ## Esto limpia el entradas para que no queden rastros de registros anteriores
    
    entradas.clear()
    
    ## Recorremos la lista creando un campo por fila y le damos las dimensiones
    
    for campo in campos:
        frame_fila = tk.Frame(frame_center)
        frame_fila.pack(pady=2, padx=78)
        
        lbl = tk.Label(frame_fila, text=campo+":", width=15, anchor="w")
        lbl.pack(side="left")
        
        var = tk.StringVar()
        entry = tk.Entry(frame_fila, textvariable=var, width=40)
        entry.pack(side="left")
        
        entradas[campo] = var

    tk.Button(frame_center, text="Guardar", command=guardar_alta).pack(pady=15)

## GUARDAMOS EL NUEVO REGISTRO

def guardar_alta():
    titulo = entradas["Título"]
    artista = entradas["Artista"]
    anio = entradas["Año"]
    genero = entradas["Género"]
    
    patron_texto = "^[A-Za-záéíóúÁÉÍÓÚñÑ ]+$"
        
    if re.match(patron_texto, titulo.get()) and re.match(patron_texto, artista.get()):
        
        con = crear_base()
        cursor = con.cursor()
        
        sql = "INSERT INTO listadiscos(titulo, artista, anio, genero) VALUES(%s, %s, %s, %s)"
        data = (titulo.get(), artista.get(), anio.get() if anio.get() else None, genero.get())
        cursor.execute(sql, data)
        con.commit()
        
        titulo.set("")
        artista.set("")
        anio.set("")
        genero.set("")
        
        text_output.insert(tk.END, f"Registro agregado: {data}\n")
        cursor.close()
        con.close()
    else:
        text_output.insert(tk.END, "Error en los campos Título, Artista o Año\n")

## BAJA

def baja():
    limpiar_frame_center()
    
    tk.Label(frame_center, text="Baja de disco", font=("Arial", 14, "bold")).pack(pady=10)
    
    frame_fila = tk.Frame(frame_center)
    frame_fila.pack(pady=5, padx=10, anchor="w")
    
    tk.Label(frame_fila, text="Título EXACTO del disco a borrar:", width=25, anchor="w").pack(side="left")
    var_titulo = tk.StringVar()
    tk.Entry(frame_fila, textvariable=var_titulo, width=40).pack(side="left")
    
    # Botón Buscar
    tk.Button(frame_center, text="Buscar", command=lambda: ejecutar_baja(var_titulo.get())).pack(pady=15)

def ejecutar_baja(titulo_buscar):
    if not titulo_buscar:
        text_output.insert(tk.END, "Debe ingresar un título.\n")
        return

    con = crear_base()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM listadiscos WHERE titulo = %s", (titulo_buscar,))
    registros = cursor.fetchall()
    
    if registros:
        for registro in registros:
            respuesta = messagebox.askyesno(
                "Confirmar Borrado",
                f"Registro encontrado:\nID: {registro[0]}, Título: {registro[1]}, Artista: {registro[2]}, Año: {registro[3]}, Género: {registro[4]}\n\n¿Desea borrar este registro?"
            )
            if respuesta:
                cursor.execute("DELETE FROM listadiscos WHERE id = %s", (registro[0],))
                con.commit()
                text_output.insert(tk.END, f"Registro eliminado: {registro}\n")
            else:
                text_output.insert(tk.END, f"Borrado cancelado para el registro: {registro}\n")
    else:
        text_output.insert(tk.END, f"No se encontró ningún disco con el título '{titulo_buscar}'.\n")
    
    cursor.close()
    con.close()

## MODIFICACIÓN

def modificacion():
    limpiar_frame_center()
    
    tk.Label(frame_center, text="Modificar Disco", font=("Arial", 14, "bold")).pack(pady=10)
    
    frame_fila = tk.Frame(frame_center)
    frame_fila.pack(pady=5, padx=10, anchor="w")
    tk.Label(frame_fila, text="Título a modificar:", width=15, anchor="w").pack(side="left")
    
    var_titulo = tk.StringVar()
    tk.Entry(frame_fila, textvariable=var_titulo, width=40).pack(side="left")
    tk.Button(frame_center, text="Buscar", command=lambda: ejecutar_modificacion(var_titulo.get())).pack(pady=15)

def ejecutar_modificacion(titulo_buscar):
    if not titulo_buscar:
        text_output.insert(tk.END, "Debe ingresar un título.\n")
        return
    
    con = crear_base()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM listadiscos WHERE titulo = %s", (titulo_buscar,))
    registros = cursor.fetchall()
    
    if registros:
        registro = registros[0]
        entradas.clear()
        limpiar_frame_center()
        
        campos = ["Título", "Artista", "Año", "Género"]
        valores = [registro[1], registro[2], str(registro[3]) if registro[3] else "", registro[4] if registro[4] else ""]
        
        for i, campo in enumerate(campos):
            frame_fila = tk.Frame(frame_center)
            frame_fila.pack(pady=5, padx=10, anchor="w")
            
            tk.Label(frame_fila, text=campo+":", width=15, anchor="w").pack(side="left")
            var = tk.StringVar()
            var.set(valores[i])
            tk.Entry(frame_fila, textvariable=var, width=40).pack(side="left")
            entradas[campo] = var
        
        tk.Button(frame_center, text="Guardar cambios", command=lambda: guardar_modificacion(registro[0])).pack(pady=5)
        tk.Button(frame_center, text="Cancelar", command=mostrar_inicio).pack(pady=5)
    else:
        text_output.insert(tk.END, f"No se encontró ningún disco con el título '{titulo_buscar}'.\n")
    
    cursor.close()
    con.close()

def guardar_modificacion(registro_id):
    titulo = entradas["Título"].get()
    artista = entradas["Artista"].get()
    anio = entradas["Año"].get()
    genero = entradas["Género"].get()
    
    patron_texto = "^[A-Za-záéíóúÁÉÍÓÚñÑ ]+$"
    patron_anio = "^[0-9]{4}$"
    
    if re.match(patron_texto, titulo) and re.match(patron_texto, artista) and (anio=="" or re.match(patron_anio, anio)):
        con = crear_base()
        cursor = con.cursor()
        sql = "UPDATE listadiscos SET titulo=%s, artista=%s, anio=%s, genero=%s WHERE id=%s"
        data = (titulo, artista, anio if anio else None, genero, registro_id)
        cursor.execute(sql, data)
        con.commit()
        
        text_output.insert(tk.END, f"Registro modificado: {data}\n")
        cursor.close()
        con.close()
        mostrar_inicio()
    else:
        text_output.insert(tk.END, "Error en los campos Título, Artista o Año\n")

## BÚSQUEDA DE REGISTROS

def busqueda():
    limpiar_frame_center()
    
    tk.Label(frame_center, text="Búsqueda de disco", font=("Arial", 14, "bold")).pack(pady=10)
    
    frame_fila = tk.Frame(frame_center)
    frame_fila.pack(pady=5, padx=10, anchor="w")
    
    tk.Label(frame_fila, text="Título o Artista:", width=15, anchor="w").pack(side="left")
    var_termino = tk.StringVar()
    tk.Entry(frame_fila, textvariable=var_termino, width=40).pack(side="left")
    
    tk.Button(frame_center, text="Buscar", command=lambda: ejecutar_busqueda(var_termino.get())).pack(pady=15)

def ejecutar_busqueda(termino):
    if not termino:
        text_output.insert(tk.END, "Debe ingresar un término de búsqueda.\n")
        return

    con = crear_base()
    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM listadiscos WHERE titulo LIKE %s OR artista LIKE %s",
        (f"%{termino}%", f"%{termino}%")
    )
    resultados = cursor.fetchall()
    
    if resultados:
        text_output.insert(tk.END, f"Resultados para '{termino}':\n")
        for r in resultados:
            text_output.insert(tk.END, f"ID: {r[0]}, Título: {r[1]}, Artista: {r[2]}, Año: {r[3]}, Género: {r[4]}\n")
    else:
        text_output.insert(tk.END, f"No se encontraron registros con '{termino}'.\n")
    
    cursor.close()
    con.close()

## MOSTRAR TODOS LOS REGISTROS

def mostrar_todo():
    con = crear_base()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM listadiscos")
    registros = cursor.fetchall()
    
    text_output.insert(tk.END, "=== TODOS LOS DISCOS ===\n")
    
    for r in registros:
       text_output.insert(tk.END, f"Título: {r[1]}, Artista: {r[2]}, Año: {r[3]}, Género: {r[4]}\n")
    text_output.insert(tk.END, "\n")
    cursor.close()
    con.close()

## LIMPIAR LA PANTALLA
def limpiar_pantalla():
    text_output.delete("1.0", tk.END)
    mostrar_inicio()
    
## SALIR DEL PROGRAMA

def salir():
    root.destroy()

## Styling de los botones y los colores

root = tk.Tk()
root.title("Disquería EL PALACIO DE LA MÚSICA")
root.geometry("800x600")

frame_left = tk.Frame(root, bg="#434966", width=200)
frame_left.pack(side="left", fill="y")

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

boton_busqueda = tk.Button(frame_left, text="Búsqueda", font=fuente, width=anchor, height=altor, command=busqueda)
boton_busqueda.pack(padx=pad_x, pady=pad_y)

boton_mostrar = tk.Button(frame_left, text="Mostrar todo", font=fuente, width=anchor, height=altor, command=mostrar_todo)
boton_mostrar.pack(padx=pad_x, pady=pad_y)

boton_limpiar = tk.Button(frame_left, text="Limpiar pantalla", font=fuente, width=anchor, height=altor, command=limpiar_pantalla)
boton_limpiar.pack(padx=pad_x, pady=pad_y)

boton_salir = tk.Button(frame_left, text="Quit", font=fuente, width=anchor, height=altor, command=salir)
boton_salir.pack(padx=pad_x, pady=pad_y)

# Frame central
frame_center = tk.Frame(root, bg="white")
frame_center.pack(side="left", fill="both", expand=True)

# Área de texto
text_output = tk.Text(frame_center, wrap="word")
text_output.pack(fill="both", expand=True, padx=pad_x, pady=pad_y)

entradas = {}

# Crear tabla al iniciar
crear_tabla()
mostrar_inicio()

root.mainloop()