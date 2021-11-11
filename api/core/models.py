from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


# Create your models here.
