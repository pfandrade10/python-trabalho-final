from django.http.response import HttpResponse
from meuapp.models.Classificacao import CLASSIFICACAO_CHOICE
from meuapp.models import Classificacao
from django.http.request import HttpRequest
from django.shortcuts import render


def create_category(request: HttpRequest):
  if request.method == 'GET':
    category_type = CLASSIFICACAO_CHOICE
    return render(request, 'category/create.html', { 'classificacao': category_type })
  else:
    data = request.POST
    _name = data['nome']
    _description = data['descricao']
    _type = data['classificacao']

    category = Classificacao(nome=_name, descricao=_description, classificacao=_type)

    category.save()

    categories = Classificacao.objects.all()

    return render(request, 'category/list.html', { 'categories': categories })


