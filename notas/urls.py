from django.urls import path

from . import views

app_name = "notas"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:matricula>/", views.detail, name="detail"),
    path("<int:matricula>/materias/", views.detail_materia, name="detail_materia"),
]
