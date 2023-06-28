from django.contrib import admin
from .models import Matricula, Cidade, Curso

# Register your models here.

admin.site.register(Matricula)
admin.site.register(Cidade)
admin.site.register(Curso)