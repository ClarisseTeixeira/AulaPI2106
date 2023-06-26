from django.shortcuts import render
from .forms import ProjetoForm
from .models import Projeto
# Create your views here.

def cadastro_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProjetoForm()
    else:
        form = ProjetoForm()
    return render(request, 'projeto\cadastro_projeto.html', {'form': form})