from django.db import models

class Aluno(models.Model):
    CAMPUS_CHOICES = {
        RECREIO: "campus_recreio",
        TAQUARA: "campus_taquara",
        BARRA_DA_TIJUCA: "campus_barra_da_tijuca",
    }
    matricula = models.CharField(max_lenght=12, primary_key=True)
    nome = models.CharField(max_lenght=50, null=False)
    campus = models.CharField(choices=CAMPUS_CHOICES)
    serie = models.CharField()


