import mysql.connector

base = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="discos"
)

cursor = base.cursor()

## Creación de la BBDD si no existe

cursor.execute("CREATE DATABASE IF NOT EXISTS discos")

## Creación de la tabla si no existe

cursor.execute("CREATE TABLE IF NOT EXISTS listadiscos( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, "
                 "titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, "
                 "artista VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, "
                 "anio int(4) COLLATE utf8_spanish2_ci, "
                 "genero VARCHAR(25) COLLATE utf8_spanish2_ci NOT NULL )")

## Alta de un registro

## sql = "INSERT INTO listadiscos(titulo, artista, anio, genero) VALUES (%s, %s, %s, %s)"
## datos = ("Stationary Traveler","Camel","1984", "Rock Progresivo")
## cursor.execute(sql,datos)
 
## base.commit()

print("Cantidad de Registros Agregados",cursor.rowcount)

sql = "DELETE FROM listadiscos WHERE id=%s"
dato = ('5',)

cursor.execute(sql,dato)

base.commit()

print("Registros Borrados ",cursor.rowcount)


