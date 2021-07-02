from django.db import models

class Classificacao(models.Model):
    nome= models.CharField
    descricao = models.CharField
    dataInclusao = models.DateTimeField