import psycopg
from uuid import uuid4 as gen_uuid
import datetime
from peewee import AutoField, BooleanField, DateField, DateTimeField, ForeignKeyField, Model, CharField, UUIDField

class Aluno(Model):
  id = UUIDField(primary_key=True, verbose_name='Matrícula', unique=True, default=gen_uuid())
  status_matricula = BooleanField(default=True)
  name = CharField()
  data_nascimento = DateField()
  campus = CharField()
  serie = CharField()
  data_matricula = DateTimeField(default=datetime.datetime.now)
