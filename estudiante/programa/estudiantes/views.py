from django.shortcuts import render, get_object_or_404
from .models import Programa, Materia, Estudiante

def home(request):
    return render(request, "estudiantes/home.html", {})


def lista_programas(request):
    programas = Programa.objects.all().order_by("nombre")
    return render(request, "estudiantes/lista_programas.html", {"programas": programas})

def detalle_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    materias = programa.materias.all()
    estudiantes = programa.estudiante_set.all()
    return render(request, "estudiantes/detalle_programa.html", {
        "programa": programa,
        "materias": materias,
        "estudiantes": estudiantes
    })

# ---------------- MATERIAS ----------------
def lista_materias(request):
    materias = Materia.objects.select_related("programa").all().order_by("nombre")
    return render(request, "estudiantes/lista_materias.html", {"materias": materias})

def detalle_materia(request, pk):
    materia = get_object_or_404(Materia.objects.select_related("programa"), pk=pk)
    estudiantes = materia.estudiantes.all()
    return render(request, "estudiantes/detalle_materia.html", {
        "materia": materia,
        "estudiantes": estudiantes
    })

# ---------------- ESTUDIANTES ----------------
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.select_related("programa").prefetch_related("materias").order_by("nombre")
    return render(request, "estudiantes/lista_estudiantes.html", {"estudiantes": estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(
        Estudiante.objects.select_related("programa").prefetch_related("materias"),
        pk=pk
    )
    return render(request, "estudiantes/detalle_estudiante.html", {"estudiante": estudiante})
