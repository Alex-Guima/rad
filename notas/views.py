from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.template import loader

from .models import Aluno, Materia

# Create your views here.
def index(request):
    lista_alunos_ativos = get_list_or_404(Aluno, status_matricula=True)
    template = loader.get_template("notas/index.html")
    context = {
        "lista_alunos_ativos": lista_alunos_ativos,
    }
    return render(request, "notas/index.html", context)

def detail(request, matricula):
    aluno = get_object_or_404(Aluno, pk=matricula)
    return render(request, "notas/detail.html", {"aluno": aluno})

def materias_matriculadas(request, matricula):
    aluno = get_object_or_404(Aluno, pk=matricula)
    materias = aluno.materiasMatriculadas.all()
    return render(request, "notas/materias_matriculadas.html", {"materias": materias})
