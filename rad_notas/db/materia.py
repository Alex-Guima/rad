import datetime
from peewee import CharField, Check, Model, AutoField, ForeignKeyField, DateTimeField
from aluno import Aluno


class Materia(Model):
  name = CharField(null=False, verbose_name='Nome da Materia', unique=True, primary_key=True)
  carga_horaria = CharField(null=False, verbose_name='Carga Horária da Materia')
  professor = CharField(null=False, verbose_name='Professor alocado na Materia')
  metodo_avaliativo = CharField(null=False, verbose_name='Metodo Avaliativo da Materia', constraints = [Check('metodo_avaliativo IN ("PROVA", "NF")')])
  created_at = DateTimeField(default=datetime.datetime.now)
  updated_at = DateTimeField(default=datetime.datetime.now)
