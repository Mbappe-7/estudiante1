from django.shortcuts import render, get_object_or_404, redirect
from .models import Programa, Materia, Estudiante
from .forms import ProgramaForm, EstudianteForm
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
    
    # Total de estudiantes en la base de datos
    total_estudiantes = Estudiante.objects.count()

    return render(request, "estudiantes/detalle_estudiante.html", {
        "estudiante": estudiante,
        "total_estudiantes": total_estudiantes
    })
# -------------------------------------------------
def crear_programa(request):
    if request.method == "POST":
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiantes:lista_programas")
    else:
        form= ProgramaForm()
    return render(request, "estudiantes/crear_programa.html",{"form": form})

def editar_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)

    if request.method == "POST":
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect("estudiantes:detalle_programa", pk=programa.pk)
    else:
        form =ProgramaForm(instance=programa)
        
    return render(request, "estudiantes/editar_programa.html", {"form": form, "programa": programa})
    
def eliminar_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)

    if request.method == "POST":  
        programa.delete()
        return redirect("estudiantes:lista_programas")

    # si es GET, mostrar confirmación
    return render(request, "estudiantes/eliminar_programa.html", {"programa": programa})
#------------------------------------------------
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "estudiantes/lista_estudiantes.html", {"estudiantes": estudiantes})

# CREAR
def crear_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiantes:lista_estudiantes")
    else:
        form = EstudianteForm()
    return render(request, "estudiantes/crear_estudiante.html", {"form": form})

# DETALLE
def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, "estudiantes/detalle_estudiante.html", {"estudiante": estudiante})

# EDITAR
def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect("estudiantes:detalle_estudiante", pk=estudiante.pk)
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, "estudiantes/editar_estudiante.html", {"form": form, "estudiante": estudiante})

# ELIMINAR
def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        estudiante.delete()
        return redirect("estudiantes:lista_estudiantes")
    return render(request, "estudiantes/eliminar_estudiante.html", {"estudiante": estudiante})


