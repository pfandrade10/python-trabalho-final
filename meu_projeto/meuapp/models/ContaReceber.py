from django.db import models
from . import formaPagamento, classificao

class ContaPagar(models.Model):
    dataExpectativa = models.DateTimeField(null=True)
    dataRecebimento = models.DateTimeField(null=True) 
    valor = models.FloatField
    descricao = models.CharField
    situacao = [('S','Recebido'), ('N','A Receber')]
    formaRecebimento = models.OneToOneField(formaPagamento)
    classificacao = models.OneToOneField(classificao)