from tkinter.messagebox import *


def revisar_datos():
    showerror(
        "ERROR",
        (
            "Revise los datos ingresados."
            "\nNombre / Apellido / Empresa / Uso / Cobertura solo aceptan letras y espacios,"
            "\nMarca acepta letras, números y espacios,"
            "\nAño debe ser numérico (4 dígitos),"
            "\nDominio debe ser una patente válida (letras y números),"
            "\nNúmero de póliza acepta letras, números y guiones,"
            "\nFechas en formato dd/mm/aaaa,"
            "\nImporte numérico con decimales opcionales."
        ),
    )


def no_fila():
    showerror("ERROR", "Ninguna fila fue seleccionada.")


def p_eliminado():
    showinfo("¡Listo!", "El registro ha sido eliminado.")


def p_modificado():
    showinfo("¡Listo!", "El registro ha sido modificado.")


def confirmar_b():
    return askyesno("Confirmación", "¿Desea eliminar el registro seleccionado?")


def b_cancelada():
    showinfo("Confirmación", "Se canceló la eliminación.")


def confirmar_m():
    return askyesno("Confirmación", "¿Desea modificar el registro seleccionado?")


def m_cancelada():
    showinfo("Confirmación", "Se canceló la modificación.")


def avisar_vencimientos(texto):
    showinfo("Próximos vencimientos", texto)
