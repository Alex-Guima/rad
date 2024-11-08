from peewee import Model, ForeignKeyField, BooleanField, CompositeKey

from aluno import Aluno
from materia import Materia


class Aluno_Materia(Model):
  aluno = ForeignKeyField(Aluno)
  materia = ForeignKeyField(Materia)
  isAprovado = BooleanField()

  class Meta:
    primary_key = CompositeKey('aluno', 'materia')
