# Generated by Django 5.1.2 on 2024-10-24 12:10

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0005_rename_createdat_aluno_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='materias_matriculadas',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='alunos_matriculados',
        ),
        migrations.AddField(
            model_name='materia',
            name='alunos',
            field=models.ManyToManyField(to='notas.aluno'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='created_at',
            field=models.DateTimeField(db_default=django.db.models.functions.datetime.Now(), editable=False),
        ),
    ]
