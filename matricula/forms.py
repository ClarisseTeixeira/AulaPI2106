from django import forms
from .models import Matricula, Curso

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'

        widgets = {
            'nome_aluno': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'})
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }
