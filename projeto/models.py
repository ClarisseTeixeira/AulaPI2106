from django.db import models

# Create your models here.

class Projeto(models.Model):
    nome= models.CharField(max_length=250)
    descricao = models.TextField()
    data_criacao = models.DateField()
    
