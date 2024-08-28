from django.db import models

class Tb_culturas(models.Model):
    index = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tb_armazem(models.Model):
    index = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
