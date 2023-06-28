from django import forms
from .models import Matricula

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'

        widgets = {
            'nome_aluno': forms.TextInput(attrs={'class': 'form-label'})
        }