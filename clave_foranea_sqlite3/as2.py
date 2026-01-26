import sqlite3

con= sqlite3.connect('empresa.db')
cursor = con.cursor()
data = ("pelotas", )
sql = "INSERT INTO categoria(nombre) VALUES( ?)"
cursor.execute(sql, data)
con.commit()


cursor = con.cursor()
data = ("pelotas", 1)
sql = "INSERT INTO producto(nombre, categoria_id) VALUES(?, ?)"
cursor.execute(sql, data)
con.commit()