import sqlite3
import re
from mis_regex import MisRegex
# ##############################################
# MODELO
# ##############################################
class Abmc:

    def __init__(self, ):
        try:
            self.conexion()
            self.crear_tabla()
        except:
            print("Hay un error")


    def conexion(self, ):
        con = sqlite3.connect("mibase.db")
        return con

    def crear_tabla(self, ):
        con = self.conexion()
        cursor = con.cursor()
        
        sql = """CREATE TABLE productos
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto varchar(20) NOT NULL,
                cantidad real,
                precio real)
        """
        cursor.execute(sql)
        con.commit()

    def alta(self, producto, cantidad, precio):
    
        cadena = producto
        obj = MisRegex()
        patron= obj.regex_producto()
        if(re.match(patron, cadena)):
            print(producto, cantidad, precio)
            con=self.conexion()
            cursor=con.cursor()
            data=(producto, cantidad, precio)
            sql="INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
            cursor.execute(sql, data)
            con.commit()
            print("Estoy en alta todo ok")
        else:
            print("error en campo producto")

    def consultar(self, compra):
        
        print(compra)

    def borrar(self, tree):
        valor = tree.selection()
        print(valor)   #('I005',)
        item = tree.item(valor)
        print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
        print(item['text'])
        mi_id = item['text']

        con=self.conexion()
        cursor=con.cursor()
        #mi_id = int(mi_id)
        data = (mi_id,)
        sql = "DELETE FROM productos WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(valor)


    def consultat(self,  ):

        sql = "SELECT * FROM productos ORDER BY id ASC"
        con=self.conexion()
        cursor=con.cursor()
        datos=cursor.execute(sql)
        return datos

 