import mysql.connector

## Conectamos a la BBDD

def crear_base():
            return mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="discos"
            )

    