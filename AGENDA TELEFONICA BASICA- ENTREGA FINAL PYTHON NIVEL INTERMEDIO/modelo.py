import sqlite3
import re
from mis_regex import MisRegex

objmiregex = MisRegex()
patron_nombre = objmiregex.regex_nombre()


class Abmc:

    def __init__(self):
        try:
            self.con = sqlite3.connect("mibase.db")
            self.crear_tabla()
        except sqlite3.Error as e:
            raise Exception(f"Error al conectar con la base de datos: {str(e)}")

    def crear_tabla(self):
        try:
            cursor = self.con.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS contacto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                telefono TEXT NOT NULL
            )
            """
            cursor.execute(sql)
            self.con.commit()
        except sqlite3.Error as e:
            raise Exception(f"Error al crear la tabla: {str(e)}")

    def alta(self, nombre, apellido, telefono):
        try:
            if not nombre or not apellido or not telefono:
                raise ValueError("Todos los campos son obligatorios")
            
            if re.match(patron_nombre, nombre):
                cursor = self.con.cursor()
                sql = "INSERT INTO contacto (nombre, apellido, telefono) VALUES (?, ?, ?)"
                data = (nombre, apellido, telefono)
                cursor.execute(sql, data)
                self.con.commit()
                return "Contacto agregado correctamente"
            else:
                raise ValueError("El nombre no cumple con el formato requerido (solo letras, de 2 a 20 caracteres)")
        except sqlite3.Error as e:
            return f"Error en la base de datos: {str(e)}"
        except ValueError as e:
            return f"Error de validación: {str(e)}"
        except Exception as e:
            return f"Error inesperado: {str(e)}"

    def borrar_por_id(self, mi_id):
        try:
            assert mi_id, "El ID no puede estar vacío"
            
            cursor = self.con.cursor()
            
            # Verificar si existe el contacto
            sql_check = "SELECT * FROM contacto WHERE id = ?"
            cursor.execute(sql_check, (mi_id,))
            if not cursor.fetchone():
                raise ValueError(f"No existe un contacto con ID {mi_id}")
            
            sql = "DELETE FROM contacto WHERE id = ?"  
            cursor.execute(sql, (mi_id,))
            self.con.commit()
            return "Contacto eliminado correctamente"
        except sqlite3.Error as e:
            return f"Error en la base de datos: {str(e)}"
        except (ValueError, AssertionError) as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Error inesperado: {str(e)}"

    def consultar_todos(self):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM contacto ORDER BY id ASC"
            cursor.execute(sql)
            return cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Error al consultar registros: {str(e)}")

    def consultar_por_nombre(self, nombre):
        try:
            if not nombre:
                raise ValueError("Debe ingresar un nombre para buscar")
            
            cursor = self.con.cursor()
            sql = "SELECT * FROM contacto WHERE nombre LIKE ?"
            cursor.execute(sql, ('%' + nombre + '%',))
            return cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Error al consultar por nombre: {str(e)}")
        except ValueError as e:
            raise e