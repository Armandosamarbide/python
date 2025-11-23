from tkinter import *
import shelve
from leer import CrearFormLeer, imprimir, camposLeer
from PersonaP.PersonaM import Persona

def show(idVar, popupLeer):
    popupLeer.destroy()
    imprimir(idVar)

""""""


def lee(idVar, popupLeer):
    lab = Label(popupLeer, width=100, text=idVar.get())
    lab.pack(side=TOP)
    t = idVar.get()

    db = shelve.open('persona')
    print("-------------------------------")
    valorALeer = db[t]

    print("Nombre: ", valorALeer)
    lab_leer = Label(popupLeer, width=100, text=valorALeer)
    lab_leer.pack(side=TOP)
    db.close()


def leer():
    popupLeer = Toplevel()
    popupLeer.geometry("400x300")
    vars_leer = CrearFormLeer(popupLeer, camposLeer)
    Button(popupLeer, text='OK', command=(lambda: show(vars_leer, popupLeer))).pack()
    Button(popupLeer, text='Leer', command=(lambda: lee(vars_leer, popupLeer))).pack()

    popupLeer.grab_set()
    popupLeer.focus_set()
    popupLeer.wait_window()