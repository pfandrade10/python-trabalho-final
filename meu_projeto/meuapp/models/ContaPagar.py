from django.db import models
from . import formaPagamento, classificao

class ContaPagar(models.Model):
    dataVencimento = models.DateTimeField
    dataPagamento = models.DateTimeField
    valor = models.FloatField
    descricao = models.CharField
    situacao = [('S','Pago'), ('N','A Pagar')]
    formaDePagamento = models.OneToOneField(formaPagamento)
    classificacao = models.OneToOneField(classificao)
	