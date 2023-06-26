from django import forms
from .models import Professor


class ProfessorForm(forms.ModelForm):
    class Meta: 
        model = Professor
        fields = '__all__'

# Create your models here.
class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=250)
    email = forms.EmailField()
    data_nascimento = forms.DateField()