from tkinter import *
from tkinter.messagebox import *
import sqlite3                         # <------ IMPORTAMOS MÓDULO DE SQLITE 3
from tkinter import ttk
import re

# ##############################################
# MODELO
# ##############################################
# 1) Crear la base
def crear_base():
    con = sqlite3.connect('miriam.db')
    return con

crear_base()
# 2) Crear la tabla
def crear_tabla(con):
    cursor = con.cursor()
    sql = """CREATE TABLE IF NOT EXISTS productos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             producto varchar(20) NOT NULL,
             cantidad real,
             precio real)
    """
    cursor.execute(sql)
    con.commit()
crear_tabla(crear_base())

# 3) Dar de alta

def alta(producto, cantidad, precio, tree): 
    print(producto, cantidad, precio)
    print(producto.get(), cantidad.get(), precio.get())

    cadena = producto.get()
    patron="^[A-Za-záéíóú]*$"
    if(re.match(patron, cadena)):
        con = crear_base()
        cursor = con.cursor()
        #mi_id = int(mi_id)
        data = (producto.get(), cantidad.get(), precio.get())
        sql = "INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        producto.set("---")
        actualizar_treeview(tree)
    else:
        print("error en campo producto")

def actualizar_treeview(mitreview):
    # Borrar
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    # Consulta 
    sql = "SELECT * FROM productos ORDER BY id ASC"
    con=crear_base()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()

    # Los muestra
    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))


# ##############################################
# CONTROLADOR
# ##############################################

root = Tk()
# ##############################################
# VISTA
# ##############################################

root.title("Tarea POO")
        
titulo = Label(root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

producto = Label(root, text="Producto")
producto.grid(row=1, column=0, sticky=W)
cantidad=Label(root, text="Cantidad")
cantidad.grid(row=2, column=0, sticky=W)
precio=Label(root, text="Precio")
precio.grid(row=3, column=0, sticky=W)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val = StringVar(), DoubleVar(), DoubleVar()
w_ancho = 20

entrada1 = Entry(root, textvariable = a_val, width = w_ancho) 
entrada1.grid(row = 1, column = 1)
entrada2 = Entry(root, textvariable = b_val, width = w_ancho) 
entrada2.grid(row = 2, column = 1)
entrada3 = Entry(root, textvariable = c_val, width = w_ancho) 
entrada3.grid(row = 3, column = 1)

# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------

tree = ttk.Treeview(root)
tree["columns"]=("col1", "col2", "col3")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=80)
tree.column("col2", width=200, minwidth=80)
tree.column("col3", width=200, minwidth=80)
tree.heading("#0", text="ID")
tree.heading("col1", text="Producto")
tree.heading("col2", text="cantidad")
tree.heading("col3", text="precio")
tree.grid(row=10, column=0, columnspan=4)

boton_alta=Button(root, text="Alta", command=lambda:alta(a_val, b_val, c_val, tree))
boton_alta.grid(row=6, column=1)


root.mainloop()


