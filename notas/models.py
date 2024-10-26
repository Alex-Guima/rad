import datetime

from django.http import HttpResponse

from django.db import models
from django.db.models.functions import Now

from django.utils import timezone

class Aluno(models.Model):
    CAMPUS_CHOICES = {
        "RECREIO": "campus_recreio",
        "TAQUARA": "campus_taquara",
        "BARRA_DA_TIJUCA": "campus_barra_da_tijuca",
    }
    matricula = models.BigAutoField(primary_key=True)
    status_matricula = models.BooleanField(default=True, null=False)
    nome = models.CharField(max_length=50, null=False)
    campus = models.CharField(choices=CAMPUS_CHOICES, null=False)
    serie = models.CharField()
    created_at = models.DateTimeField(db_default=Now(), editable=False)

    def __str__(self):
        return self.nome


class Materia(models.Model):
    NOMES_MATERIAS = {
        "MATEMATICA": "matematica",
        "PORTUGUES": "portugues",
        "HISTORIA": "historia",
        "GEOGRAFIA": "geografia",
        "CIENCIAS": "ciencias",
        "INGLES": "ingles",
        "EDUCACAO_FISICA": "educacao_fisica",
    }
    nome = models.CharField(max_length=50, null=False, choices=NOMES_MATERIAS)
    carga_horaria = models.IntegerField()
    professor = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(db_default=Now(), editable=False)
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.nome
