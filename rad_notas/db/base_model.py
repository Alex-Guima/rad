from peewee import Model
import psycopg


db = psycopg.connect("db=notas_rad user=notas_admin")

class BaseModel(Model):
    class Meta:
        database = db
