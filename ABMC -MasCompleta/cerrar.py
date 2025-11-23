from tkinter import *
from tkinter.messagebox import askokcancel

class Cerrar(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Cerrar', command=self.cerrar)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def cerrar(self):
        consulta = askokcancel('Cerrar', "¿Desea abandonar la aplicación?")
        if consulta:
            Frame.quit(self)

if __name__ == '__main__':
    Cerrar().mainloop()
