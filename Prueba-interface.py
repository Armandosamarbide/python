from tkinter import *
from tkinter.messagebox import *
import sqlite3                         # <------ IMPORTAMOS MÓDULO DE SQLITE 3
from tkinter import ttk

root = Tk()

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

boton_alta=Button(root, text="Alta", command=lambda:alta(a_val.get(), b_val.get(), c_val.get(), tree))
boton_alta.grid(row=6, column=1)


root.mainloop()

## Esto es un patrón que analiza el texto que puedo encontrar

## patron=^[A-Za-záéíóúñ]*

## El formato correcto es este:

## ^

##  [
##          A-Z
##          a-z
##          áéíóú
##          ñ
##  ]