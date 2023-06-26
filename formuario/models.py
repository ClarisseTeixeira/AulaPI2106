from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    data_nascimento = models.DateField()

class Professor(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    disciplina = models.CharField(max_length=250)
    nome_mãe = models.CharField(max_length=250, null=True, blank=True)