from django.http.response import HttpResponse
from meuapp.models.ContaReceber import ContaReceber, SITUACAO_CHOICE
from meuapp.models.Classificacao import Classificacao
from django.http.request import HttpRequest
from django.shortcuts import redirect, render, resolve_url

def create_receive_bills(request: HttpRequest):
  categories = Classificacao.objects.filter(classificacao='R')
  if request.method == 'GET':
    status = SITUACAO_CHOICE
    return render(request, 'finances/receive/create.html', {
      'status': status,
      'categories': categories,
    })
  else:
    data = request.POST
    _value = data['valor']
    _description = data['descricao']
    _receive_date = data['dataRecebimento']
    _status = data['situacao']
    _category_id = data['classificacao']

    category = Classificacao.objects.get(id=_category_id)

    ContaReceber.objects.create(valor=_value, descricao=_description, dataRecebimento=_receive_date, situacao=_status, classificacao=category)

    return redirect(resolve_url('home'))
