from modelo_poo_orm import db, Poliza
from decorador_log import log_accion
from observador_log import Observable, LogObserver
from mis_regex_poo import (
    patron_texto, patron_marca, patron_anio, patron_dominio,
    patron_poliza, patron_importe, patron_fecha,
                          )
import re
from datetime import datetime, date, timedelta

db.connect()
db.create_tables([Poliza])

class AccionesControlador(Observable):
    def __init__(self):
        super().__init__()
        # Observador que escribe en app.log (mismo archivo que el decorador)
        self.attach(LogObserver())

    def _validar_regex(self, patron, valor):
        return re.fullmatch(patron, valor) is not None

    def _parsear_fecha(self, fecha_str):
        return datetime.strptime(fecha_str, "%d/%m/%Y").date()

    def chequear_p(self, *args):
        try:
            (
                nombre, apellido, marca, modelo, anio, empresa, dominio,
                uso_vehiculo, numero_poliza, tipo_cobertura,
                fecha_inicio, fecha_vencimiento, importe
            ) = args

            campos = [
                ("Nombre", patron_texto, nombre),
                ("Apellido", patron_texto, apellido),
                ("Marca", patron_marca, marca),
                ("Modelo", patron_marca, modelo),
                ("Año", patron_anio, anio),
                ("Empresa", patron_texto, empresa),
                ("Dominio", patron_dominio, dominio.upper()),
                ("Uso vehículo", patron_texto, uso_vehiculo),
                ("Número de póliza", patron_poliza, numero_poliza),
                ("Cobertura", patron_texto, tipo_cobertura),
                ("Fecha de inicio", patron_fecha, fecha_inicio),
                ("Fecha de vencimiento", patron_fecha, fecha_vencimiento),
                ("Importe", patron_importe, importe),
            ]

            for etiqueta, patron, valor in campos:
                if not self._validar_regex(patron, valor):
                    return False, f"El campo «{etiqueta}» tiene un valor inválido."

            # Validación de rango de año
            anio_int = int(anio)
            if anio_int < 1900 or anio_int > date.today().year + 1:
                return False, "El campo «Año» debe estar entre 1900 y el año actual + 1."

            # Validación de relación entre fechas
            f_ini = self._parsear_fecha(fecha_inicio)
            f_vto = self._parsear_fecha(fecha_vencimiento)
            if f_vto <= f_ini:
                return False, "La fecha de vencimiento debe ser posterior a la fecha de inicio."

            return True, "OK"
        except Exception:
            return False, "Ocurrió un error al validar los datos. Revise los campos."

    def _crear_datos(self, *args):
        (nombre, apellido, marca, modelo, anio, empresa, dominio, uso_vehiculo,
         numero_poliza, tipo_cobertura, fecha_inicio, fecha_vencimiento, importe) = args

        return dict(
            nombre=nombre,
            apellido=apellido,
            marca=marca,
            modelo=modelo,
            anio=int(anio),
            empresa=empresa,
            dominio=dominio.upper(),
            uso_vehiculo=uso_vehiculo,
            numero_poliza=numero_poliza,
            tipo_cobertura=tipo_cobertura,
            fecha_inicio=self._parsear_fecha(fecha_inicio),
            fecha_vencimiento=self._parsear_fecha(fecha_vencimiento),
            importe=float(importe),
                    )

    @log_accion("CONSULTA")
    def consulta(self):
        try:
            registros = Poliza.select()
            self.notify("CONSULTA", completado=True)
            return registros
        except Exception as e:
            self.notify("CONSULTA", completado=False, error=str(e))
            return []


    @log_accion("ALTA")
    def alta(self, *args):
        try:
            datos = self._crear_datos(*args)
            Poliza.create(**datos)
            resultado = {
                'completado': True,
                'titulo': "Operación exitosa",
                'mensaje': "Registro agregado correctamente"
            }
        except Exception as e:
            resultado = {
                'completado': False,
                'titulo': "Error en alta",
                'mensaje': str(e)
            }

        # Notifica al observador (log)
        self.notify("ALTA", completado=resultado.get("completado"))
        return resultado

    @log_accion("BAJA")
    def baja(self, db_id):
        try:
            fila = Poliza.get(Poliza.id == db_id)
            fila.delete_instance()
            resultado = {
                'completado': True,
                'titulo': "Operación exitosa",
                'mensaje': "Registro eliminado"
            }
        except Exception as e:
            resultado = {
                'completado': False,
                'titulo': "Error en baja",
                'mensaje': str(e)
            }

        self.notify("BAJA", completado=resultado.get("completado"), id=db_id)
        return resultado

    @log_accion("MODIFICAR")
    def modificar(self, *args, db_id):
        try:
            datos = self._crear_datos(*args)
            Poliza.update(datos).where(Poliza.id == db_id).execute()
            resultado = {
                'completado': True,
                'titulo': "Operación exitosa",
                'mensaje': "Registro modificado"
            }
        except Exception as e:
            resultado = {
                'completado': False,
                'titulo': "Error en modificación",
                'mensaje': str(e)
            }

        self.notify("MODIFICAR", completado=resultado.get("completado"), id=db_id)
        return resultado

    @log_accion("BUSCAR")
    def buscar(self, nombre_buscar, apellido_buscar):
        try:
            query = Poliza.select()
            if nombre_buscar:
                query = query.where(Poliza.nombre.contains(nombre_buscar))
            if apellido_buscar:
                query = query.where(Poliza.apellido.contains(apellido_buscar))
            resultado = {'completado': True, 'registros': query}
        except Exception as e:
            resultado = {'completado': False, 'titulo': "Error en búsqueda", 'mensaje': str(e)}

        self.notify("BUSCAR", completado=resultado.get("completado"), nombre=nombre_buscar, apellido=apellido_buscar)
        return resultado

    @log_accion("PROXIMOS_VENCIMIENTOS")
    def proximos_vencimientos(self, dias=15):
        try:
            hoy = date.today()
            limite = hoy + timedelta(days=dias)
            registros = (
                Poliza.select()
                .where((Poliza.fecha_vencimiento >= hoy) & (Poliza.fecha_vencimiento <= limite))
                .order_by(Poliza.fecha_vencimiento)
            )
            self.notify("PROXIMOS_VENCIMIENTOS", completado=True, dias=dias)
            return registros
        except Exception as e:
            self.notify("PROXIMOS_VENCIMIENTOS", completado=False, error=str(e), dias=dias)
            return []
