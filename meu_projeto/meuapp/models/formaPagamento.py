from django.db import models

class FormaPagamento(models.Model):
    nome = models.CharField
    descricao = models.CharField
    dataInclusao = models.DateTimeField