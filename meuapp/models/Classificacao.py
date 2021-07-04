from django.db import models

CLASSIFICACAO_CHOICE = (('D','Despesa'), ('R','Receita'))   
class Classificacao(models.Model):
    nome= models.CharField(max_length=150)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    classificacao = models.CharField(choices=CLASSIFICACAO_CHOICE, default='D', max_length=10)