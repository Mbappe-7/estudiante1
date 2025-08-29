from django.urls import path
from . import views

app_name = "estudiantes"

urlpatterns = [
    path("", views.home, name="home"),

    # Programas
    path("programas/", views.lista_programas, name="lista_programas"),
    path("programas/<int:pk>/", views.detalle_programa, name="detalle_programa"),

    # Materias
    path("materias/", views.lista_materias, name="lista_materias"),
    path("materias/<int:pk>/", views.detalle_materia, name="detalle_materia"),

    # Estudiantes
    path("estudiantes/", views.lista_estudiantes, name="lista_estudiantes"),
    path("estudiantes/<int:pk>/", views.detalle_estudiante, name="detalle_estudiante"),
]
