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
    path("programa/nuevo/", views.crear_programa, name="crear_programa"),
    path("programa/<int:pk>/editar/", views.editar_programa, name="editar_programa"),
    path("programa/<int:pk>/eliminar/", views.eliminar_programa, name="eliminar_programa"),

    path("estudiantes/nuevo/", views.crear_estudiante, name="crear_estudiante"),
    
    path("estudiantes/<int:pk>/editar/", views.editar_estudiante, name="editar_estudiante"),
    path("estudiantes/<int:pk>/eliminar/", views.eliminar_estudiante, name="eliminar_estudiante"),
]
