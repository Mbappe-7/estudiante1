from django import forms
from .models import Programa

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