## Esta funcionalidad controla el borrado de pantalla y la salida de la aplicación

import tkinter as tk
from utilidades import Utilidades

class OperacionesMisc:

    @staticmethod
    def limpiar_pantalla(text_output, frame_center):
        # reutiliza utilidades
        Utilidades.limpiar_pantalla(text_output, frame_center)

    @staticmethod
    def salir(root):
        Utilidades.salir(root)