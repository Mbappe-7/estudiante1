from django.shortcuts import render, get_object_or_404, redirect
from .models import Programa, Materia, Estudiante
from .forms import ProgramaForm
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

def crear_programa(request):
    if request.method == "POST":
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiantes:lista_programa")
    else:
        form= ProgramaForm()
    return render(request, "estudiantes/crear_programa.html",{"form": form})

def editar_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)

    if request.method == "POST":
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect("estudiates:detalle_programa", pk=programa.pk)
        else:
            form =ProgramaForm(instance=programa)

        return render(request, "estudiantes/editar_programa.html", {"from": form})
    
def eliminar_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)

    if request.method == "POST":  
        programa.delete()
        return redirect("estudiantes:lista_programa")

    # si es GET, mostrar confirmación
    return render(request, "estudiantes/eliminar_programa.html", {"programa": programa})
