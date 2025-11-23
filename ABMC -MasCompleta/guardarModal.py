from tkinter import *
import shelve
from guardar import *


def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)


def guarda(variables, popupGuardar):
    
    popupGuardar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    valor_id = lista[0]
    print(valor_id)
    db = shelve.open('persona')
    guardoValor = Persona(lista[1], lista[2], lista[3], lista[4])
    db[lista[0]] = guardoValor
    db.close()


def guardar():
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)
    Button(popupGuardar, text='OK', command=(lambda: show(vars_guardar, popupGuardar))).pack()
    Button(popupGuardar, text='guardar', command=(lambda: guarda(vars_guardar, popupGuardar))).pack()

    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()
