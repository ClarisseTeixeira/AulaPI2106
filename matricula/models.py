from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=250)
    sigla_estado = models.CharField(max_length=2)
    def __str__(self):
        return self.nome + "-" + self.sigla_estado

class Curso(models.Model):
    nome = models.CharField(max_length=250)
    def __str__(self):
        return self.nome

class Matricula(models.Model):
    nome_aluno = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_aluno