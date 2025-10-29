import mysql.connector

def crear_base():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="discos"
    )

def crear_tabla():
    con = crear_base()
    cursor = con.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS listadiscos (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        titulo VARCHAR(100) NOT NULL,
        artista VARCHAR(30) NOT NULL,
        anio INT(4),
        genero VARCHAR(30)
    )
    """
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()
