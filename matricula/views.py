from django.shortcuts import render
from .forms import MatriculaForm, CursoForm
from .models import Matricula
# Create your views here.

def criar_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            form = MatriculaForm()
    else:
        form = MatriculaForm()
    return render(request, 'matricula\criar_matricula.html', {'form': form})

def cadastrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            form = CursoForm()
    else:
        form = CursoForm()
    return render(request, 'matricula\cadastrar_curso.html', {'form': form})
