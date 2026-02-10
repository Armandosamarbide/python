import tkinter as tk
from tkinter import ttk, messagebox
from controlador_poo_orm import AccionesControlador
from notificaciones_poo import *


class IniciarSegurosAutomotor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestión de Seguros de Automotor")

        self.ac = AccionesControlador()

        # Variables
        self.var_nombre = tk.StringVar()
        self.var_apellido = tk.StringVar()
        self.var_marca = tk.StringVar()
        self.var_modelo = tk.StringVar()
        self.var_anio = tk.StringVar()
        self.var_empresa = tk.StringVar()
        self.var_dominio = tk.StringVar()
        self.var_uso = tk.StringVar()
        self.var_numero_poliza = tk.StringVar()
        self.var_cobertura = tk.StringVar()
        self.var_fecha_inicio = tk.StringVar()
        self.var_fecha_vencimiento = tk.StringVar()
        self.var_importe = tk.StringVar()

        frame_form = tk.Frame(self.root)
        frame_form.pack(fill="x", padx=10, pady=10)

        # Columna izquierda
        tk.Label(frame_form, text="Nombre").grid(row=0, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_nombre).grid(row=0, column=1)

        tk.Label(frame_form, text="Apellido").grid(row=1, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_apellido).grid(row=1, column=1)

        tk.Label(frame_form, text="Marca").grid(row=2, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_marca).grid(row=2, column=1)

        tk.Label(frame_form, text="Modelo").grid(row=3, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_modelo).grid(row=3, column=1)

        tk.Label(frame_form, text="Año").grid(row=4, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_anio).grid(row=4, column=1)

        tk.Label(frame_form, text="Empresa").grid(row=5, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_empresa).grid(row=5, column=1)

        # Columna derecha
        etiquetas2 = [
            "Dominio",
            "Uso vehículo",
            "N° póliza",
            "Cobertura",
            "F. inicio (dd/mm/aaaa)",
            "F. vencimiento (dd/mm/aaaa)",
            "Importe",
        ]
        vars2 = [
            self.var_dominio,
            self.var_uso,
            self.var_numero_poliza,
            self.var_cobertura,
            self.var_fecha_inicio,
            self.var_fecha_vencimiento,
            self.var_importe,
        ]

        for j, (etq, var) in enumerate(zip(etiquetas2, vars2)):
            tk.Label(frame_form, text=etq).grid(row=j, column=2, sticky="w")
            tk.Entry(frame_form, textvariable=var).grid(row=j, column=3)

        # Botonera
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(fill="x", padx=10, pady=5)

        botones = [
            ("Agregar", self._btn_agregar),
            ("Modificar", self._btn_modificar),
            ("Eliminar", self._btn_eliminar),
            ("Buscar", self._btn_buscar),
            ("Limpiar", self._limpiar_campos),
        ]

        for i, (texto, cmd) in enumerate(botones):
            tk.Button(frame_botones, text=texto, width=12, command=cmd).grid(
                row=0, column=i, padx=5
            )

        # TreeView
        frame_tree = tk.Frame(self.root)
        frame_tree.pack(fill="both", expand=True, padx=10, pady=10)

        cols = (
            "nombre",
            "apellido",
            "marca",
            "modelo",
            "anio",
            "empresa",
            "dominio",
            "uso",
            "numero_poliza",
            "cobertura",
            "fecha_inicio",
            "fecha_vencimiento",
            "importe",
        )

        self.tree = ttk.Treeview(frame_tree, columns=cols, show="headings")

        for c in cols:
            self.tree.heading(c, text=c.capitalize())
            self.tree.column(c, width=100)

        self.tree.pack(fill="both", expand=True)

        self.tree.bind("<<TreeviewSelect>>", self._cargar_datos_seleccion)

        # Cargar tabla
        self._actualizar_tree(self.ac.consulta())

        self.root.mainloop()

    def _cargar_datos_seleccion(self, event=None):
        item = self.tree.focus()
        if not item:
            return

        valores = self.tree.item(item, "values")
        if not valores:
            return

        (
            nombre,
            apellido,
            marca,
            modelo,
            anio,
            empresa,
            dominio,
            uso,
            numero_poliza,
            cobertura,
            fecha_inicio,
            fecha_vencimiento,
            importe,
        ) = valores

        self.var_nombre.set(nombre)
        self.var_apellido.set(apellido)
        self.var_marca.set(marca)
        self.var_modelo.set(modelo)
        self.var_anio.set(anio)
        self.var_empresa.set(empresa)
        self.var_dominio.set(dominio)
        self.var_uso.set(uso)
        self.var_numero_poliza.set(numero_poliza)
        self.var_cobertura.set(cobertura)
        self.var_fecha_inicio.set(fecha_inicio)
        self.var_fecha_vencimiento.set(fecha_vencimiento)
        self.var_importe.set(importe)

    def _limpiar_campos(self):
        self.var_nombre.set("")
        self.var_apellido.set("")
        self.var_marca.set("")
        self.var_modelo.set("")
        self.var_anio.set("")
        self.var_empresa.set("")
        self.var_dominio.set("")
        self.var_uso.set("")
        self.var_numero_poliza.set("")
        self.var_cobertura.set("")
        self.var_fecha_inicio.set("")
        self.var_fecha_vencimiento.set("")
        self.var_importe.set("")

    def _actualizar_tree(self, filas):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for f in filas:
            self.tree.insert(
                "",
                "end",
                values=(
                    f.nombre,
                    f.apellido,
                    f.marca,
                    f.modelo,
                    f.anio,
                    f.empresa,
                    f.dominio,
                    f.uso_vehiculo,
                    f.numero_poliza,
                    f.tipo_cobertura,
                    f.fecha_inicio.strftime("%d/%m/%Y"),
                    f.fecha_vencimiento.strftime("%d/%m/%Y"),
                    f"{f.importe:.2f}",
                ),
            )

    def _obtener_id(self):
        item = self.tree.focus()
        if not item:
            return None

        nombre = self.tree.item(item, "values")[0]
        fila = self.ac.buscar(nombre, "")
        try:
            return list(fila["registros"])[0].id
        except:
            return None

    def _btn_agregar(self):
        args = (
            self.var_nombre.get(),
            self.var_apellido.get(),
            self.var_marca.get(),
            self.var_modelo.get(),
            self.var_anio.get(),
            self.var_empresa.get(),
            self.var_dominio.get(),
            self.var_uso.get(),
            self.var_numero_poliza.get(),
            self.var_cobertura.get(),
            self.var_fecha_inicio.get(),
            self.var_fecha_vencimiento.get(),
            self.var_importe.get(),
        )

        ok, msg = self.ac.chequear_p(*args)
        if ok:
            resultado = self.ac.alta(*args)
            if resultado["completado"]:
                messagebox.showinfo(resultado["titulo"], resultado["mensaje"])
                self._actualizar_tree(self.ac.consulta())
                self._limpiar_campos()
        else:
            messagebox.showerror("Error", msg)
            messagebox.showerror("Error", "Revisar los datos ingresados.")

    def _btn_modificar(self):
        db_id = self._obtener_id()
        if not db_id:
            return no_fila()

        args = (
            self.var_nombre.get(),
            self.var_apellido.get(),
            self.var_marca.get(),
            self.var_modelo.get(),
            self.var_anio.get(),
            self.var_empresa.get(),
            self.var_dominio.get(),
            self.var_uso.get(),
            self.var_numero_poliza.get(),
            self.var_cobertura.get(),
            self.var_fecha_inicio.get(),
            self.var_fecha_vencimiento.get(),
            self.var_importe.get(),
        )

        ok, msg = self.ac.chequear_p(*args)
        if ok:
            resultado = self.ac.modificar(*args, db_id=db_id)
            if resultado["completado"]:
                messagebox.showinfo(resultado["titulo"], resultado["mensaje"])
                self._actualizar_tree(self.ac.consulta())
                self._limpiar_campos()
        else:
            messagebox.showerror("Error", msg)

    def _btn_eliminar(self):
        db_id = self._obtener_id()
        if not db_id:
            return no_fila()

        resultado = self.ac.baja(db_id)
        if resultado["completado"]:
            messagebox.showinfo(resultado["titulo"], resultado["mensaje"])
            self._actualizar_tree(self.ac.consulta())
            self._limpiar_campos()
        else:
            messagebox.showerror(resultado["titulo"], resultado["mensaje"])

    def _btn_buscar(self):
        nombre = self.var_nombre.get()
        apellido = self.var_apellido.get()
        resultado = self.ac.buscar(nombre, apellido)

        if resultado["completado"]:
            self._actualizar_tree(resultado["registros"])
        else:
            messagebox.showerror(resultado["titulo"], resultado["mensaje"])
