from tkinter import *
from cerrar import Cerrar
archivo = 'persona'
camposLeer = ('nombre', 'edad', 'sueldo', 'trabajo')


def imprimir(idVar):
    print(idVar.get())


def CrearFormLeer(root, camposLeer):
    formulario = Frame(root)
    div0 = Frame(formulario)
    formulario.pack(fill=X)
    div0.pack(side=TOP, expand=YES, fill=X)
    id_leer = Entry(div0, width=10)
    id_leer.pack(side=TOP)
    idVar = StringVar()
    id_leer.config(textvariable=idVar)
    idVar.set("Luis")


    return idVar


if __name__ == '__main__':
    root = Tk()
    vars_leer = CrearFormLeer(root, camposLeer)
    Button(root, text='Imprimir', command=(lambda: imprimir(vars_leer))).pack(side=LEFT)
    Cerrar(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: imprimir(vars_leer)))
    root.mainloop()
