import sqlite3                         # <------ IMPORTAMOS MÓDULO DE SQLITE 3

## Creamos la Base de datos

def crear_base():
    con = sqlite3.connect('martin.db')
    return con

crear_base()

## Creamos la tabla, que recibe como parámetro una conexión a la BBDD

def crear_tabla(con):
    
    ## Con el cursor podemos ejecutar sentencias SQL sobre con.
    
    cursor = con.cursor()
    
    ## Todo ese choclo se guarda en la variable sql
    
    sql = """CREATE TABLE IF NOT EXISTS discos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             producto varchar(20) NOT NULL,
             cantidad real,
             precio real)
    """
    cursor.execute(sql)
    con.commit()
crear_tabla(crear_base())