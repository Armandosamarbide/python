import os
from peewee import SqliteDatabase, Model, CharField, IntegerField, DateField, FloatField

ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(ruta_script, "gestion_seguros.db")

db = SqliteDatabase(ruta_db)

class BaseModel(Model):
    class Meta:
        database = db

class Poliza(BaseModel):
    nombre = CharField()
    apellido = CharField()
    marca = CharField()
    modelo = CharField()
    anio = IntegerField()
    empresa = CharField()
    dominio = CharField()
    uso_vehiculo = CharField()
    numero_poliza = CharField()
    tipo_cobertura = CharField()
    fecha_inicio = DateField()
    fecha_vencimiento = DateField()
    importe = FloatField()
