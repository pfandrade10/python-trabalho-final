from django.db import models
from . import  Classificacao
from django.db.models.aggregates import Sum

SITUACAO_CHOICE = (('N', 'a Pagar'), ('S','Pago'))
PAGAMENTO_CHOICE = (('D','Dinheiro'), ('CD','Débito'), ('CC','Crédito'), ('B','Boleto'))

class ContaPagarManager(models.Manager):
  def get_sum_pay_month(self, month, year):
    sum_month = float(ContaPagar.objects.filter(validade__month=month, validade__year=year).aggregate(Sum('valor'))['valor__sum'] or 0)
    return sum_month

  def get_sum_pays_category(self, month, year):
    categories = Classificacao.objects.all().count()
    pays = []

    for i in range(1, categories):
      sum_pays = float(ContaPagar.objects.filter(validade__month=month, validade__year=year, category=i).aggregate(Sum('valor'))['valor__sum'] or 0)
      pay = {
        'category': Classificacao.objects.get(id=i),
        'sum_pays': sum_pays
      }
      if sum_pays > 0:
        pays.append(pay)
      
    return pays

class ContaPagar(models.Model):
    valor = models.FloatField()
    descricao = models.CharField(max_length=250, null=True, blank=True)
    situacao = models.CharField(max_length=10, choices=SITUACAO_CHOICE, default='N')
    formaPagamento = models.CharField(max_length=10, choices=PAGAMENTO_CHOICE, default='D')
    validade = models.DateField(null=True, blank=True)
    dataPagamento = models.DateField(null=True, blank=True)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
    objects = ContaPagarManager()
	