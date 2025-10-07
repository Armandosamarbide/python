import mysql.connector

base = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 ## database="discos"
)

cursor = base.cursor()
cursor.execute("CREATE DATABASE discos")

cursor.execute("CREATE TABLE listadiscos (id int(6) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo varchar(128) COLLATE utf8_spanish2_ci NOT NULL, artista varchar(128) COLLATE utf8_spanish2_ci NOT NULL, anio int(4) COLLATE utf8_spanish2_ci NOT NULL, genero varchar(40) COLLATE utf8_spanish2_ci NOT NULL,)")