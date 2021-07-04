from django.http.response import HttpResponse
from meuapp.models import Classificacao
from meuapp.models.Classificacao import Classificacao
from meuapp.models.ContaPagar import PAGAMENTO_CHOICE, ContaPagar, SITUACAO_CHOICE
from django.http.request import HttpRequest
from django.shortcuts import redirect, render, resolve_url

def create_pay_bills(request: HttpRequest):
  categories = Classificacao.objects.filter(classificacao='D')
  if request.method == 'GET':
    payment = PAGAMENTO_CHOICE
    status = SITUACAO_CHOICE
    return render(request, 'finances/pay/create.html', {
      'payment': payment,
      'status': status,
      'categories': categories,
     })
  else:
    data = request.POST
    _value = data['valor']
    _description = data['descricao']
    _due_date = data['validade']
    _pay_date = data['dataPagamento']
    _payment = data['formaPagamento']
    _status = data['situcao']
    _category_id = data['classificacao']

    category = Classificacao.objects.get(id=_category_id)

    ContaPagar.objects.create(valor=_value, descricao=_description, validade=_due_date, dataPagamento=_pay_date, formaPagamento=_payment, situcao=_status, classificacao=category)

    return redirect(resolve_url('home'))