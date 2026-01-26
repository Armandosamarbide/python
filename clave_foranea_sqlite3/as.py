import sqlite3

con= sqlite3.connect('empresa.db')
sql = '''CREATE TABLE IF NOT EXISTS categoria(
    id integer PRIMARY KEY AUTOINCREMENT, 
    nombre text)'''
con.execute(sql)
sql = '''CREATE TABLE IF NOT EXISTS producto(
    id integer PRIMARY KEY AUTOINCREMENT, 
    nombre text, 
    categoria_id id integer, 
    FOREIGN KEY(categoria_id) REFERENCES categoria(id))'''
 
con.execute(sql)
con.close()