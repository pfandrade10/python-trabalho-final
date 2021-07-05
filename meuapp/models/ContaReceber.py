from django.db import models
from django.db.models.aggregates import Sum
from . import  Classificacao

SITUACAO_CHOICE = (('N', 'a Receber'), ('S','Recebido'))

class ContaReceberManager(models.Manager):
  def get_sum_receive_month(self, month, year):
    sum_month = float(ContaReceber.objects.filter(dataRecebimento__month=month, dataRecebimento__year=year).aggregate(Sum('valor'))['valor__sum'] or 0)
    return sum_month
  
  def get_sum_receives_category(self, month, year):
    categories = Classificacao.objects.all().count()
    receives = []

    for i in range(1, categories):
      sum_receives = float(ContaReceber.objects.filter(dataRecebimento__month=month, dataRecebimento__year=year, classificacao=i).aggregate(Sum('valor'))['valor__sum'] or 0)
      pay = {
        'category': Classificacao.objects.get(id=i),
        'sum_receives': sum_receives
      }
      if sum_receives > 0:
        receives.append(pay)
      
    return receives

class ContaReceber(models.Model):
    valor = models.FloatField()
    descricao = models.CharField(max_length=200, null=True, blank=True)
    situacao = models.CharField(max_length=10, choices=SITUACAO_CHOICE, default='N')
    dataRecebimento = models.DateField()
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
    objects = ContaReceberManager()