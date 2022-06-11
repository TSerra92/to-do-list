from django.db import models


# Create your models here.
class Task(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=256)
    local = models.CharField(max_length=80)
    data = models.DateField(auto_now=False,auto_now_add=False)
    hora = models.TimeField(auto_now=False,auto_now_add=False)
    

    def  __str__(self):
        return self.nome
