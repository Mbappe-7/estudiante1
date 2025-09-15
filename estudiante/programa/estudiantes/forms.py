from django import forms
from .models import Programa, Estudiante
class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields= ['nombre', 'descripcion', 'estado']

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Nombre del programa"
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Breve descripcion"
            }),
            "estado": forms.Select(attrs={
                "class": "form-select"
            }),
        }



class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre", "edad", "materias", "programa"]

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Nombre completo del estudiante"
            }),
            "edad": forms.NumberInput(attrs={
                "min": 1,
                "placeholder": "Edad"
            }),
            "materias": forms.CheckboxSelectMultiple(),  # permite marcar varias materias
            "programa": forms.Select(attrs={
                "class": "form-select"
            }),
        }